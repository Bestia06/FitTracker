import 'dart:math' as math;
import 'package:flutter/material.dart';

class ProgressoLogoCircularFade extends StatefulWidget {
  const ProgressoLogoCircularFade({
    super.key,
    this.size = 160,
    this.period = const Duration(milliseconds: 2400),
    this.repeat = true, // true = loop, false = una sola vez
    this.onCompleted,
  });

  final double size;
  final Duration period;
  final bool repeat;
  final VoidCallback? onCompleted;

  @override
  State<ProgressoLogoCircularFade> createState() => _ProgressoLogoCircularFadeState();
}

class _ProgressoLogoCircularFadeState extends State<ProgressoLogoCircularFade>
    with SingleTickerProviderStateMixin {
  late final AnimationController _c;

  @override
  void initState() {
    super.initState();
    _c = AnimationController(vsync: this, duration: widget.period);
    if (widget.repeat) {
      _c.repeat(period: widget.period);
    } else {
      _c.forward();
      _c.addStatusListener((st) {
        if (st == AnimationStatus.completed) widget.onCompleted?.call();
      });
    }
  }

  @override
  void dispose() {
    _c.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final cs = Theme.of(context).colorScheme;
    return AnimatedBuilder(
      animation: _c,
      builder: (_, __) => CustomPaint(
        size: Size.square(widget.size),
        painter: _CircularFadePainter(
          t: _c.value, // 0..1
          base: cs.primary,
          accent: cs.secondary,
        ),
      ),
    );
  }
}

class _CircularFadePainter extends CustomPainter {
  _CircularFadePainter({required this.t, required this.base, required this.accent});
  final double t;
  final Color base;
  final Color accent;

  @override
  void paint(Canvas canvas, Size size) {
    final stroke = size.width * 0.095;
    final r = (size.width - stroke) / 2;
    final center = size.center(Offset.zero);

    final bg = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = stroke
      ..color = base.withOpacity(0.10)
      ..strokeCap = StrokeCap.round;

    final fg = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = stroke
      ..strokeCap = StrokeCap.round;

    // Anillo de fondo
    canvas.drawCircle(center, r, bg);

    // 4 segmentos que “aparecen” con un desfasaje suave
    // Cada segmento tiene una ventana de 0.35 del ciclo con easing.
    final segs = 4;
    final sweep = math.pi * 0.55; // tamaño del arco
    for (int i = 0; i < segs; i++) {
      final startBase = (i / segs);            // fase base
      final local = ((t - startBase) % 1 + 1) % 1; // 0..1 ciclo local

      // ventana de visibilidad
      double vis = 0.0;
      if (local < 0.35) {
        // ease-in/out simple
        final u = local / 0.35;
        vis = (1 - math.cos(u * math.pi)) / 2; // 0→1→(suave)
      }

      if (vis <= 0) continue;

      fg.color = Color.lerp(base, accent, 0.35 + 0.65 * vis)!.withOpacity(0.25 + 0.75 * vis);

      final startAngle = (i * (2 * math.pi / segs)) + (t * 2 * math.pi * 0.7);
      canvas.drawArc(
        Rect.fromCircle(center: center, radius: r),
        startAngle,
        sweep * vis,
        false,
        fg,
      );
    }

    // Marca central (puedes cambiar por tu isotipo si tienes uno)
    final dot = Paint()..color = accent.withOpacity(0.9);
    canvas.drawCircle(center, stroke * 0.22, dot);
  }

  @override
  bool shouldRepaint(covariant _CircularFadePainter oldDelegate) {
    return oldDelegate.t != t || oldDelegate.base != base || oldDelegate.accent != accent;
  }
}
