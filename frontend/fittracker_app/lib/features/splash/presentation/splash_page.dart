import '../../auth/domain/auth_state.dart';
// lib/features/splash/presentation/splash_page.dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:flutter/foundation.dart';

import '../../../shared/di.dart';
import '../../../shared/widgets/progresso_logo.dart';

class SplashPage extends ConsumerStatefulWidget {
  const SplashPage({super.key});
  @override
  ConsumerState<SplashPage> createState() => _SplashPageState();
}

class _SplashPageState extends ConsumerState<SplashPage> with SingleTickerProviderStateMixin {
  ProviderSubscription<AuthState>? _authListener;
  late final AnimationController _ac;
  late final Animation<double> _t;

  @override
  void initState() {
    super.initState();
    _ac = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1800),
    )..repeat();
    _t = CurvedAnimation(parent: _ac, curve: Curves.easeInOut);

    const useFakeAuth = kDebugMode && bool.fromEnvironment('FAKE_AUTH', defaultValue: false);
    if (useFakeAuth) {
      // Auto-login fake: inmediato
      final controller = ref.read(authControllerProvider.notifier);
      try {
        // ignore: avoid_dynamic_calls, invalid_use_of_protected_member
        (controller as dynamic).signInDev?.call();
      } catch (_) {}
      // Si ya está autenticado, redirige de inmediato
      if (ref.read(authControllerProvider).isAuthenticated) {
        WidgetsBinding.instance.addPostFrameCallback((_) {
          if (mounted) context.go('/dashboard');
        });
        return;
      }
      // Si no, escucha el provider y redirige cuando cambie a autenticado
      _authListener = ref.listenManual(authControllerProvider, (prev, next) {
        if (next.isAuthenticated && mounted) {
          context.go('/dashboard');
        }
      });
      return;
    }
    // En real, sí espera el splash
    Future.delayed(const Duration(milliseconds: 2600), () async {
      if (!mounted) return;
      final isAuth = ref.read(authControllerProvider).isAuthenticated;
      context.go(isAuth ? '/dashboard' : '/welcome');
    });
  }

  @override
  void dispose() {
    _ac.dispose();
  _authListener?.close();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final cs = Theme.of(context).colorScheme;
    final tt = Theme.of(context).textTheme;

    return Scaffold(
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topCenter, end: Alignment.bottomCenter,
            colors: [cs.surface, cs.surface],
          ),
        ),
        child: SafeArea(
          child: Center(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                // ✅ El logo NO se rebuild por frame
                const ProgressoLogoCircularFade(
                  size: 160,
                  period: Duration(milliseconds: 2400),
                  repeat: true, // loop
                ),

                const SizedBox(height: 16),

                // ✅ Solo el texto se anima por frame
                AnimatedBuilder(
                  animation: _t,
                  builder: (_, __) => _TextSweep(
                    progress: _t.value,
                    text: 'Progresso',
                    baseStyle: tt.headlineMedium?.copyWith(
                      fontWeight: FontWeight.w600,
                      height: 1.05,
                      fontSize: 36,
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

// ── Tu _TextSweep como ya lo tienes ───────────────────────────────────────────
class _TextSweep extends StatelessWidget {
  const _TextSweep({
    required this.progress,
    required this.text,
    required this.baseStyle,
  });
  final double progress;
  final String text;
  final TextStyle? baseStyle;

  @override
  Widget build(BuildContext context) {
    final cs = Theme.of(context).colorScheme;
    final dx = -0.40 + progress * 1.80;

    return ShaderMask(
      blendMode: BlendMode.srcIn,
      shaderCallback: (bounds) {
        return LinearGradient(
          begin: Alignment(dx - 0.25, 0.0),
          end: Alignment(dx + 0.25, 0.0),
          colors: [
            cs.tertiary,
            cs.secondary,
            cs.primary,
            cs.secondary.withValues(alpha: .95),
            cs.tertiary,
          ],
          stops: const [0.0, 0.35, 0.50, 0.65, 1.0],
        ).createShader(bounds);
      },
      child: Text(text, textAlign: TextAlign.center, style: baseStyle),
    );
  }
}
