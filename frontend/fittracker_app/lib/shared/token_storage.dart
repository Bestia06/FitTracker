import 'package:flutter_secure_storage/flutter_secure_storage.dart';

abstract class TokenStorage {
  Future<void> saveTokens({required String access, String? refresh});
  Future<String?> readAccess();
  Future<String?> readRefresh();
  Future<void> clear();
}

class DefaultTokenStorage implements TokenStorage {
  final _s = const FlutterSecureStorage();
  @override
  Future<void> saveTokens({required String access, String? refresh}) async {
    await _s.write(key: 'access', value: access);
    if (refresh != null) await _s.write(key: 'refresh', value: refresh);
  }
  @override
  Future<String?> readAccess() => _s.read(key: 'access');
  @override
  Future<String?> readRefresh() => _s.read(key: 'refresh');
  @override
  Future<void> clear() async {
    await _s.delete(key: 'access');
    await _s.delete(key: 'refresh');
  }
}
