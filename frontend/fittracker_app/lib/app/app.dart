import 'package:flutter/material.dart';
import 'router/app_router.dart';
import 'theme/app_theme.dart';

class FitTrackerApp extends StatelessWidget {
  const FitTrackerApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      routerConfig: appRouter,
      theme: AppTheme.light,
    );
  }
}
