# FitTracker Backend - Script de Instalación Automática
# Este script instala todas las dependencias necesarias para el backend

Write-Host "🚀 Instalando FitTracker Backend..." -ForegroundColor Green
Write-Host ""

# Verificar si Python está instalado
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python encontrado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python no está instalado. Instala Python 3.8+ desde https://python.org" -ForegroundColor Red
    exit 1
}

# Navegar al directorio backend
Set-Location -Path "backend"

# Crear entorno virtual si no existe
if (-not (Test-Path "venv")) {
    Write-Host "📦 Creando entorno virtual..." -ForegroundColor Yellow
    python -m venv venv
}

# Activar entorno virtual
Write-Host "🔄 Activando entorno virtual..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Actualizar pip
Write-Host "⬆️ Actualizando pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip

# Instalar dependencias esenciales primero
Write-Host "📥 Instalando dependencias esenciales..." -ForegroundColor Yellow
pip install -r requirements/install.txt

# Intentar instalar dependencias de desarrollo
Write-Host "📥 Instalando dependencias de desarrollo..." -ForegroundColor Yellow
try {
    pip install -r requirements/dev.txt
    Write-Host "✅ Dependencias de desarrollo instaladas" -ForegroundColor Green
} catch {
    Write-Host "⚠️ Algunas dependencias de desarrollo fallaron, pero las esenciales están instaladas" -ForegroundColor Yellow
}

# Crear archivo .env si no existe
if (-not (Test-Path ".env")) {
    Write-Host "📝 Creando archivo .env..." -ForegroundColor Yellow
    Copy-Item "../env.example" ".env"
}

# Ejecutar migraciones
Write-Host "🗄️ Ejecutando migraciones de base de datos..." -ForegroundColor Yellow
python manage.py migrate

# Crear superusuario (opcional)
Write-Host ""
$createSuperuser = Read-Host "¿Deseas crear un superusuario? (y/N)"
if ($createSuperuser -eq "y" -or $createSuperuser -eq "Y") {
    python manage.py createsuperuser
}

# Verificar instalación
Write-Host ""
Write-Host "🧪 Verificando instalación..." -ForegroundColor Yellow
python manage.py check

Write-Host ""
Write-Host "🎉 ¡Instalación completada!" -ForegroundColor Green
Write-Host "Para iniciar el servidor:" -ForegroundColor Cyan
Write-Host "  cd backend" -ForegroundColor White
Write-Host "  .\venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "  python manage.py runserver 8000" -ForegroundColor White
Write-Host ""
Write-Host "Endpoints disponibles:" -ForegroundColor Cyan
Write-Host "  🌐 API: http://localhost:8000/api/" -ForegroundColor White
Write-Host "  📚 Docs: http://localhost:8000/api/docs/" -ForegroundColor White
Write-Host "  🔧 Admin: http://localhost:8000/admin/" -ForegroundColor White


