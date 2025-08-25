import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';

class SignUpPage extends ConsumerStatefulWidget {
  const SignUpPage({super.key});
  @override
  ConsumerState<SignUpPage> createState() => _SignUpPageState();
}

class _SignUpPageState extends ConsumerState<SignUpPage> with SingleTickerProviderStateMixin {
  final _formKey = GlobalKey<FormState>();
  final _emailCtrl = TextEditingController();
  bool _submitting = false;

  @override
  void dispose() {
    _emailCtrl.dispose();
    super.dispose();
  }

  String? _validateEmail(String? v) {
    final value = (v ?? '').trim();
    if (value.isEmpty) return 'Required';
    final re = RegExp(r'^[^\s@]+@[^\s@]+\.[^\s@]+$');
    if (!re.hasMatch(value)) return 'Enter a valid email';
    return null;
  }

  Future<void> _onEmailContinue() async {
    if (!(_formKey.currentState?.validate() ?? false)) return;
    setState(() => _submitting = true);
    try {
      await Future<void>.delayed(const Duration(milliseconds: 500));
    } finally {
      if (mounted) setState(() => _submitting = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    final cs = Theme.of(context).colorScheme;
    final tt = Theme.of(context).textTheme;

    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).scaffoldBackgroundColor,
        elevation: 0,
        leading: IconButton(
          icon: const Icon(Icons.arrow_back, semanticLabel: 'Back'),
          color: cs.primary,
          onPressed: () {
            context.go('/welcome');
          },
          tooltip: 'Back',
        ),
      ),
      body: SafeArea(
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 420),
            child: Stack(
              children: [
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 24),
                  child: SingleChildScrollView(
                    padding: const EdgeInsets.only(top: 28, bottom: 100),
                    child: Column(
                      children: [
              const SizedBox(height: 12),

                // ===== LOGO PNG ESTÁTICO =====
                Center(
                  child: Image.asset(
                    'assets/images/logo_grande.png', // <- ajusta la ruta
                    height: 148,
                  ),
                ),

                const SizedBox(height: 28),

                // ===== TITULOS (color primario) =====
                Text(
                  'Create an account',
                  textAlign: TextAlign.center,
                  style: tt.titleLarge?.copyWith(
                    fontWeight: FontWeight.w600,
                    color: cs.primary, // primario
                  ),
                ),
                const SizedBox(height: 6),
                Text(
                  'Enter your email to sign up for this app',
                  textAlign: TextAlign.center,
                  style: tt.bodyMedium?.copyWith(color: cs.onSurface.withOpacity(.75)),
                ),

                const SizedBox(height: 26),

                // ===== FORM EMAIL =====
                Form(
                  key: _formKey,
                  child: Column(
                    children: [
                      TextFormField(
                        controller: _emailCtrl,
                        keyboardType: TextInputType.emailAddress,
                        autofillHints: const [AutofillHints.email],
                        autocorrect: false,
                        enableSuggestions: false,
                        style: tt.bodyLarge?.copyWith(
                          fontFamilyFallback: const ['Roboto', 'Arial', 'sans-serif'],
                        ),
                        decoration: InputDecoration(
                          hintText: 'email@domain.com',
                          hintStyle: const TextStyle(
                            fontFamily: 'Roboto',
                            fontWeight: FontWeight.w400,
                            fontSize: 16,
                            color: Colors.grey, // puedes ajustar el color si quieres
                          ),
                        ),
                        validator: _validateEmail,
                      ),
                      const SizedBox(height: 18), // más espacio antes de Continue
                      SizedBox(
                        width: double.infinity,
                        height: 50,
                        child: FilledButton(
                          onPressed: _submitting ? null : _onEmailContinue,
                          // usa FilledButtonTheme (primary) del theme
                          child: _submitting
                              ? const SizedBox(
                                  width: 22, height: 22,
                                  child: CircularProgressIndicator(strokeWidth: 2),
                                )
                              : const Text('Continue'),
                        ),
                      ),
                    ],
                  ),
                ),

                const SizedBox(height: 28), // más espacio entre Continue y "or"

                // ===== "or" CON LÍNEAS =====
                Row(
                  children: [
                    Expanded(
                      child: Divider(
                        color: cs.onSurface.withOpacity(0.2),
                        thickness: 1,
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 16),
                      child: Text(
                        'or',
                        style: tt.bodySmall?.copyWith(color: cs.onSurface.withOpacity(.7)),
                      ),
                    ),
                    Expanded(
                      child: Divider(
                        color: cs.onSurface.withOpacity(0.2),
                        thickness: 1,
                      ),
                    ),
                  ],
                ),

                const SizedBox(height: 20), // más espacio antes de sociales

                // ===== SOCIAL BUTTONS (tertiary, sin bordes negros) =====
                _SocialFilledButton(
                  label: 'Continue with Google',
                  imageAsset: 'assets/icons/G_googleIcon.png',
                  background: cs.tertiary,
                  foreground: cs.onTertiary,
                  isGoogle: true,
                  onTap: _submitting
                      ? null
                      : () async {
                          setState(() => _submitting = true);
                          try {
                            await Future<void>.delayed(const Duration(milliseconds: 400));
                          } finally {
                            if (mounted) setState(() => _submitting = false);
                          }
                        },
                ),
                const SizedBox(height: 12),
                _SocialFilledButton(
                  label: 'Continue with Apple',
                  icon: Icons.apple,
                  background: cs.tertiary,
                  foreground: cs.onTertiary,
                  onTap: _submitting
                      ? null
                      : () async {
                          setState(() => _submitting = true);
                          try {
                            await Future<void>.delayed(const Duration(milliseconds: 400));
                          } finally {
                            if (mounted) setState(() => _submitting = false);
                          }
                        },
                ),

                const SizedBox(height: 24),

                // ===== LEGAL =====
                Text.rich(
                  TextSpan(
                    style: tt.bodySmall?.copyWith(color: cs.onSurface.withOpacity(.75)),
                    children: [
                      const TextSpan(text: 'By clicking continue, you agree to our '),
                      WidgetSpan(
                        baseline: TextBaseline.alphabetic,
                        alignment: PlaceholderAlignment.baseline,
                        child: InkWell(
                          onTap: () => context.push('/terms'),
                          child: Text(
                            'Terms of Service',
                            style: tt.bodySmall?.copyWith(
                              color: cs.primary,
                              decoration: TextDecoration.underline,
                            ),
                          ),
                        ),
                      ),
                      const TextSpan(text: ' and '),
                      WidgetSpan(
                        baseline: TextBaseline.alphabetic,
                        alignment: PlaceholderAlignment.baseline,
                        child: InkWell(
                          onTap: () => context.push('/privacy'),
                          child: Text(
                            'Privacy Policy',
                            style: tt.bodySmall?.copyWith(
                              color: cs.primary,
                              decoration: TextDecoration.underline,
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                  textAlign: TextAlign.center,
                ),

                const SizedBox(height: 18),

                // Padding extra al final para el espacio del footer
                const SizedBox(height: 80),
              ],
            ),
          ),
        ),
        // Footer posicionado en la parte inferior
        Positioned(
          left: 0,
          right: 0,
          bottom: 0,
          child: Container(
            color: cs.surface,
            padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Expanded(
                  child: ShaderMask(
                    shaderCallback: (bounds) {
                      return LinearGradient(
                        colors: [
                          cs.tertiary,
                          cs.secondary,
                          cs.primary,
                        ],
                      ).createShader(
                        Rect.fromLTWH(0, 0, bounds.width, bounds.height),
                      );
                    },
                    child: Text(
                      'Progresso',
                      textAlign: TextAlign.center,
                      style: tt.labelLarge?.copyWith(
                        color: Colors.white, // Necesario para el gradiente
                        letterSpacing: 0.4,
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ]),
    ),
  ),
),
);
  }
}

// ===== Botón social con fondo tertiary y sin borde =====
class _SocialFilledButton extends StatelessWidget {
  const _SocialFilledButton({
    required this.label,
    this.icon,
    this.imageAsset,
    required this.background,
    required this.foreground,
    this.onTap,
    this.isGoogle = false,
  });

  final String label;
  final IconData? icon;
  final String? imageAsset;
  final Color background;
  final Color foreground;
  final VoidCallback? onTap;
  final bool isGoogle;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 56,
      width: double.infinity,
      child: FilledButton(
        onPressed: onTap,
        style: FilledButton.styleFrom(
          backgroundColor: background,
          foregroundColor: foreground,
          elevation: 0,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(14),
          ),
          padding: const EdgeInsets.symmetric(horizontal: 12),
        ),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          mainAxisSize: MainAxisSize.min,
          children: [
            if (imageAsset != null)
              Padding(
                padding: const EdgeInsets.only(right: 12),
                child: Image.asset(
                  imageAsset!,
                  height: 32,
                  width: 32,
                  fit: BoxFit.contain,
                ),
              )
            else if (icon != null)
              Padding(
                padding: const EdgeInsets.only(right: 12),
                child: Icon(icon, size: 32),
              ),
            Flexible(
              child: Text(
                label,
                textAlign: TextAlign.center,
                style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                  fontWeight: isGoogle ? FontWeight.w700 : FontWeight.w500,
                  fontFamilyFallback: const ['Roboto', 'Arial', 'sans-serif'],
                  color: foreground,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
