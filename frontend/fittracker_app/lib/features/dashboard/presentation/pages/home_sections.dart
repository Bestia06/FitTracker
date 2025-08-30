import 'package:flutter/material.dart';

class HabitTrackerSection extends StatefulWidget {
  const HabitTrackerSection({super.key});

  @override
  State<HabitTrackerSection> createState() => _HabitTrackerSectionState();
}

class _HabitTrackerSectionState extends State<HabitTrackerSection> {
  final List<bool> _checked = [false, false, false];

  @override
  Widget build(BuildContext context) {
    final cs = Theme.of(context).colorScheme;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
        Padding(
          padding: const EdgeInsets.only(top: 8, bottom: 0),
          child: Text(
            'Habit tracker',
            style: TextStyle(
              color: cs.primary,
              fontSize: 38,
              fontWeight: FontWeight.w400,
              fontFamily: 'TheSeasons',
              letterSpacing: 1.1,
              height: 1.1,
              shadows: [
                Shadow(
                  color: cs.primary.withOpacity(0.13),
                  blurRadius: 8,
                  offset: const Offset(0, 2),
                ),
              ],
            ),
            textAlign: TextAlign.center,
          ),
        ),
        Container(
          margin: const EdgeInsets.only(top: 0, bottom: 0, left: 12, right: 12),
          padding: const EdgeInsets.fromLTRB(16, 8, 16, 16),
          decoration: BoxDecoration(
            color: cs.primary.withOpacity(0.07),
            borderRadius: BorderRadius.circular(32),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              _HabitRow(
                label: '6-8 hours of sleep',
                icon: Icons.bedtime,
                checked: _checked[0],
                onChanged: (val) => setState(() => _checked[0] = val ?? false),
              ),
              _HabitRow(
                label: 'Weightlifting',
                icon: Icons.fitness_center,
                checked: _checked[1],
                onChanged: (val) => setState(() => _checked[1] = val ?? false),
              ),
              _HabitRow(
                label: '8-10k steps a day',
                icon: Icons.directions_walk,
                checked: _checked[2],
                onChanged: (val) => setState(() => _checked[2] = val ?? false),
              ),
            ],
          ),
        ),
      ],
    );
  }
}

class _HabitRow extends StatelessWidget {
  final String label;
  final IconData icon;
  final bool checked;
  final ValueChanged<bool?>? onChanged;
  const _HabitRow(
      {required this.label,
      required this.icon,
      required this.checked,
      this.onChanged});

  @override
  Widget build(BuildContext context) {
    final cs = Theme.of(context).colorScheme;
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4.0, horizontal: 0),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Transform.scale(
            scale: 1.5, // 50% más grande
            child: Theme(
              data: Theme.of(context).copyWith(
                unselectedWidgetColor: cs.primary,
                checkboxTheme: CheckboxThemeData(
                  shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(6)),
                  side: BorderSide(color: cs.primary, width: 2),
                  fillColor: WidgetStateProperty.resolveWith<Color>(
                      (states) => Colors.transparent),
                  checkColor: WidgetStateProperty.all(Colors.green),
                  overlayColor:
                      WidgetStateProperty.all(cs.primary.withOpacity(0.08)),
                  splashRadius: 27,
                ),
              ),
              child: Checkbox(
                value: checked,
                onChanged: onChanged,
                activeColor: Colors.transparent,
                checkColor: Colors.green,
                side: BorderSide(color: cs.primary, width: 2),
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(6)),
                materialTapTargetSize: MaterialTapTargetSize.shrinkWrap,
                visualDensity: VisualDensity.compact,
              ),
            ),
          ),
          const SizedBox(width: 8),
          Expanded(
            child: Text(
              label,
              style: const TextStyle(
                fontWeight: FontWeight.w400,
                fontSize: 15,
                fontFamily: 'Roboto',
                letterSpacing: 0.1,
              ),
              textAlign: TextAlign.center,
            ),
          ),
          const SizedBox(width: 8),
          Icon(icon, color: cs.primary, size: 28),
        ],
      ),
    );
  }
}

class ProgressSection extends StatelessWidget {
  const ProgressSection({super.key});

  @override
  Widget build(BuildContext context) {
    final cs = Theme.of(context).colorScheme;
    final tt = Theme.of(context).textTheme;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
        Padding(
          padding: const EdgeInsets.only(top: 8.0, bottom: 12.0),
          child: Text('Progress',
              style: tt.titleMedium
                  ?.copyWith(fontWeight: FontWeight.bold, color: cs.primary)),
        ),
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            _ProgressCircle(label: 'Calories', percent: 0.7, color: cs.primary),
            _ProgressCircle(label: 'Steps', percent: 0.5, color: cs.secondary),
            _ProgressCircle(label: 'Sleep', percent: 0.9, color: cs.tertiary),
            _ProgressCircle(label: 'Water', percent: 0.6, color: cs.primary),
          ],
        ),
      ],
    );
  }
}

class _ProgressCircle extends StatelessWidget {
  final String label;
  final double percent;
  final Color color;
  const _ProgressCircle(
      {required this.label, required this.percent, required this.color});

  @override
  Widget build(BuildContext context) {
    final tt = Theme.of(context).textTheme;
    return Column(
      children: [
        Stack(
          alignment: Alignment.center,
          children: [
            SizedBox(
              width: 56,
              height: 56,
              child: CircularProgressIndicator(
                value: percent,
                strokeWidth: 6,
                backgroundColor: color.withOpacity(0.15),
                valueColor: AlwaysStoppedAnimation<Color>(color),
              ),
            ),
            Text('${(percent * 100).toInt()}%', style: tt.bodySmall),
          ],
        ),
        const SizedBox(height: 6),
        Text(label, style: tt.bodySmall),
      ],
    );
  }
}

class WorkoutsSection extends StatelessWidget {
  const WorkoutsSection({super.key});

  @override
  Widget build(BuildContext context) {
    final cs = Theme.of(context).colorScheme;
    final tt = Theme.of(context).textTheme;
    return Container(
      margin: const EdgeInsets.symmetric(vertical: 16, horizontal: 24),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: cs.primary.withOpacity(0.08),
        borderRadius: BorderRadius.circular(18),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text('Workouts',
                  style: tt.titleMedium?.copyWith(
                      fontWeight: FontWeight.bold, color: cs.primary)),
              ElevatedButton(
                onPressed: () {},
                style: ElevatedButton.styleFrom(
                  backgroundColor: cs.primary,
                  foregroundColor: Colors.white,
                  shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(12)),
                  padding:
                      const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                ),
                child: const Text('Add new'),
              ),
            ],
          ),
          const SizedBox(height: 12),
          ...List.generate(3, (i) => _WorkoutItem(title: 'Workout ${i + 1}')),
        ],
      ),
    );
  }
}

class _WorkoutItem extends StatelessWidget {
  final String title;
  const _WorkoutItem({required this.title});

  @override
  Widget build(BuildContext context) {
    final cs = Theme.of(context).colorScheme;
    final tt = Theme.of(context).textTheme;
    return Container(
      margin: const EdgeInsets.only(bottom: 8),
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: cs.surface,
        borderRadius: BorderRadius.circular(12),
        boxShadow: [
          BoxShadow(
            color: cs.primary.withOpacity(0.06),
            blurRadius: 4,
            offset: const Offset(0, 2),
          ),
        ],
      ),
      child: Text(title, style: tt.bodyMedium?.copyWith(color: cs.primary)),
    );
  }
}
