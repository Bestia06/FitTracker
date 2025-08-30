import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class WelcomePage extends StatefulWidget {
  const WelcomePage({super.key});

  @override
  State<WelcomePage> createState() => _WelcomePageState();
}

class _WelcomePageState extends State<WelcomePage>
    with TickerProviderStateMixin {
  late AnimationController _fadeController;
  late AnimationController _slideController;
  late AnimationController _logoController;
  late AnimationController _buttonsController;

  late Animation<double> _fadeAnimation;
  late Animation<Offset> _slideAnimation;
  late Animation<double> _logoFadeAnimation;
  late Animation<double> _logoScaleAnimation;
  late Animation<double> _buttonsAnimation;

  @override
  void initState() {
    super.initState();
    
    _fadeController = AnimationController(
      duration: const Duration(milliseconds: 800),
      vsync: this,
    );
    
    _slideController = AnimationController(
      duration: const Duration(milliseconds: 1000),
      vsync: this,
    );
    
    _logoController = AnimationController(
      duration: const Duration(milliseconds: 1200),
      vsync: this,
    );
    
    _buttonsController = AnimationController(
      duration: const Duration(milliseconds: 600),
      vsync: this,
    );

    _fadeAnimation = Tween<double>(
      begin: 0.0,
      end: 1.0,
    ).animate(CurvedAnimation(
      parent: _fadeController,
      curve: Curves.easeInOut,
    ));

    _slideAnimation = Tween<Offset>(
      begin: const Offset(0, 0.3),
      end: Offset.zero,
    ).animate(CurvedAnimation(
      parent: _slideController,
      curve: Curves.easeOutCubic,
    ));

    _logoFadeAnimation = Tween<double>(
      begin: 0.0,
      end: 1.0,
    ).animate(CurvedAnimation(
      parent: _logoController,
      curve: const Interval(0.0, 0.6, curve: Curves.easeOut),
    ));

    _logoScaleAnimation = Tween<double>(
      begin: 0.8,
      end: 1.0,
    ).animate(CurvedAnimation(
      parent: _logoController,
      curve: const Interval(0.0, 0.8, curve: Curves.elasticOut),
    ));

    _buttonsAnimation = Tween<double>(
      begin: 0.0,
      end: 1.0,
    ).animate(CurvedAnimation(
      parent: _buttonsController,
      curve: Curves.easeOutBack,
    ));

    _startAnimations();
  }

  void _startAnimations() async {
    _logoController.forward();
    await Future.delayed(const Duration(milliseconds: 400));
    _slideController.forward();
    await Future.delayed(const Duration(milliseconds: 300));
    _fadeController.forward();
    await Future.delayed(const Duration(milliseconds: 500));
    _buttonsController.forward();
  }

  @override
  void dispose() {
    _fadeController.dispose();
    _slideController.dispose();
    _logoController.dispose();
    _buttonsController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;
    final isWeb = size.width > 600;

    return Scaffold(
      backgroundColor: const Color(0xFFF8F9FA),
      body: AnimatedBuilder(
        animation: Listenable.merge([
          _fadeController,
          _slideController,
          _logoController,
          _buttonsController,
        ]),
        builder: (context, child) {
          return SafeArea(
            child: Padding(
              padding: EdgeInsets.symmetric(horizontal: isWeb ? 40 : 24),
              child: Column(
                children: [
                  const Spacer(flex: 2),

                  // Logo with animations
                  FadeTransition(
                    opacity: _logoFadeAnimation,
                    child: ScaleTransition(
                      scale: _logoScaleAnimation,
                      child: SizedBox(
                        width: isWeb ? 140 : 120,
                        height: isWeb ? 140 : 120,
                        child: Stack(
                          alignment: Alignment.center,
                          children: [
                            Container(
                              width: double.infinity,
                              height: double.infinity,
                              decoration: BoxDecoration(
                                shape: BoxShape.circle,
                                color: Colors.white,
                                boxShadow: [
                                  BoxShadow(
                                    color: Colors.black.withOpacity(0.1),
                                    blurRadius: 20,
                                    offset: const Offset(0, 10),
                                  ),
                                ],
                              ),
                            ),
                            CustomPaint(
                              size: Size(isWeb ? 80 : 70, isWeb ? 80 : 70),
                              painter: ProgressoLogoPainter(),
                            ),
                          ],
                        ),
                      ),
                    ),
                  ),

                  const SizedBox(height: 20),

                  // Brand name with gradient and animation
                  SlideTransition(
                    position: _slideAnimation,
                    child: FadeTransition(
                      opacity: _fadeAnimation,
                      child: ShaderMask(
                        shaderCallback: (bounds) => LinearGradient(
                          colors: [
                            const Color(0xFF87CEEB), // Light blue
                            const Color(0xFF4682B4), // Steel blue
                            const Color(0xFF1E3A8A), // Dark blue
                          ],
                        ).createShader(bounds),
                        child: Text(
                          'Progresso',
                          style: TextStyle(
                            fontFamily: 'TheSeasons',
                            fontWeight: FontWeight.w400,
                            fontSize: isWeb ? 36 : 32,
                            height: 1.1,
                            color: Colors.white,
                            letterSpacing: 1.2,
                          ),
                        ),
                      ),
                    ),
                  ),

                  const Spacer(flex: 3),

                  // Buttons with animation
                  ScaleTransition(
                    scale: _buttonsAnimation,
                    child: FadeTransition(
                      opacity: _buttonsAnimation,
                      child: Row(
                        children: [
                          // Log In button (outlined)
                          Expanded(
                            child: Container(
                              height: isWeb ? 56 : 52,
                              decoration: BoxDecoration(
                                borderRadius: BorderRadius.circular(12),
                                border: Border.all(
                                  color: const Color(0xFF3B82F6),
                                  width: 1.5,
                                ),
                              ),
                              child: Material(
                                color: Colors.transparent,
                                child: InkWell(
                                  onTap: () => context.go('/login'),
                                  borderRadius: BorderRadius.circular(12),
                                  child: Container(
                                    alignment: Alignment.center,
                                    child: Text(
                                      'Log In',
                                      style: TextStyle(
                                        color: const Color(0xFF3B82F6),
                                        fontSize: isWeb ? 16 : 15,
                                        fontWeight: FontWeight.w600,
                                        letterSpacing: 0.5,
                                      ),
                                    ),
                                  ),
                                ),
                              ),
                            ),
                          ),
                          
                          const SizedBox(width: 16),
                          
                          // Sign up button (filled)
                          Expanded(
                            child: Container(
                              height: isWeb ? 56 : 52,
                              decoration: BoxDecoration(
                                gradient: const LinearGradient(
                                  colors: [
                                    Color(0xFF1E40AF),
                                    Color(0xFF3B82F6),
                                  ],
                                  begin: Alignment.topLeft,
                                  end: Alignment.bottomRight,
                                ),
                                borderRadius: BorderRadius.circular(12),
                                boxShadow: [
                                  BoxShadow(
                                    color: const Color(0xFF3B82F6).withOpacity(0.3),
                                    blurRadius: 12,
                                    offset: const Offset(0, 4),
                                  ),
                                ],
                              ),
                              child: Material(
                                color: Colors.transparent,
                                child: InkWell(
                                  onTap: () => context.go('/register'),
                                  borderRadius: BorderRadius.circular(12),
                                  child: Container(
                                    alignment: Alignment.center,
                                    child: Text(
                                      'Sign up',
                                      style: TextStyle(
                                        color: Colors.white,
                                        fontSize: isWeb ? 16 : 15,
                                        fontWeight: FontWeight.w600,
                                        letterSpacing: 0.5,
                                      ),
                                    ),
                                  ),
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),

                  const SizedBox(height: 24),
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}

class ProgressoLogoPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    final paint1 = Paint()
      ..color = const Color(0xFF87CEEB)
      ..style = PaintingStyle.fill;
    
    final paint2 = Paint()
      ..color = const Color(0xFF4682B4)
      ..style = PaintingStyle.fill;
    
    final paint3 = Paint()
      ..color = const Color(0xFF1E3A8A)
      ..style = PaintingStyle.fill;

    final center = Offset(size.width / 2, size.height / 2);
    final leafSize = size.width * 0.25;

    // First leaf (top-right, light blue)
    final path1 = Path();
    path1.moveTo(center.dx, center.dy - leafSize * 0.5);
    path1.quadraticBezierTo(
      center.dx + leafSize * 1.2, center.dy - leafSize * 0.8,
      center.dx + leafSize * 0.8, center.dy + leafSize * 0.2,
    );
    path1.quadraticBezierTo(
      center.dx + leafSize * 0.3, center.dy + leafSize * 0.1,
      center.dx, center.dy - leafSize * 0.5,
    );
    canvas.drawPath(path1, paint1);

    // Second leaf (left, steel blue)
    final path2 = Path();
    path2.moveTo(center.dx - leafSize * 0.2, center.dy - leafSize * 0.3);
    path2.quadraticBezierTo(
      center.dx - leafSize * 1.3, center.dy - leafSize * 0.2,
      center.dx - leafSize * 1.1, center.dy + leafSize * 0.8,
    );
    path2.quadraticBezierTo(
      center.dx - leafSize * 0.4, center.dy + leafSize * 0.4,
      center.dx - leafSize * 0.2, center.dy - leafSize * 0.3,
    );
    canvas.drawPath(path2, paint2);

    // Third leaf (bottom-right, dark blue)
    final path3 = Path();
    path3.moveTo(center.dx + leafSize * 0.2, center.dy + leafSize * 0.1);
    path3.quadraticBezierTo(
      center.dx + leafSize * 1.1, center.dy + leafSize * 0.5,
      center.dx + leafSize * 0.6, center.dy + leafSize * 1.3,
    );
    path3.quadraticBezierTo(
      center.dx + leafSize * 0.1, center.dy + leafSize * 0.8,
      center.dx + leafSize * 0.2, center.dy + leafSize * 0.1,
    );
    canvas.drawPath(path3, paint3);
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}
