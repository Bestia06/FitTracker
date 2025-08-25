import 'package:go_router/go_router.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter/widgets.dart';

import '../../shared/di.dart';
import '../../features/auth/presentation/login_page.dart';
import '../../features/lagepage/presentation/lage_page.dart';
import '../../features/dashboard/presentation/pages/home_page.dart';
import '../../features/auth/presentation/register_page.dart';
import '../../features/splash/presentation/splash_page.dart';

// import '../../features/admin/presentation/pages/admin_page.dart'; // si la usas

final appRouter = GoRouter(
  initialLocation: '/splash',
  redirect: (context, state) {
    final path = state.matchedLocation;

    // ✅ 1) ¡Deja pasar la splash! (no la interceptes)
    if (path == '/splash') return null;

    final container = ProviderScope.containerOf(context, listen: false);
    final auth = container.read(authControllerProvider);

    // ✅ 2) Rutas públicas que SÍ puede ver sin login
    final isPublic = path == '/welcome' || path == '/login' || path == '/register';

    // ✅ 3) Si NO está autenticado y quiere ir a algo privado → mándalo a /welcome (no a /login)
    if (!auth.isAuthenticated && !isPublic) return '/welcome';

    // ✅ 4) Si SÍ está autenticado y quiere ir a páginas públicas → al dashboard
    if (auth.isAuthenticated && isPublic) return '/dashboard';

    return null;
  },
  routes: [
    GoRoute(path: '/splash', builder: (c, s) => const SplashPage()),
    GoRoute(path: '/welcome', builder: (c, s) => const WelcomePage()),
    GoRoute(path: '/login', builder: (c, s) => const LoginScreen()),
  GoRoute(path: '/dashboard', builder: (c, s) => const HomePage()),
    GoRoute(path: '/register', builder: (c, s) => const SignUpPage()),

    // GoRoute(path: '/admin', builder: (c, s) => const AdminPage()),
  ],
);
