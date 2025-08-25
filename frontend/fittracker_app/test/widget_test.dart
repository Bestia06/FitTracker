import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:fittracker_app/app/app.dart';

void main() {
  testWidgets('App loads without errors', (WidgetTester tester) async {
    // Construye la app base
    await tester.pumpWidget(const FitTrackerApp());

    // Verifica que se muestre el login (o el dashboard según config inicial)
    expect(find.byType(MaterialApp), findsOneWidget);
  });
}
