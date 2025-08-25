# 🏃‍♂️ FitTracker

<div align="center">

![FitTracker Logo](https://img.shields.io/badge/FitTracker-Fitness%20Tracking-blue?style=for-the-badge&logo=django&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2+-green?style=for-the-badge&logo=django&logoColor=white)
![Flutter](https://img.shields.io/badge/Flutter-3.0+-blue?style=for-the-badge&logo=flutter&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-AWS%20RDS-orange?style=for-the-badge&logo=mysql&logoColor=white)

**A comprehensive fitness tracking application built with Django Ninja (backend) and Flutter (frontend)**

[🚀 Features](#-features) • [🏗️ Architecture](#️-architecture) • [🛠️ Tech Stack](#️-tech-stack) • [🚀 Quick Start](#-quick-start) • [📚 API Docs](#-api-documentation)

</div>

---

## 🎯 Overview

FitTracker is a modern fitness application that helps users track their workouts, nutrition, habits, and overall fitness progress. Built with a robust Django Ninja backend and a beautiful Flutter frontend, it provides a seamless experience across all platforms.

## 🏗️ Architecture

```
FitTracker/
├── 🐍 backend/                 # Django Ninja backend
│   ├── 📱 apps/               # Django applications
│   │   ├── 🔐 accounts/       # User authentication & profiles
│   │   ├── 💪 workouts/       # Workout tracking & exercises
│   │   ├── 🥗 nutrition/      # Nutrition tracking & meals
│   │   ├── 📊 stats/          # Statistics & progress analytics
│   │   └── ✅ habits/         # Habit tracking & streaks
│   ├── ⚙️ config/             # Django settings & configuration
│   ├── 🔧 core/               # Core utilities & helpers
│   ├── 📦 requirements/       # Python dependencies
│   └── 🧪 tests/              # Backend tests
├── 📱 frontend/               # Flutter frontend
│   └── fittracker_app/        # Flutter application
│       ├── lib/
│       │   ├── 🎨 app/        # App configuration & theme
│       │   ├── 🚀 features/   # Feature modules
│       │   └── 🔄 shared/     # Shared components & utilities
│       └── test/              # Frontend tests
├── 📚 docs/                   # Documentation & schemas
├── 🐳 docker-compose.yml      # Docker configuration
└── 📄 README.md               # This file
```

## 🚀 Features

### 🔐 Authentication & User Management
- **JWT Authentication**: Secure token-based authentication
- **Role-based Access Control**: User roles and permissions
- **User Profiles**: Extended user information and preferences
- **Social Login**: Integration with social platforms (planned)

### 💪 Workout Tracking
- **Exercise Library**: Comprehensive exercise database
- **Workout Plans**: Custom and pre-built workout routines
- **Progress Tracking**: Weight, reps, and performance metrics
- **Workout History**: Complete workout logging and history

### 🥗 Nutrition Management
- **Food Database**: Extensive food and nutrition information
- **Meal Logging**: Daily meal and calorie tracking
- **Macro Tracking**: Protein, carbs, and fat monitoring
- **Nutrition Goals**: Personalized nutrition targets

### 📊 Analytics & Statistics
- **Progress Charts**: Visual progress tracking
- **Body Measurements**: Weight, body fat, and measurements
- **Fitness Goals**: Goal setting and achievement tracking
- **Performance Analytics**: Detailed workout analytics

### ✅ Habit Tracking
- **Daily Habits**: Customizable daily habit tracking
- **Streak Counter**: Habit streak monitoring
- **Habit Categories**: Organized habit management
- **Progress Visualization**: Habit completion charts

## 🛠️ Tech Stack

### 🐍 Backend (Django Ninja)
- **Framework**: Django 4.2+
- **API**: Django Ninja (Fast API-style for Django)
- **Database**: MySQL 8.0 (AWS RDS)
- **Authentication**: JWT (JSON Web Tokens)
- **Cache**: Redis (planned implementation)
- **Testing**: pytest
- **Documentation**: Auto-generated API docs

### 📱 Frontend (Flutter)
- **Framework**: Flutter 3.0+
- **State Management**: Riverpod
- **Navigation**: GoRouter
- **HTTP Client**: Dio
- **UI Framework**: Material Design 3
- **Testing**: Flutter Test

### ☁️ Infrastructure
- **Database**: AWS RDS MySQL
- **Containerization**: Docker & Docker Compose
- **CI/CD**: GitHub Actions
- **Cache**: Redis (planned)
- **Monitoring**: Application monitoring (planned)

## 🗄️ Database Configuration

### AWS RDS MySQL Setup
```bash
# Database Connection Details
Server: fittrackdb.ceja6aik6pl1.us-east-1.rds.amazonaws.com
Database: FitTrackerDB
Username: admin
Password: Alpha*FitTracker*5
Port: 3306 (default)
```

### Environment Variables
```bash
# Database Configuration
DATABASE_URL=mysql://admin:Alpha*FitTracker*5@fittrackdb.ceja6aik6pl1.us-east-1.rds.amazonaws.com:3306/FitTrackerDB

# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# JWT Settings
JWT_SECRET_KEY=your-jwt-secret-key
JWT_ACCESS_TOKEN_LIFETIME=5
JWT_REFRESH_TOKEN_LIFETIME=1
```

## 📋 Prerequisites

- **Python**: 3.11+
- **Flutter**: 3.0+
- **Docker**: Latest version
- **MySQL**: 8.0+ (or AWS RDS)
- **Redis**: 6.0+ (for caching, planned)

## 🚀 Quick Start

### 🐳 Using Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/josephr2316/fittracker.git
   cd fittracker
   ```

2. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your AWS RDS configuration
   ```

3. **Start the application**
   ```bash
   docker-compose up -d
   ```

4. **Access the application**
   - 🌐 Backend API: http://localhost:8000
   - 📱 Frontend Web: http://localhost:3000
   - 🔧 Django Admin: http://localhost:8000/admin
   - 📚 API Docs: http://localhost:8000/api/docs

### 🛠️ Manual Setup

#### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Activate virtual environment**
   ```bash
   # On Windows PowerShell:
   .\venv\Scripts\Activate.ps1
   
   # On Windows Command Prompt:
   venv\Scripts\activate.bat
   
   # On Linux/Mac:
   source venv/bin/activate
   ```

3. **Install dependencies (if not already installed)**
   ```bash
   pip install -r requirements/dev.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

   **Or use the provided script:**
   ```bash
   # From project root:
   .\start_backend.ps1
   ```

7. **Access the application**
   - 🌐 Backend API: http://127.0.0.1:8000
   - 📚 API Documentation: http://127.0.0.1:8000/api/docs/
   - 🔧 Django Admin: http://127.0.0.1:8000/admin

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

### Django Ninja Auto-generated Docs
- **Swagger UI**: http://localhost:8000/api/docs/
- **ReDoc**: http://localhost:8000/api/redoc/

### API Endpoints Overview
```
/api/v1/
├── auth/           # Authentication endpoints
├── users/          # User management
├── workouts/       # Workout operations
├── nutrition/      # Nutrition tracking
├── stats/          # Statistics & analytics
└── habits/         # Habit management
```

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

### Integration Tests
```bash
# Run all tests
docker-compose -f docker-compose.test.yml up
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

### AWS Deployment
```bash
# Deploy to AWS ECS
aws ecs update-service --cluster fittracker-cluster --service fittracker-service --force-new-deployment
```

## 🔧 Development

### Code Style
- **Backend**: Black, isort, flake8
- **Frontend**: Dart formatter
- **Git Hooks**: Pre-commit hooks for code quality

### Branching Strategy
```
main          # Production-ready code
develop       # Integration branch
feature/*     # New features
bugfix/*      # Bug fixes
hotfix/*      # Critical fixes
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes** and add tests
4. **Commit your changes** (`git commit -m 'Add amazing feature'`)
5. **Push to the branch** (`git push origin feature/amazing-feature`)
6. **Open a Pull Request**

### Team Responsibilities
- **Backend Changes**: @jumaster23 will review Django/Python code
- **Frontend Changes**: @Hakerman564 will review Flutter/Dart code
- **UI/UX Changes**: @franibelmtdl will review design and user experience
- **Database Changes**: @Bestia06 will review schema and data models
- **Test Changes**: @josejavierbatistacastillo will review test implementations
- **Infrastructure Changes**: @josephr2316 will review DevOps and configuration

### Development Guidelines
- Write clear commit messages
- Add tests for new features
- Update documentation
- Follow the existing code style
- Ensure all tests pass
- Request review from the appropriate team member based on your changes

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. 📖 Check the [Documentation](docs/)
2. 🐛 Search [Issues](https://github.com/josephr2316/fittracker/issues)
3. 💬 Create a new issue with detailed information
4. 📧 Contact the maintainers

## 👥 Team

### 🏗️ Project Leadership
- **@josephr2316** - Project Lead, AWS RDS Database Setup, JWT Implementation, Django Ninja API, Infrastructure & DevOps

### 🐍 Backend Development
- **@jumaster23** - Django Backend Development, API Endpoints, Core Backend Logic

### 📱 Frontend Development
- **@Hakerman564** - Flutter Frontend Development, Mobile App Implementation

### 🎨 UX/UI Design
- **@franibelmtdl** - User Experience & Interface Design, Frontend Assets, Design System

### 🧪 Testing & Quality Assurance
- **@josejavierbatistacastillo** - Test Implementation, Quality Assurance, Test Automation

### 🗄️ Database & Schema
- **@Bestia06** - Database Schema Design, Table Creation, Data Modeling

## 📊 Project Status

### ✅ Completed
- [x] 🏗️ Project structure and architecture
- [x] 📚 Documentation (README, CONTRIBUTING, env.example)
- [x] 🐳 Docker configuration
- [x] 🔧 Development environment setup
- [x] 📋 Code quality tools (pre-commit, EditorConfig)
- [x] 🎨 VS Code configuration
- [x] 🗄️ Database schema design
- [x] 👥 Team structure and responsibilities

### 🚧 In Progress
- [ ] 🔐 JWT Authentication implementation (@jumaster23 + @josephr2316)
- [ ] 🗄️ Redis Caching setup (@josephr2316)
- [ ] 📱 Flutter UI development (@Hakerman564 + @franibelmtdl)
- [ ] 🐍 Django Ninja API endpoints (@jumaster23)
- [ ] 🧪 Test implementation (@josejavierbatistacastillo)
- [ ] 🗄️ Database tables creation (@Bestia06)

### 🗺️ Roadmap

### 🚀 Upcoming Features
- [ ] 🔐 JWT Role-based Authentication
- [ ] 🗄️ Redis Caching Implementation
- [ ] 📱 Mobile App Optimization
- [ ] 👥 Social Features
- [ ] 📊 Advanced Analytics
- [ ] ⌚ Fitness Device Integration
- [ ] 🍽️ Meal Planning
- [ ] 📋 Workout Templates
- [ ] 📸 Progress Photos
- [ ] 📤 Export Functionality

### 🔧 Technical Improvements
- [ ] 🧪 Comprehensive Test Coverage
- [ ] 📈 Performance Optimization
- [ ] 🔒 Enhanced Security
- [ ] 📱 PWA Support
- [ ] 🌐 Internationalization

---

<div align="center">

**Made with ❤️ by the FitTracker team**

### 🏗️ Team Members
[@josephr2316](https://github.com/josephr2316) • [@jumaster23](https://github.com/jumaster23) • [@Hakerman564](https://github.com/Hakerman564) • [@franibelmtdl](https://github.com/franibelmtdl) • [@josejavierbatistacastillo](https://github.com/josejavierbatistacastillo) • [@Bestia06](https://github.com/Bestia06)

[![GitHub stars](https://img.shields.io/github/stars/josephr2316/fittracker?style=social)](https://github.com/josephr2316/fittracker/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/josephr2316/fittracker?style=social)](https://github.com/josephr2316/fittracker/network)
[![GitHub issues](https://img.shields.io/github/issues/josephr2316/fittracker)](https://github.com/josephr2316/fittracker/issues)
[![GitHub license](https://img.shields.io/github/license/josephr2316/fittracker)](https://github.com/josephr2316/fittracker/blob/main/LICENSE)

</div>
