# Script to automatically activate the FitTracker virtual environment
Write-Host "Activating FitTracker virtual environment..." -ForegroundColor Green
& ".\backend\venv\Scripts\Activate.ps1"
Write-Host "Virtual environment activated!" -ForegroundColor Green
Write-Host "Now you can run: python manage.py runserver" -ForegroundColor Yellow

