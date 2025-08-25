# Simple script to start the FitTracker backend server
Write-Host "Starting FitTracker Backend Server..." -ForegroundColor Green
Write-Host "Make sure you're in the backend directory and virtual environment is activated" -ForegroundColor Yellow
Write-Host "If not, run: cd backend && .\venv\Scripts\Activate.ps1" -ForegroundColor Yellow
Write-Host ""
Write-Host "Starting server on http://127.0.0.1:8000" -ForegroundColor Cyan
Write-Host "API Documentation: http://127.0.0.1:8000/api/docs/" -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Red
Write-Host ""

python manage.py runserver
