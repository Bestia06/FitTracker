import 'package:dio/dio.dart';
import '../../../shared/api_client.dart';
import '../../../shared/token_storage.dart';
import 'package:jwt_decoder/jwt_decoder.dart';

class AuthRepository {
  AuthRepository(this._api, this._storage);
  final ApiClient _api;
  final TokenStorage _storage;

  Future<({String access, String? refresh, Set<String> roles})> login({
    required String email, required String password,
  }) async {
    final Response res = await _api.dio.post('/auth/login', data: {
      'email': email, 'password': password,
    });
    final access = res.data['access_token'] as String?;
    final refresh = res.data['refresh_token'] as String?;
    if (access == null || access.isEmpty) throw Exception('Token inválido');

    await _storage.saveTokens(access: access, refresh: refresh);

    // Extrae roles del claim (ajusta llave según backend: "roles", "authorities", "role")
    final claims = JwtDecoder.decode(access);
    final dynamic raw = claims['roles'] ?? claims['authorities'] ?? claims['role'];
    final roles = switch (raw) {
      List list => list.map((e) => e.toString()).toSet(),
      String s   => {s},
      _          => <String>{},
    };

    return (access: access, refresh: refresh, roles: roles);
  }

  Future<void> logout() => _storage.clear();

  Future<Set<String>> currentRoles() async {
    final at = await _storage.readAccess();
    if (at == null || at.isEmpty || JwtDecoder.isExpired(at)) return {};
    final claims = JwtDecoder.decode(at);
    final raw = claims['roles'] ?? claims['authorities'] ?? claims['role'];
    if (raw is List) return raw.map((e) => e.toString()).toSet();
    if (raw is String) return {raw};
    return {};
  }
}
