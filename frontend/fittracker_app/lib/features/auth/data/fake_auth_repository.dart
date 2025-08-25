
import 'dart:async';
import 'package:flutter/foundation.dart';
import 'package:dio/dio.dart';
import 'auth_repository.dart';
import '../../../shared/api_client.dart';
import '../../../shared/token_storage.dart';

class FakeUser {
  final String id;
  final String email;
  final String displayName;
  const FakeUser({required this.id, required this.email, required this.displayName});
}

class _FakeApiClient implements ApiClient {
  _FakeApiClient();
  @override
  Dio get dio => throw UnimplementedError('FakeApiClient.dio is not used');
  @override
  Future<bool> isAccessExpired() async => false;
}

class _FakeTokenStorage implements TokenStorage {
  @override
  Future<void> saveTokens({required String access, String? refresh}) async {}
  @override
  Future<String?> readAccess() async => null;
  @override
  Future<String?> readRefresh() async => null;
  @override
  Future<void> clear() async {}
}

class FakeAuthRepository extends AuthRepository {

  FakeAuthRepository() : super(_FakeApiClient(), _FakeTokenStorage());

  FakeUser? _currentUser;
  final _controller = StreamController<FakeUser?>.broadcast();
  // Dependencias dummy para el super constructor

  FakeUser? get currentUser => _currentUser;
  Stream<FakeUser?> authStateChanges() => _controller.stream;

  // Fake login compatible con AuthRepository
  Future<({String access, String? refresh, Set<String> roles})> login({
    required String email,
    required String password,
  }) async {
    // Simula login exitoso
    _currentUser = FakeUser(id: 'dev123', email: email, displayName: 'Dev User');
    _controller.add(_currentUser);
    return (access: 'fake_access', refresh: 'fake_refresh', roles: {'DEV'});
  }

  Future<void> logout() async {
    _currentUser = null;
    _controller.add(null);
  }

  // Para el mecanismo de auto-login
  void signInDev() {
    _currentUser = const FakeUser(id: 'dev123', email: 'dev@demo.com', displayName: 'Dev User');
    _controller.add(_currentUser);
  }

  void dispose() => _controller.close();
}
