import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'app/app.dart';
import 'package:flutter/foundation.dart';
// import 'features/auth/data/fake_auth_provider.dart';
import 'features/auth/application/fake_auth_controller_provider.dart';
import 'shared/di.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  const useFakeAuth = kDebugMode && bool.fromEnvironment('FAKE_AUTH', defaultValue: false);
  runApp(
    ProviderScope(
      overrides: useFakeAuth
          ? [
              authControllerProvider.overrideWith((ref) => ref.read(fakeAuthControllerProvider.notifier) as dynamic),
            ]
          : [],
      child: const FitTrackerApp(),
    ),
  );
}
