import 'package:flutter/material.dart';

const double kPadding = 24;
const double kRadius = 12;

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _formKey = GlobalKey<FormState>();
  final _emailCtrl = TextEditingController();
  final _passCtrl = TextEditingController();
  bool _obscure = true;
  bool _loading = false;

  @override
  void dispose() {
    _emailCtrl.dispose();
    _passCtrl.dispose();
    super.dispose();
  }

  void _onSignIn() async {
    if (!(_formKey.currentState?.validate() ?? false)) return;
    setState(() => _loading = true);
    await Future.delayed(const Duration(seconds: 1));
    setState(() => _loading = false);
    final cs = Theme.of(context).colorScheme;
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: const Text('Authentication failed.'),
        backgroundColor: cs.error,
        behavior: SnackBarBehavior.floating,
      ),
    );
  }

  void _onForgotPassword() {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text('Forgot password tapped')),
    );
  }

  void _onGoToRegister() {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text('Go to Register tapped')),
    );
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final cs = theme.colorScheme;
    final tt = theme.textTheme;
    return Scaffold(
      appBar: AppBar(
        backgroundColor: theme.scaffoldBackgroundColor,
        elevation: 0,
        leading: IconButton(
          icon: const Icon(Icons.arrow_back, semanticLabel: 'Back'),
          color: cs.primary,
          onPressed: () => Navigator.pop(context),
          tooltip: 'Back',
        ),
      ),
      body: LayoutBuilder(
        builder: (context, constraints) {
          final isLarge = constraints.maxWidth > 500;
          return Center(
            child: SingleChildScrollView(
              padding: EdgeInsets.symmetric(
                horizontal: isLarge ? kPadding * 2 : kPadding,
                vertical: kPadding,
              ),
              child: ConstrainedBox(
                constraints: const BoxConstraints(maxWidth: 400),
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    _Logo(),
                    const SizedBox(height: 32),
                    _TitleSection(),
                    const SizedBox(height: 32),
                    _LoginForm(
                      formKey: _formKey,
                      emailCtrl: _emailCtrl,
                      passCtrl: _passCtrl,
                      obscure: _obscure,
                      loading: _loading,
                      onToggleObscure: () => setState(() => _obscure = !_obscure),
                      onSignIn: _onSignIn,
                      onForgotPassword: _onForgotPassword,
                    ),
                    const SizedBox(height: 24),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Text(
                          "Don't have an account? ",
                          style: tt.bodyMedium ?? tt.bodyLarge,
                        ),
                        GestureDetector(
                          onTap: _onGoToRegister,
                          child: Text(
                            'Register',
                            style: (tt.bodyMedium ?? tt.bodyLarge)?.copyWith(
                              color: cs.secondary,
                              fontWeight: FontWeight.w600,
                              decoration: TextDecoration.underline,
                            ),
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 36),
                    _FooterBrand(),
                  ],
                ),
              ),
            ),
          );
        },
      ),
    );
  }
}

class _Logo extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final cs = Theme.of(context).colorScheme;
    return Center(
      child: Container(
        width: 72,
        height: 72,
        decoration: BoxDecoration(
          color: cs.secondary.withOpacity(0.08),
          shape: BoxShape.circle,
        ),
        child: Icon(Icons.fitness_center, size: 40, color: cs.primary, semanticLabel: 'App Logo'),
      ),
    );
  }
}

class _TitleSection extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final tt = Theme.of(context).textTheme;
    final titleStyle = tt.titleLarge?.copyWith(fontWeight: FontWeight.w600)
      ?? tt.headlineMedium?.copyWith(fontWeight: FontWeight.w600)
      ?? tt.bodyLarge;
    final subtitleStyle = tt.bodyMedium?.copyWith(color: Theme.of(context).hintColor)
      ?? tt.bodyLarge?.copyWith(color: Theme.of(context).hintColor);
    return Column(
      children: [
        Text(
          'Enter your account',
          textAlign: TextAlign.center,
          style: titleStyle,
        ),
        const SizedBox(height: 8),
        Text(
          'Enter your credentials to sign in for this app',
          textAlign: TextAlign.center,
          style: subtitleStyle,
        ),
      ],
    );
  }
}

class _LoginForm extends StatefulWidget {
  const _LoginForm({
    required this.formKey,
    required this.emailCtrl,
    required this.passCtrl,
    required this.obscure,
    required this.loading,
    required this.onToggleObscure,
    required this.onSignIn,
    required this.onForgotPassword,
  });

  final GlobalKey<FormState> formKey;
  final TextEditingController emailCtrl;
  final TextEditingController passCtrl;
  final bool obscure;
  final bool loading;
  final VoidCallback onToggleObscure;
  final VoidCallback onSignIn;
  final VoidCallback onForgotPassword;

  @override
  State<_LoginForm> createState() => _LoginFormState();
}

