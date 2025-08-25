# FitTracker Mobile App

A beautiful and modern fitness tracking mobile application built with Flutter.

## 🚀 Features

### ✅ Implemented
- **Authentication**: Login and registration screens with beautiful UI
- **Dashboard**: Overview of progress with interactive cards and statistics
- **Habits Tracking**: Complete habit management with progress tracking
- **Navigation**: Bottom navigation with smooth transitions
- **Theme**: Modern Material Design 3 with custom colors and gradients
- **State Management**: Riverpod for efficient state management

### 🚧 In Development
- **Workouts**: Exercise tracking and workout logging
- **Nutrition**: Food tracking and calorie counting
- **Statistics**: Detailed analytics and progress charts
- **API Integration**: Backend connectivity with Django REST API

## 📱 Screenshots

### Authentication
- Beautiful gradient backgrounds
- Form validation
- Demo credentials for testing

### Dashboard
- Progress overview cards
- Quick action buttons
- Recent activity feed
- Daily statistics

### Habits
- Interactive habit cards
- Progress tracking
- Add new habits dialog
- Category-based organization

## 🛠️ Technology Stack

- **Framework**: Flutter 3.0+
- **Language**: Dart
- **State Management**: Riverpod
- **Navigation**: GoRouter
- **UI**: Material Design 3
- **HTTP Client**: Dio
- **Storage**: SharedPreferences, SecureStorage

## 🎨 Design System

### Colors
- **Primary**: Blue (#2563EB)
- **Secondary**: Green (#10B981)
- **Accent**: Orange (#F59E0B)
- **Error**: Red (#EF4444)
- **Success**: Green (#22C55E)

### Typography
- **Font Family**: Inter (Google Fonts)
- **Weights**: Light, Regular, Medium, SemiBold, Bold

### Components
- Custom gradient buttons
- Progress cards
- Interactive habit cards
- Modern form inputs
- Animated splash screen

## 📁 Project Structure

```
lib/
├── app/
│   └── app.dart                 # App router and navigation
├── core/
│   ├── providers/
│   │   └── providers.dart       # State management providers
│   └── theme/
│       └── app_theme.dart       # Theme configuration
├── features/
│   ├── auth/
│   │   └── presentation/
│   │       ├── screens/
│   │       │   ├── login_screen.dart
│   │       │   └── register_screen.dart
│   │       └── widgets/
│   │           ├── auth_text_field.dart
│   │           └── gradient_button.dart
│   ├── dashboard/
│   │   └── presentation/
│   │       ├── screens/
│   │       │   └── dashboard_screen.dart
│   │       └── widgets/
│   │           ├── progress_card.dart
│   │           ├── quick_action_card.dart
│   │           └── stats_card.dart
│   ├── habits/
│   │   └── presentation/
│   │       ├── screens/
│   │       │   └── habits_screen.dart
│   │       └── widgets/
│   │           ├── habit_card.dart
│   │           └── add_habit_dialog.dart
│   ├── workouts/
│   │   └── presentation/
│   │       └── screens/
│   │           └── workouts_screen.dart
│   ├── nutrition/
│   │   └── presentation/
│   │       └── screens/
│   │           └── nutrition_screen.dart
│   └── profile/
│       └── presentation/
│           └── screens/
│               └── profile_screen.dart
├── shared/
│   └── widgets/
│       └── splash_screen.dart   # App splash screen
└── main.dart                    # App entry point
```

## 🚀 Getting Started

### Prerequisites
- Flutter SDK 3.0+
- Dart SDK
- Android Studio / VS Code
- Android Emulator or Physical Device

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd frontend/fittracker_app
   ```

2. **Install dependencies**
   ```bash
   flutter pub get
   ```

3. **Run the app**
   ```bash
   flutter run
   ```

### Development

1. **Hot Reload**
   ```bash
   flutter run --hot
   ```

2. **Build for different platforms**
   ```bash
   # Android APK
   flutter build apk
   
   # iOS
   flutter build ios
   
   # Web
   flutter build web
   ```

## 🔧 Configuration

### API Configuration
Update the API base URL in `lib/core/providers/providers.dart`:

```dart
final apiBaseUrlProvider = Provider<String>((ref) {
  // For Android emulator
  return 'http://10.0.2.2:8000/api';
  
  // For iOS simulator
  // return 'http://localhost:8000/api';
  
  // For production
  // return 'https://your-api-domain.com/api';
});
```

### Theme Configuration
Customize colors and styles in `lib/core/theme/app_theme.dart`.

## 📊 Demo Credentials

For testing purposes, you can use:
- **Email**: demo@fittracker.com
- **Password**: 123456

## 🔗 Backend Integration

The app is designed to work with the Django REST API backend. Key endpoints:

- **Authentication**: `/api/auth/`
- **Habits**: `/api/habits/`
- **Workouts**: `/api/workouts/`
- **Nutrition**: `/api/nutrition/`
- **Statistics**: `/api/stats/`

## 🎯 Roadmap

### Phase 1 (Current)
- ✅ Authentication UI
- ✅ Dashboard with mock data
- ✅ Habits tracking
- ✅ Basic navigation

### Phase 2 (Next)
- 🔄 API integration
- 🔄 Real data persistence
- 🔄 Workout tracking
- 🔄 Nutrition tracking

### Phase 3 (Future)
- 📊 Advanced analytics
- 📈 Progress charts
- 🔔 Push notifications
- 🌐 Social features

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

---

**FitTracker Mobile** - Your fitness journey starts here! 💪📱
