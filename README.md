# FitTracker

A comprehensive fitness tracking application built with Django (backend) and Flutter (frontend).

## 🏗️ Project Structure

```
FitTracker/
├── backend/                 # Django backend
│   ├── apps/               # Django applications
│   │   ├── accounts/       # User authentication & profiles
│   │   ├── workouts/       # Workout tracking
│   │   ├── nutrition/      # Nutrition tracking
│   │   ├── stats/          # Statistics & progress
│   │   └── habits/         # Habit tracking
│   ├── config/             # Django settings
│   ├── core/               # Core utilities
│   ├── requirements/       # Python dependencies
│   └── tests/              # Backend tests
├── frontend/               # Flutter frontend
│   └── fittracker_app/     # Flutter application
│       ├── lib/
│       │   ├── app/        # App configuration
│       │   ├── features/   # Feature modules
│       │   └── shared/     # Shared components
│       └── test/           # Frontend tests
├── docs/                   # Documentation
├── .github/                # GitHub workflows
└── docker-compose.yml      # Docker configuration
```

## 🚀 Features

### Backend (Django)
- **User Management**: Custom user model with profiles
- **Workout Tracking**: Exercises, workouts, and progress
- **Nutrition Tracking**: Food database and meal logging
- **Statistics**: Body measurements and fitness goals
- **Habit Tracking**: Daily habits and streaks
- **REST API**: Django REST Framework
- **Authentication**: JWT-based authentication

### Frontend (Flutter)
- **Cross-platform**: iOS, Android, and Web support
- **Modern UI**: Material Design 3
- **State Management**: Riverpod
- **Navigation**: GoRouter
- **Responsive**: Adaptive layouts

## 🛠️ Tech Stack

### Backend
- **Framework**: Django 4.2+
- **Database**: PostgreSQL
- **Cache**: Redis
- **API**: Django REST Framework
- **Authentication**: JWT
- **Testing**: pytest

### Frontend
- **Framework**: Flutter 3.0+
- **State Management**: Riverpod
- **Navigation**: GoRouter
- **HTTP Client**: Dio
- **Testing**: Flutter Test

### DevOps
- **Containerization**: Docker & Docker Compose
- **CI/CD**: GitHub Actions
- **Database**: PostgreSQL
- **Cache**: Redis

## 📋 Prerequisites

- Python 3.11+
- Flutter 3.0+
- Docker & Docker Compose
- PostgreSQL
- Redis

## 🚀 Quick Start

### Using Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/fittracker.git
   cd fittracker
   ```

2. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

3. **Start the application**
   ```bash
   docker-compose up -d
   ```

4. **Access the application**
   - Backend API: http://localhost:8000
   - Frontend Web: http://localhost:3000
   - Django Admin: http://localhost:8000/admin

### Manual Setup

#### Backend Setup

1. **Create virtual environment**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements/dev.txt
   ```

3. **Set up database**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Run development server**
   ```bash
   python manage.py runserver
   ```

#### Frontend Setup

1. **Install Flutter dependencies**
   ```bash
   cd frontend/fittracker_app
   flutter pub get
   ```

2. **Run the application**
   ```bash
   # For web
   flutter run -d chrome
   
   # For mobile
   flutter run
   ```

## 📚 API Documentation

The API documentation is available at:
- Swagger UI: http://localhost:8000/api/docs/
- ReDoc: http://localhost:8000/api/redoc/

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend/fittracker_app
flutter test
```

## 📦 Deployment

### Production Setup

1. **Environment Configuration**
   ```bash
   cp env.example .env.prod
   # Configure production environment variables
   ```

2. **Build and Deploy**
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/fittracker/issues) page
2. Create a new issue with detailed information
3. Contact the maintainers

## 🗺️ Roadmap

- [ ] Mobile app optimization
- [ ] Social features
- [ ] Advanced analytics
- [ ] Integration with fitness devices
- [ ] Meal planning
- [ ] Workout templates
- [ ] Progress photos
- [ ] Export functionality

---

Made with ❤️ by the FitTracker team
