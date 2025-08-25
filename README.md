# FitTracker - Fitness Tracking Application

A comprehensive fitness tracking application built with Django REST Framework backend and Flutter frontend.

## 🚀 Project Status

✅ **Backend**: Fully functional Django API with MySQL database  
✅ **Frontend**: Flutter web application  
✅ **Database**: MySQL (Amazon RDS) with sample data  
✅ **Docker**: Complete containerization setup  
✅ **API Documentation**: Swagger/OpenAPI documentation  

## 📊 Current Data

The application includes **50+ sample records** for each table:
- **56 Users** (including test accounts)
- **290 Habits** (various fitness and wellness habits)
- **165 Exercises** (strength training, cardio, etc.)
- **175 Workouts** (training sessions)
- **240 Nutrition entries** (food tracking)
- **53 User statistics** (progress tracking)

## 🏗️ Architecture

```
FitTracker/
├── backend/                 # Django REST API
│   ├── apps/               # Django applications
│   │   ├── accounts/       # User authentication
│   │   ├── habits/         # Habit tracking
│   │   ├── nutrition/      # Nutrition tracking
│   │   ├── stats/          # Statistics & analytics
│   │   └── workouts/       # Workout tracking
│   ├── config/             # Django settings
│   ├── requirements/       # Python dependencies
│   └── Dockerfile*         # Container configurations
├── frontend/               # Flutter application
│   └── fittracker_app/     # Flutter web app
├── docker-compose.yml      # Development setup
├── docker-compose.prod.yml # Production setup
└── nginx.conf*             # Web server configuration
```

## 🛠️ Technology Stack

### Backend
- **Django 5.0.2** - Web framework
- **Django REST Framework** - API framework
- **MySQL** - Database (Amazon RDS)
- **Redis** - Caching
- **JWT** - Authentication
- **Swagger/OpenAPI** - API documentation

### Frontend
- **Flutter** - Cross-platform framework
- **Dart** - Programming language
- **Web** - Target platform

### Infrastructure
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **Nginx** - Reverse proxy
- **AWS RDS** - Database hosting

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose
- Python 3.11+ (for local development)
- Flutter SDK (for frontend development)

### Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd FitTracker
   ```

2. **Start with Docker (Recommended)**
   ```bash
   # Start all services
   docker-compose up
   
   # Or start in background
   docker-compose up -d
   ```

3. **Access the application**
   - **Backend API**: http://localhost:8000
   - **API Documentation**: http://localhost:8000/api/docs/
   - **Frontend**: http://localhost:3000
   - **Admin Panel**: http://localhost:8000/admin

### Production Deployment

1. **Set environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your production values
   ```

2. **Deploy with Docker Compose**
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

3. **Access production**
   - **Application**: http://your-domain.com
   - **API**: http://your-domain.com/api/

## 📚 API Documentation

### Authentication
- `POST /api/auth/jwt/login/` - JWT Login
- `POST /api/auth/jwt/refresh/` - Refresh JWT Token
- `POST /api/auth/register/` - User Registration

### Habits
- `GET/POST /api/habits/` - List/Create habits
- `GET/PUT/DELETE /api/habits/<id>/` - Habit details
- `POST /api/habits/<id>/complete/` - Mark habit as completed

### Workouts
- `GET/POST /api/workouts/` - List/Create workouts
- `GET/PUT/DELETE /api/workouts/<id>/` - Workout details

### Nutrition
- `GET/POST /api/nutrition/` - List/Create nutrition entries
- `GET/PUT/DELETE /api/nutrition/<id>/` - Nutrition entry details

### Statistics
- `GET /api/stats/summary/` - User statistics summary
- `GET /api/stats/health/` - Health check endpoint

## 🔧 Development

### Backend Development

1. **Setup virtual environment**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   .\venv\Scripts\Activate.ps1  # Windows
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements/dev.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Start development server**
   ```bash
   python manage.py runserver
   ```

### Frontend Development

1. **Setup Flutter**
   ```bash
   cd frontend/fittracker_app
   flutter pub get
   ```

2. **Run development server**
   ```bash
   flutter run -d web-server --web-port 3000
   ```

## 🧪 Testing

### Backend Tests
```bash
cd backend
python manage.py test
```

### API Verification
```bash
cd backend
python verify_setup.py
```

## 📊 Database

### Production Database (MySQL)
- **Host**: Amazon RDS MySQL
- **Data**: All sample data included
- **Connection**: Configured in `config/settings.py`

### Development Database (SQLite)
- **File**: `backend/db.sqlite3`
- **Usage**: `python manage.py runserver --settings=config.settings_dev`

## 🔐 Security

- **JWT Authentication** for API access
- **CORS** configured for frontend communication
- **Environment variables** for sensitive data
- **HTTPS** ready for production

## 📈 Monitoring

- **Health Check**: `/api/stats/health/`
- **API Documentation**: `/api/docs/`
- **Admin Panel**: `/admin/`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Check the [API Documentation](http://localhost:8000/api/docs/)
- Review the [Contributing Guide](CONTRIBUTING.md)
- Open an issue on GitHub

---

**FitTracker** - Track your fitness journey with ease! 💪
