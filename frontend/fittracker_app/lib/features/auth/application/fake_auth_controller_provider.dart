import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../data/fake_auth_provider.dart';

import '../domain/auth_state.dart';
import 'fake_auth_controller.dart';

final fakeAuthControllerProvider = StateNotifierProvider<FakeAuthController, AuthState>((ref) {
  return FakeAuthController(ref.read(fakeAuthRepositoryProvider));
});
