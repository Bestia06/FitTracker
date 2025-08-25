import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'fake_auth_repository.dart';

final fakeAuthRepositoryProvider = Provider<FakeAuthRepository>((ref) {
  final repo = FakeAuthRepository();
  ref.onDispose(repo.dispose);
  return repo;
});
