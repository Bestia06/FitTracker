import '../domain/auth_state.dart';
import '../data/fake_auth_repository.dart';
import 'auth_controller.dart';

class FakeAuthController extends AuthController {
  FakeAuthController(FakeAuthRepository repo)
      : _repo = repo,
        super(repo
            as dynamic); // El super espera AuthRepository, pero no se usará

  final FakeAuthRepository _repo;

  void signInDev() {
    _repo.signInDev();
    state = AuthState(
      accessToken: null,
      refreshToken: null,
      roles: {'DEV'},
      isAuthenticated: true,
    );
  }

  @override
  Future<void> signOut() async {
    await _repo.logout();
    state = AuthState.unauthenticated();
  }
}
