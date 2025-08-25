import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'api_client.dart';
import 'token_storage.dart';
import '../features/auth/data/auth_repository.dart';
import '../features/auth/application/auth_controller.dart';
import '../features/auth/domain/auth_state.dart';

final tokenStorageProvider = Provider<TokenStorage>((ref) => DefaultTokenStorage());
final apiClientProvider   = Provider<ApiClient>((ref) => ApiClient(ref.read(tokenStorageProvider)));
final authRepoProvider    = Provider<AuthRepository>((ref) => AuthRepository(ref.read(apiClientProvider), ref.read(tokenStorageProvider)));
final authControllerProvider = StateNotifierProvider<AuthController, AuthState>(
  (ref) => AuthController(ref.read(authRepoProvider)),
);
