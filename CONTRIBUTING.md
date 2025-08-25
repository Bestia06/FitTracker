# 🤝 Contributing to FitTracker

¡Gracias por tu interés en contribuir a FitTracker! Este documento te guiará a través del proceso de contribución.

## 📋 Table of Contents

- [🎯 Getting Started](#-getting-started)
- [🏗️ Project Structure](#️-project-structure)
- [🛠️ Development Setup](#️-development-setup)
- [📝 Code Style Guidelines](#-code-style-guidelines)
- [🚀 Making Changes](#-making-changes)
- [🧪 Testing](#-testing)
- [📤 Submitting Changes](#-submitting-changes)
- [🎨 UI/UX Guidelines](#-uiux-guidelines)
- [🔒 Security Guidelines](#-security-guidelines)
- [📚 Documentation](#-documentation)
- [🐛 Reporting Bugs](#-reporting-bugs)
- [💡 Suggesting Features](#-suggesting-features)
- [❓ Getting Help](#-getting-help)

## 🎯 Getting Started

### Prerequisites

- **Python 3.11+**
- **Flutter 3.0+**
- **Docker & Docker Compose**
- **Git**
- **VS Code** (recommended)

### Quick Start

1. **Fork the repository**
   ```bash
   # Fork on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/fittracker.git
   cd fittracker
   ```

2. **Set up the development environment**
   ```bash
   # Copy environment file
   cp env.example .env
   
   # Start with Docker (recommended)
   docker-compose up -d
   
   # Or set up manually
   # Backend
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements/dev.txt
   python manage.py migrate
   
   # Frontend
   cd frontend/fittracker_app
   flutter pub get
   ```

3. **Install pre-commit hooks**
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## 🏗️ Project Structure

```
FitTracker/
├── 🐍 backend/                 # Django Ninja backend
│   ├── apps/                   # Django applications
│   │   ├── accounts/           # User authentication & profiles
│   │   ├── workouts/           # Workout tracking
│   │   ├── nutrition/          # Nutrition tracking
│   │   ├── stats/              # Statistics & analytics
│   │   └── habits/             # Habit tracking
│   ├── config/                 # Django settings
│   ├── core/                   # Core utilities
│   └── tests/                  # Backend tests
├── 📱 frontend/                # Flutter frontend
│   └── fittracker_app/         # Flutter application
│       ├── lib/
│       │   ├── app/            # App configuration
│       │   ├── features/       # Feature modules
│       │   └── shared/         # Shared components
│       └── test/               # Frontend tests
└── 📚 docs/                    # Documentation
```

## 🛠️ Development Setup

### Backend Development

1. **Virtual Environment**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements/dev.txt
   ```

3. **Database Setup**
   ```bash
   # Using local MySQL (Docker)
   docker-compose up db
   
   # Or configure AWS RDS in .env
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

### Frontend Development

1. **Install Flutter Dependencies**
   ```bash
   cd frontend/fittracker_app
   flutter pub get
   ```

2. **Run Flutter App**
   ```bash
   # Web
   flutter run -d chrome
   
   # Mobile
   flutter run
   ```

### Docker Development

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## 📝 Code Style Guidelines

### Python/Django

- **Formatter**: Black (line length: 88)
- **Import Sorting**: isort
- **Linting**: Flake8
- **Type Checking**: MyPy

```python
# Good example
from django.db import models
from django.contrib.auth.models import AbstractUser

from core.models import BaseModel


class User(AbstractUser, BaseModel):
    """Custom user model for FitTracker."""
    
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    
    class Meta:
        db_table = "users"
    
    def __str__(self) -> str:
        return self.email
```

### Flutter/Dart

- **Formatter**: dart format
- **Analysis**: flutter analyze
- **Line Length**: 80 characters

```dart
// Good example
class UserService {
  final ApiClient _apiClient;
  
  UserService(this._apiClient);
  
  Future<User> getUser(int id) async {
    try {
      final response = await _apiClient.get('/users/$id');
      return User.fromJson(response.data);
    } catch (e) {
      throw UserException('Failed to fetch user: $e');
    }
  }
}
```

### Commit Messages

Use conventional commits:

```bash
# Format: type(scope): description
feat(auth): add JWT authentication
fix(workouts): resolve workout creation bug
docs(readme): update installation instructions
style(ui): improve button styling
refactor(api): simplify user endpoints
test(auth): add authentication tests
```

## 🚀 Making Changes

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 2. Make Your Changes

- Follow the code style guidelines
- Write tests for new functionality
- Update documentation if needed

### 3. Test Your Changes

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend/fittracker_app
flutter test

# Run all tests
docker-compose -f docker-compose.test.yml up
```

### 4. Format and Lint

```bash
# Backend
cd backend
black .
isort .
flake8 .

# Frontend
cd frontend/fittracker_app
dart format .
flutter analyze
```

## 🧪 Testing

### Backend Testing

```python
# Example test
import pytest
from django.test import TestCase
from apps.accounts.models import User


class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(
            email="test@example.com",
            password="testpass123"
        )
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("testpass123"))
```

### Frontend Testing

```dart
// Example test
import 'package:flutter_test/flutter_test.dart';
import 'package:fittracker_app/features/auth/auth_service.dart';

void main() {
  group('AuthService', () {
    test('should login user successfully', () async {
      final authService = AuthService();
      final result = await authService.login('test@example.com', 'password');
      expect(result.isSuccess, true);
    });
  });
}
```

## 📤 Submitting Changes

### 1. Push Your Changes

```bash
git add .
git commit -m "feat: add new feature"
git push origin feature/your-feature-name
```

### 2. Create a Pull Request

1. Go to the GitHub repository
2. Click "New Pull Request"
3. Select your feature branch
4. Fill out the PR template
5. Request review from code owners

### 3. PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Backend tests pass
- [ ] Frontend tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes
```

## 🎨 UI/UX Guidelines

### Design Principles

- **Consistency**: Use the same patterns throughout the app
- **Accessibility**: Follow WCAG 2.1 guidelines
- **Responsive**: Support multiple screen sizes
- **Performance**: Optimize for speed and efficiency

### Flutter UI Guidelines

```dart
// Use consistent theming
class AppTheme {
  static const primaryColor = Color(0xFF2196F3);
  static const secondaryColor = Color(0xFF4CAF50);
  
  static ThemeData get lightTheme {
    return ThemeData(
      primaryColor: primaryColor,
      colorScheme: ColorScheme.light(
        primary: primaryColor,
        secondary: secondaryColor,
      ),
    );
  }
}
```

## 🔒 Security Guidelines

### Backend Security

- Never commit secrets or API keys
- Use environment variables for sensitive data
- Validate all user inputs
- Implement proper authentication and authorization

```python
# Good: Use environment variables
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')

# Bad: Hardcoded secrets
SECRET_KEY = "my-secret-key-123"
```

### Frontend Security

- Sanitize user inputs
- Use HTTPS for all API calls
- Implement proper error handling
- Don't store sensitive data in local storage

## 📚 Documentation

### Code Documentation

```python
def create_workout(user: User, workout_data: dict) -> Workout:
    """
    Create a new workout for the user.
    
    Args:
        user: The user creating the workout
        workout_data: Dictionary containing workout information
        
    Returns:
        The created workout instance
        
    Raises:
        ValidationError: If workout data is invalid
    """
    # Implementation here
```

### API Documentation

- Use Django Ninja's automatic documentation
- Document all endpoints with examples
- Include error responses

```python
@api.post("/workouts/")
def create_workout(
    request,
    workout: WorkoutCreate,
    user: User = Depends(get_current_user)
) -> WorkoutResponse:
    """
    Create a new workout.
    
    - **name**: Workout name (required)
    - **description**: Workout description (optional)
    - **exercises**: List of exercises (required)
    """
    return workout_service.create_workout(user, workout)
```

## 🐛 Reporting Bugs

### Bug Report Template

```markdown
## Bug Description
Clear description of the bug

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: [e.g. Windows 10]
- Browser: [e.g. Chrome 91]
- Flutter Version: [e.g. 3.0.0]
- Django Version: [e.g. 4.2]

## Screenshots
If applicable, add screenshots

## Additional Context
Any other context about the problem
```

## 💡 Suggesting Features

### Feature Request Template

```markdown
## Feature Description
Clear description of the feature

## Problem Statement
What problem does this feature solve?

## Proposed Solution
How should this feature work?

## Alternatives Considered
Other solutions you've considered

## Additional Context
Any other context or screenshots
```

## ❓ Getting Help

### Resources

- **Documentation**: Check the `/docs` folder
- **Issues**: Search existing issues on GitHub
- **Discussions**: Use GitHub Discussions
- **Code Review**: Ask questions in PR reviews

### Contact

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For general questions
- **Email**: [Your email] (for private matters)

## 🎉 Recognition

Contributors will be recognized in:

- **README.md** contributors section
- **GitHub contributors** page
- **Release notes** for significant contributions

## 📄 License

By contributing to FitTracker, you agree that your contributions will be licensed under the [MIT License](LICENSE).

---

Thank you for contributing to FitTracker! 🚀
