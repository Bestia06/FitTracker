# 🏃‍♂️ FitTracker - Aplicación de Fitness Completa

[![Django](https://img.shields.io/badge/Django-5.0.2-green.svg)](https://django.com)
[![Flutter](https://img.shields.io/badge/Flutter-3.0+-blue.svg)](https://flutter.dev)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)](https://mysql.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)

**FitTracker** es una aplicación completa de fitness que combina un backend robusto en Django con una aplicación móvil moderna en Flutter, diseñada para ayudar a los usuarios a rastrear sus hábitos, entrenamientos y nutrición.

## 🎨 Diseños de Figma

### 📱 Diseños de la Aplicación Móvil
- **Figma Design**: [FitTracker Mobile App Design](https://www.figma.com/design/yx0c9lSdTkqt3Lvka7VNkh/Untitled?node-id=0-1&t=8x9ECGHJFux02pXz-1)
- **Características del diseño**:
  - Interfaz moderna y intuitiva
  - Paleta de colores profesional
  - Navegación fluida con bottom navigation
  - Pantallas de autenticación elegantes
  - Dashboard con estadísticas visuales
  - Gestión de hábitos con progreso visual
  - Placeholder para entrenamientos y nutrición

### 🎯 Pantallas Implementadas
1. **Splash Screen** - Pantalla de carga con animaciones
2. **Login/Register** - Autenticación con validación
3. **Dashboard** - Resumen de progreso y estadísticas
4. **Habits** - Gestión y seguimiento de hábitos
5. **Workouts** - Placeholder para entrenamientos
6. **Nutrition** - Placeholder para nutrición
7. **Profile** - Perfil de usuario y configuración

## 🏗️ Arquitectura del Proyecto

```
FitTracker/
├── backend/                 # Backend Django
│   ├── apps/               # Aplicaciones Django
│   │   ├── accounts/       # Gestión de usuarios
│   │   ├── habits/         # Gestión de hábitos
│   │   ├── nutrition/      # Gestión de nutrición
│   │   ├── workouts/       # Gestión de entrenamientos
│   │   └── stats/          # Estadísticas y análisis
│   ├── config/             # Configuración Django
│   ├── requirements/       # Dependencias Python
│   └── manage.py           # Comando Django
├── frontend/               # Frontend Flutter
│   └── fittracker_app/     # Aplicación Flutter
│       ├── lib/            # Código fuente Dart
│       ├── assets/         # Recursos (imágenes, fuentes)
│       └── pubspec.yaml    # Dependencias Flutter
├── docker-compose.yml      # Configuración Docker
├── nginx.conf             # Configuración Nginx
└── README.md              # Este archivo
```

## 🚀 Tecnologías Utilizadas

### Backend (Django)
- **Framework**: Django 5.0.2
- **API**: Django REST Framework
- **Autenticación**: JWT (JSON Web Tokens)
- **Base de datos**: MySQL (Amazon RDS) + SQLite (local)
- **Documentación**: Swagger/OpenAPI
- **CORS**: django-cors-headers
- **Validación**: django-filter

### Frontend (Flutter)
- **Framework**: Flutter 3.0+
- **Estado**: Riverpod
- **Navegación**: GoRouter
- **HTTP**: Dio + Retrofit
- **Almacenamiento**: SharedPreferences + SecureStorage
- **UI**: Material Design 3
- **Gráficos**: fl_chart + Syncfusion Charts

### DevOps
- **Contenedores**: Docker + Docker Compose
- **Proxy**: Nginx
- **CI/CD**: GitHub Actions (configurado)

## 📊 Estado del Proyecto

### ✅ Completado
- [x] Backend Django completamente funcional
- [x] API REST con 39 endpoints verificados
- [x] Autenticación JWT implementada
- [x] Base de datos MySQL configurada
- [x] Aplicación Flutter con UI completa
- [x] Navegación y estado gestionado
- [x] Diseños de Figma implementados
- [x] Docker configurado para desarrollo y producción
- [x] Documentación de API (Swagger)

### 🔄 En Desarrollo
- [ ] Integración completa frontend-backend
- [ ] Funcionalidad de entrenamientos
- [ ] Funcionalidad de nutrición
- [ ] Gráficos y estadísticas avanzadas
- [ ] Notificaciones push

## 🛠️ Instalación y Configuración

### Prerrequisitos
- Python 3.8+
- Flutter 3.0+
- Docker (opcional)
- MySQL (para producción)

### 1. Clonar el Repositorio
```bash
git clone <repository-url>
cd FitTracker
```

### 2. Configurar el Backend
```bash
# Activar entorno virtual
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements/dev.txt

# Configurar variables de entorno
cp ../env.example .env
# Editar .env con tus configuraciones

# Ejecutar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver 8000
```

### 3. Configurar el Frontend
```bash
# Navegar al directorio de la app
cd frontend/fittracker_app

# Obtener dependencias
flutter pub get

# Ejecutar la aplicación
flutter run -d chrome --web-port 3000
```

### 4. Verificar la Instalación
```bash
# Verificar endpoints del backend
cd backend
python verify_endpoints.py

# Verificar integración
cd ..
python test_integration.py

# Verificar puertos
python check_ports.py
```

## 🔧 Configuración de Puertos

| Servicio | Puerto | Descripción |
|----------|--------|-------------|
| Backend Django | 8000 | API REST |
| Frontend Flutter | 3000 | Aplicación web |
| MySQL | 3306 | Base de datos |
| Nginx | 80 | Proxy reverso |

## 📱 Uso de la Aplicación

### Credenciales de Demo
- **Email**: `demo@fittracker.com`
- **Contraseña**: `123456`

### Funcionalidades Disponibles
1. **Autenticación**: Registro y login con JWT
2. **Dashboard**: Resumen de progreso diario
3. **Hábitos**: Crear, editar y completar hábitos
4. **Perfil**: Información del usuario y estadísticas
5. **API**: 39 endpoints completamente funcionales

## 🔌 Endpoints de la API

### Autenticación
- `POST /api/auth/jwt/login/` - Login con JWT
- `POST /api/auth/jwt/refresh/` - Renovar token
- `POST /api/auth/register/` - Registro de usuario

### Usuarios
- `GET /api/accounts/profile/` - Perfil del usuario
- `PUT /api/accounts/profile/` - Actualizar perfil

### Hábitos
- `GET /api/habits/` - Listar hábitos
- `POST /api/habits/` - Crear hábito
- `GET /api/habits/{id}/` - Detalle de hábito
- `PUT /api/habits/{id}/` - Actualizar hábito
- `DELETE /api/habits/{id}/` - Eliminar hábito

### Nutrición
- `GET /api/nutrition/` - Listar entradas de nutrición
- `POST /api/nutrition/` - Crear entrada de nutrición
- `POST /api/nutrition/enrich/` - Enriquecer datos nutricionales

### Entrenamientos
- `GET /api/workouts/` - Listar entrenamientos
- `POST /api/workouts/` - Crear entrenamiento
- `GET /api/workouts/exercises/search/` - Buscar ejercicios

### Estadísticas
- `GET /api/stats/summary/` - Resumen de estadísticas
- `GET /api/stats/user/` - Estadísticas del usuario
- `GET /api/stats/health/` - Health check

### Documentación
- `GET /api/docs/` - Swagger UI
- `GET /api/redoc/` - ReDoc
- `GET /api/schema/` - Esquema OpenAPI

## 🐳 Docker

### Desarrollo
```bash
docker-compose up -d
```

### Producción
```bash
docker-compose -f docker-compose.prod.yml up -d
```

## 🧪 Testing

### Backend
```bash
cd backend
python manage.py test
```

### Frontend
```bash
cd frontend/fittracker_app
flutter test
```

### Integración
```bash
python test_integration.py
```

## 📈 Base de Datos

### Configuración
- **Desarrollo**: SQLite local
- **Producción**: MySQL en Amazon RDS
- **Migraciones**: Automáticas con Django

### Datos de Ejemplo
El proyecto incluye scripts para generar datos de ejemplo:
- 50 usuarios de prueba
- 50 hábitos por usuario
- 50 entrenamientos por usuario
- 50 entradas de nutrición por usuario

## 🔒 Seguridad

- Autenticación JWT
- CORS configurado
- Validación de datos
- Sanitización de inputs
- Headers de seguridad

## 📚 Documentación

- [API Documentation](http://localhost:8000/api/docs/)
- [Backend README](backend/README.md)
- [Frontend README](frontend/fittracker_app/README.md)
- [Docker Setup](docs/docker_setup.md)

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👥 Equipo

- **Desarrollo Backend**: Django + DRF
- **Desarrollo Frontend**: Flutter
- **Diseño UI/UX**: Figma
- **DevOps**: Docker + Nginx

## 📞 Soporte

- **Issues**: [GitHub Issues](https://github.com/your-repo/issues)
- **Documentación**: [Wiki](https://github.com/your-repo/wiki)
- **Email**: support@fittracker.com

---

**FitTracker** - Tu compañero de fitness personal 🏃‍♂️💪