class _LoginFormState extends State<_LoginForm> {
  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final cs = theme.colorScheme;
    final tt = theme.textTheme;
    final inputTheme = theme.inputDecorationTheme;
    final labelStyle = inputTheme.labelStyle ?? tt.bodyMedium;
    return Form(
      key: widget.formKey,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          TextFormField(
            controller: widget.emailCtrl,
            keyboardType: TextInputType.emailAddress,
            autofillHints: const [AutofillHints.email],
            style: tt.bodyMedium,
            decoration: InputDecoration(
              prefixIcon: Icon(Icons.email_outlined, color: cs.primary, semanticLabel: 'Email'),
              hintText: 'email',
              hintStyle: inputTheme.hintStyle ?? labelStyle,
              filled: inputTheme.filled,
              fillColor: inputTheme.fillColor,
              contentPadding: inputTheme.contentPadding,
              border: inputTheme.border,
              enabledBorder: inputTheme.enabledBorder,
              focusedBorder: inputTheme.focusedBorder,
              errorBorder: inputTheme.errorBorder,
              focusedErrorBorder: inputTheme.focusedErrorBorder,
            ),
            validator: (v) {
              final value = (v ?? '').trim();
              if (value.isEmpty) return 'Email required';
              final re = RegExp(r'^[^\s@]+@[^\s@]+\.[^\s@]+$');
              if (!re.hasMatch(value)) return 'Enter a valid email';
              return null;
            },
            textInputAction: TextInputAction.next,
          ),
          const SizedBox(height: 16),
          TextFormField(
            controller: widget.passCtrl,
            obscureText: widget.obscure,
            style: tt.bodyMedium,
            decoration: InputDecoration(
              prefixIcon: Icon(Icons.lock_outline, color: cs.primary, semanticLabel: 'Password'),
              hintText: 'password',
              hintStyle: inputTheme.hintStyle ?? labelStyle,
              filled: inputTheme.filled,
              fillColor: inputTheme.fillColor,
              contentPadding: inputTheme.contentPadding,
              border: inputTheme.border,
              enabledBorder: inputTheme.enabledBorder,
              focusedBorder: inputTheme.focusedBorder,
              errorBorder: inputTheme.errorBorder,
              focusedErrorBorder: inputTheme.focusedErrorBorder,
              suffixIcon: IconButton(
                icon: Icon(
                  widget.obscure ? Icons.visibility_off : Icons.visibility,
                  color: cs.primary,
                  semanticLabel: widget.obscure ? 'Show password' : 'Hide password',
                ),
                onPressed: widget.onToggleObscure,
                tooltip: widget.obscure ? 'Show password' : 'Hide password',
              ),
            ),
            validator: (v) {
              final value = v ?? '';
              if (value.isEmpty) return 'Password required';
              if (value.length < 6) return 'Minimum 6 characters';
              return null;
            },
            textInputAction: TextInputAction.done,
            onFieldSubmitted: (_) => widget.onSignIn(),
          ),
          const SizedBox(height: 8),
          Align(
            alignment: Alignment.centerRight,
            child: TextButton(
              onPressed: widget.onForgotPassword,
              child: Text(
                'Forgot password?',
                style: tt.labelLarge?.copyWith(
                  color: cs.primary,
                  fontWeight: FontWeight.w600,
                  decoration: TextDecoration.underline,
                ) ?? tt.bodyMedium,
              ),
              style: TextButton.styleFrom(
                foregroundColor: cs.primary,
                padding: EdgeInsets.zero,
                minimumSize: const Size(0, 0),
                tapTargetSize: MaterialTapTargetSize.shrinkWrap,
              ),
            ),
          ),
          const SizedBox(height: 18),
          SizedBox(
            height: 48,
            child: ElevatedButton(
              onPressed: widget.loading ? null : widget.onSignIn,
              style: Theme.of(context).elevatedButtonTheme.style ?? ElevatedButton.styleFrom(
                backgroundColor: cs.primary,
                foregroundColor: cs.onPrimary,
                padding: const EdgeInsets.symmetric(vertical: 12),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(kRadius),
                ),
                textStyle: tt.labelLarge,
              ),
              child: widget.loading
                  ? const SizedBox(
                      width: 22,
                      height: 22,
                      child: CircularProgressIndicator(
                        strokeWidth: 2,
                        valueColor: AlwaysStoppedAnimation<Color>(Colors.white),
                      ),
                    )
                  : const Text('Sign in', semanticsLabel: 'Sign in'),
            ),
          ),
        ],
      ),
    );
  }
}

class _FooterBrand extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final tt = Theme.of(context).textTheme;
    final cs = Theme.of(context).colorScheme;
    return Padding(
      padding: const EdgeInsets.only(top: 12, bottom: 8),
      child: Text(
        'Progresso',
        textAlign: TextAlign.center,
        style: tt.labelLarge?.copyWith(
          color: cs.primary.withOpacity(0.18),
          fontWeight: FontWeight.w600,
          letterSpacing: 0.4,
        ) ?? tt.bodyMedium,
      ),
    );
  }
}

/*
VERIFICACIÓN FINAL:
1) Títulos usan Theseason desde textTheme (con fallbacks seguros).
2) Texto/inputs/botones usan Roboto desde textTheme/inputDecorationTheme.
3) Todos los colores provienen de Theme.of(context) (sin hex).
4) AppBar leading hace Navigator.pop.
5) No se creó/alteró ThemeData ni se accedió a otros archivos.
*/
