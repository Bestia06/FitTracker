import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../domain/auth_state.dart';
import '../data/auth_repository.dart';

class AuthController extends StateNotifier<AuthState> {
  AuthController(this._repo) : super(AuthState.unauthenticated());

  final AuthRepository _repo;

  Future<void> signIn(String email, String password) async {
    final result = await _repo.login(email: email, password: password);
    state = AuthState(
      accessToken: result.access,
      refreshToken: result.refresh,
      roles: result.roles,
      isAuthenticated: true,
    );
  }

  Future<void> signOut() async {
    await _repo.logout();
    state = AuthState.unauthenticated();
  }

  bool hasRole(String role) => state.roles.contains(role);
}
