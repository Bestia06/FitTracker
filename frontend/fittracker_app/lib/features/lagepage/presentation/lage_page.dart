import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class WelcomePage extends StatelessWidget {
  const WelcomePage({super.key});

  @override
  Widget build(BuildContext context) {
    final cs = Theme.of(context).colorScheme;
    final tt = Theme.of(context).textTheme;

    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 24),
          child: Column(
            children: [
              const Spacer(flex: 2),

              // Logo desde assets (usa tu registro en pubspec.yaml)
              Image.asset(
                'assets/images/logo_grande.png',
                width: 140,
                height: 140,
                fit: BoxFit.contain,
              ),

              const SizedBox(height: 20),

              // Marca con fuente global (TheSeasons) y gradiente desde el ColorScheme
              GradientText(
                'Progresso',
                gradient: LinearGradient(
                  colors: [cs.tertiary, cs.secondary, cs.primary],
                ),
                style: tt.headlineMedium?.copyWith(
                  // headlineMedium viene del tema y ya usa TheSeasons
                  fontWeight: FontWeight.w400,
                  fontSize: 36,
                  height: 1.1,
                ),
              ),

              const Spacer(flex: 3),

              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  // OutlinedButton hereda estilos del tema (outlinedButtonTheme)
                  OutlinedButton(
                    onPressed: () => context.go('/login'),
                    child: const Text('Log In'),
                  ),
                  const SizedBox(width: 16),
                  // FilledButton hereda estilos del tema (filledButtonTheme)
                  FilledButton(
                    onPressed: () => context.go('/register'),
                    child: const Text('Sign up'),
                  ),
                ],
              ),

              const SizedBox(height: 24),
            ],
          ),
        ),
      ),
    );
  }
}

/// Texto con gradiente construido a partir del ColorScheme
class GradientText extends StatelessWidget {
  const GradientText(
    this.text, {
    super.key,
    required this.gradient,
    this.style,
  });

  final String text;
  final Gradient gradient;
  final TextStyle? style;

  @override
  Widget build(BuildContext context) {
    return ShaderMask(
      blendMode: BlendMode.srcIn,
      shaderCallback: (bounds) =>
          gradient.createShader(Rect.fromLTWH(0, 0, bounds.width, bounds.height)),
      child: Text(text, style: style),
    );
  }
}
