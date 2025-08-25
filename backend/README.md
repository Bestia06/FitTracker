# FitTracker Backend

A robust Django-based backend API for the FitTracker fitness application.

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Virtual environment (already set up)

### Getting Started

1. **Activate the virtual environment**
   ```bash
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1
   
   # Windows Command Prompt
   venv\Scripts\activate.bat
   
   # Linux/Mac
   source venv/bin/activate
   ```

2. **Install dependencies** (if not already installed)
   ```bash
   pip install -r requirements/dev.txt
   ```

3. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

4. **Start the development server**
   ```bash
   python manage.py runserver
   ```

5. **Access the application**
   - 🌐 API Root: http://127.0.0.1:8000/
   - 📚 API Documentation: http://127.0.0.1:8000/api/docs/
   - 🔧 Django Admin: http://127.0.0.1:8000/admin

## 🏗️ Project Structure

```
backend/
├── apps/                    # Django applications
│   ├── accounts/           # User authentication & profiles
│   ├── habits/             # Habit tracking
│   ├── nutrition/          # Nutrition tracking
│   ├── stats/              # Statistics & analytics
│   └── workouts/           # Workout tracking
├── config/                 # Django settings
├── core/                   # Core utilities
├── requirements/           # Python dependencies
├── tests/                  # Test suite
└── manage.py              # Django management script
```

## 🔧 Available Commands

### Development
```bash
# Check for issues
python manage.py check

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver

# Run tests
python manage.py test
```

### Database
```bash
# Show migrations status
python manage.py showmigrations

# Create new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

## 📚 API Endpoints

### Authentication
- `POST /api/auth/jwt/login/` - JWT Login
- `POST /api/auth/jwt/refresh/` - Refresh JWT Token
- `POST /api/auth/register/` - User Registration

### Habits
- `GET/POST /api/habits/` - List/Create habits
- `GET/PUT/DELETE /api/habits/<id>/` - Habit details
- `POST /api/habits/<id>/complete/` - Mark habit as completed
- `POST /api/habits/<id>/incomplete/` - Mark habit as incomplete
- `GET /api/habits/<id>/progress/` - Get habit progress

### Nutrition
- `GET/POST /api/nutrition/` - List/Create nutrition entries
- `GET/PUT/DELETE /api/nutrition/<id>/` - Nutrition entry details
- `POST /api/nutrition/enrich/` - Enrich nutrition data

### Workouts
- `GET/POST /api/workouts/` - List/Create workouts
- `GET/PUT/DELETE /api/workouts/<id>/` - Workout details
- `GET /api/workouts/exercises/search/` - Search exercises

### Statistics
- `GET /api/stats/summary/` - User statistics summary
- `GET/PUT /api/stats/user/` - User stats
- `GET/POST /api/stats/habits/progress/` - Habit progress stats
- `GET/POST /api/stats/workouts/` - Workout statistics
- `GET/POST /api/stats/nutrition/` - Nutrition statistics

## 🔐 Authentication

The API uses JWT (JSON Web Tokens) for authentication. Include the token in the Authorization header:

```
Authorization: Bearer <your_jwt_token>
```

## 🛠️ Configuration

### Environment Variables
- `SECRET_KEY` - Django secret key
- `DEBUG` - Debug mode (True/False)
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts
- `API_NINJA_KEY` - API Ninja key for external data
- `DB_*` - Database configuration variables

### Database
The application is configured to use MySQL by default, but can be switched to SQLite for development.

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.habits

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

## 📝 API Documentation

The API documentation is automatically generated using drf-spectacular and is available at:
- Swagger UI: http://127.0.0.1:8000/api/docs/
- ReDoc: http://127.0.0.1:8000/api/redoc/
- OpenAPI Schema: http://127.0.0.1:8000/api/schema/

## 🔧 Troubleshooting

### Common Issues

1. **Django not found**: Make sure the virtual environment is activated
2. **Database connection errors**: Check your database configuration
3. **Migration errors**: Run `python manage.py migrate` to apply pending migrations
4. **Import errors**: Ensure all dependencies are installed with `pip install -r requirements/dev.txt`

### Getting Help

If you encounter issues:
1. Check the Django logs in the console
2. Verify the virtual environment is activated
3. Ensure all migrations are applied
4. Check the API documentation for endpoint details
