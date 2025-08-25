import 'package:dio/dio.dart';
import 'token_storage.dart';
import 'package:jwt_decoder/jwt_decoder.dart';

class ApiClient {
  ApiClient(this._storage) {
    _dio = Dio(BaseOptions(
      baseUrl: const String.fromEnvironment('API_BASE_URL', defaultValue: 'http://10.0.2.2:8080'),
      connectTimeout: const Duration(seconds: 10),
      receiveTimeout: const Duration(seconds: 20),
    ));

    _dio.interceptors.add(InterceptorsWrapper(
      onRequest: (options, handler) async {
        final at = await _storage.readAccess();
        if (at != null && at.isNotEmpty) {
          options.headers['Authorization'] = 'Bearer $at';
        }
        handler.next(options);
      },
      onError: (e, handler) async {
        // Si 401, intenta 1 vez refresh
        if (e.response?.statusCode == 401) {
          final newToken = await _refreshToken();
          if (newToken != null) {
            // Reintenta la request original con el token nuevo
            final req = e.requestOptions;
            req.headers['Authorization'] = 'Bearer $newToken';
            final clone = await _dio.fetch(req);
            return handler.resolve(clone);
          }
        }
        handler.next(e);
      },
    ));
  }

  late final Dio _dio;
  final TokenStorage _storage;

  Dio get dio => _dio;

  Future<String?> _refreshToken() async {
    final rt = await _storage.readRefresh();
    if (rt == null || rt.isEmpty) return null;
    try {
      final res = await _dio.post('/auth/refresh', data: {'refresh_token': rt});
      final access = res.data['access_token'] as String?;
      final refresh = res.data['refresh_token'] as String?;
      if (access == null) return null;
      await _storage.saveTokens(access: access, refresh: refresh);
      return access;
    } catch (_) {
      await _storage.clear();
      return null;
    }
  }

  // Utilidad: ¿está expirado el access token?
  Future<bool> isAccessExpired() async {
    final at = await _storage.readAccess();
    if (at == null) return true;
    return JwtDecoder.isExpired(at);
  }
}
