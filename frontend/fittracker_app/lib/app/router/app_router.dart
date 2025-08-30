import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

import '../../core/providers/providers.dart';
import '../../features/auth/presentation/screens/login_screen.dart';
import '../../features/auth/presentation/screens/register_screen.dart';
import '../../features/dashboard/presentation/screens/dashboard_screen.dart';
import '../../features/habits/presentation/screens/habits_screen.dart';
import '../../features/lagepage/presentation/lage_page.dart';
import '../../features/notifications/presentation/screens/notifications_screen.dart';
import '../../features/nutrition/presentation/screens/nutrition_screen.dart';
import '../../features/profile/presentation/screens/profile_screen.dart';
import '../../features/splash/presentation/splash_page.dart';
import '../../features/workouts/presentation/screens/workouts_screen.dart';
import '../../shared/widgets/splash_screen.dart';

// import '../../features/admin/presentation/pages/admin_page.dart'; // si la usas

final appRouter = GoRouter(
  initialLocation: '/',
  redirect: (context, state) {
    final path = state.matchedLocation;

    // Permitir splash screen
    if (path == '/' || path == '/splash') return null;

    final container = ProviderScope.containerOf(context, listen: false);
    final appState = container.read(appStateProvider);

    // Rutas públicas
    final isPublic =
        path == '/welcome' || path == '/login' || path == '/register';

    // Si no está autenticado y quiere ir a algo privado → login
    if (!appState.isAuthenticated && !isPublic) return '/login';

    // Si está autenticado y quiere ir a páginas públicas → dashboard
    if (appState.isAuthenticated && isPublic) return '/dashboard';

    return null;
  },
  routes: [
    GoRoute(path: '/', builder: (context, state) => const SplashScreen()),
    GoRoute(path: '/splash', builder: (context, state) => const SplashPage()),
    GoRoute(path: '/welcome', builder: (context, state) => const WelcomePage()),
    GoRoute(path: '/login', builder: (context, state) => const LoginScreen()),
    GoRoute(
      path: '/register',
      builder: (context, state) => const RegisterScreen(),
    ),
    ShellRoute(
      builder: (context, state, child) => MainScaffold(child: child),
      routes: [
        GoRoute(
          path: '/dashboard',
          builder: (context, state) => const DashboardScreen(),
        ),
        GoRoute(
          path: '/habits',
          builder: (context, state) => const HabitsScreen(),
        ),
        GoRoute(
          path: '/workouts',
          builder: (context, state) => const WorkoutsScreen(),
        ),
        GoRoute(
          path: '/nutrition',
          builder: (context, state) => const NutritionScreen(),
        ),
        GoRoute(
          path: '/notifications',
          builder: (context, state) => const NotificationsScreen(),
        ),
        GoRoute(
          path: '/profile',
          builder: (context, state) => const ProfileScreen(),
        ),
      ],
    ),
  ],
);

class MainScaffold extends ConsumerStatefulWidget {
  final Widget child;

  const MainScaffold({super.key, required this.child});

  @override
  ConsumerState<MainScaffold> createState() => _MainScaffoldState();
}

class _MainScaffoldState extends ConsumerState<MainScaffold> {
  int _currentIndex = 0;

  final List<NavigationItem> _navigationItems = [
    NavigationItem(
      icon: Icons.home_outlined,
      activeIcon: Icons.home,
      label: 'Home',
      route: '/dashboard',
    ),
    NavigationItem(
      icon: Icons.show_chart_outlined,
      activeIcon: Icons.show_chart,
      label: 'Stats',
      route: '/workouts',
    ),
    NavigationItem(
      icon: Icons.notifications_outlined,
      activeIcon: Icons.notifications,
      label: 'Notifications',
      route: '/notifications',
    ),
    NavigationItem(
      icon: Icons.person_outline,
      activeIcon: Icons.person,
      label: 'Personal',
      route: '/profile',
    ),
  ];

  @override
  Widget build(BuildContext context) {
    final currentRoute = GoRouterState.of(context).matchedLocation;
    _currentIndex = _navigationItems.indexWhere(
      (item) => item.route == currentRoute,
    );
    if (_currentIndex == -1) _currentIndex = 0;

    return Scaffold(
      body: widget.child,
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        onTap: (index) {
          context.go(_navigationItems[index].route);
        },
        type: BottomNavigationBarType.fixed,
        items: _navigationItems.map((item) {
          final isActive = _navigationItems.indexOf(item) == _currentIndex;
          return BottomNavigationBarItem(
            icon: Icon(
              item.icon,
              color: isActive
                  ? const Color(0xFF3B82F6)
                  : const Color(0xFF9CA3AF),
            ),
            activeIcon: Icon(
              item.activeIcon ?? item.icon,
              color: const Color(0xFF3B82F6),
            ),
            label: item.label,
          );
        }).toList(),
        selectedItemColor: const Color(0xFF3B82F6),
        unselectedItemColor: const Color(0xFF9CA3AF),
        backgroundColor: Colors.white,
        elevation: 8,
        selectedFontSize: 12,
        unselectedFontSize: 11,
      ),
    );
  }
}

class NavigationItem {
  final IconData icon;
  final IconData? activeIcon;
  final String label;
  final String route;

  NavigationItem({
    required this.icon,
    this.activeIcon,
    required this.label,
    required this.route,
  });
}
