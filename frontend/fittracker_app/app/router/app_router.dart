import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../features/auth/presentation/pages/login_page.dart';
import '../../features/auth/presentation/pages/register_page.dart';
import '../../features/dashboard/presentation/pages/dashboard_page.dart';
import '../../features/workouts/presentation/pages/workouts_page.dart';
import '../../features/nutrition/presentation/pages/nutrition_page.dart';
import '../../features/stats/presentation/pages/stats_page.dart';
import '../../features/habits/presentation/pages/habits_page.dart';
import '../../features/profile/presentation/pages/profile_page.dart';

final appRouterProvider = Provider<GoRouter>((ref) {
  return GoRouter(
    initialLocation: '/login',
    routes: [
      // Auth routes
      GoRoute(
        path: '/login',
        builder: (context, state) => const LoginPage(),
      ),
      GoRoute(
        path: '/register',
        builder: (context, state) => const RegisterPage(),
      ),
      
      // Main app routes
      GoRoute(
        path: '/dashboard',
        builder: (context, state) => const DashboardPage(),
      ),
      GoRoute(
        path: '/workouts',
        builder: (context, state) => const WorkoutsPage(),
      ),
      GoRoute(
        path: '/nutrition',
        builder: (context, state) => const NutritionPage(),
      ),
      GoRoute(
        path: '/stats',
        builder: (context, state) => const StatsPage(),
      ),
      GoRoute(
        path: '/habits',
        builder: (context, state) => const HabitsPage(),
      ),
      GoRoute(
        path: '/profile',
        builder: (context, state) => const ProfilePage(),
      ),
      
      // Redirect root to dashboard
      GoRoute(
        path: '/',
        redirect: (context, state) => '/dashboard',
      ),
    ],
  );
});
