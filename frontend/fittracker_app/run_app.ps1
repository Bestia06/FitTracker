# FitTracker Mobile App Runner
# This script helps you run the Flutter mobile app

Write-Host "🚀 FitTracker Mobile App" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green

# Check if Flutter is installed
try {
  $flutterVersion = flutter --version
  Write-Host "✅ Flutter is installed" -ForegroundColor Green
}
catch {
  Write-Host "❌ Flutter is not installed or not in PATH" -ForegroundColor Red
  Write-Host "Please install Flutter from: https://flutter.dev/docs/get-started/install" -ForegroundColor Yellow
  exit 1
}

# Check if we're in the correct directory
if (-not (Test-Path "pubspec.yaml")) {
  Write-Host "❌ Please run this script from the fittracker_app directory" -ForegroundColor Red
  exit 1
}

# Get dependencies
Write-Host "📦 Getting Flutter dependencies..." -ForegroundColor Blue
flutter pub get

if ($LASTEXITCODE -ne 0) {
  Write-Host "❌ Failed to get dependencies" -ForegroundColor Red
  exit 1
}

# Check available devices
Write-Host "📱 Checking available devices..." -ForegroundColor Blue
flutter devices

# Ask user which device to use
Write-Host ""
Write-Host "Select a device to run the app on:" -ForegroundColor Yellow
Write-Host "1. Android Emulator" -ForegroundColor White
Write-Host "2. iOS Simulator (macOS only)" -ForegroundColor White
Write-Host "3. Chrome (Web)" -ForegroundColor White
Write-Host "4. Physical device (if connected)" -ForegroundColor White

$choice = Read-Host "Enter your choice (1-4)"

switch ($choice) {
  "1" {
    Write-Host "🤖 Starting Android emulator..." -ForegroundColor Blue
    flutter run -d android
  }
  "2" {
    Write-Host "🍎 Starting iOS simulator..." -ForegroundColor Blue
    flutter run -d ios
  }
  "3" {
    Write-Host "🌐 Starting Chrome..." -ForegroundColor Blue
    flutter run -d chrome
  }
  "4" {
    Write-Host "📱 Running on physical device..." -ForegroundColor Blue
    flutter run
  }
  default {
    Write-Host "❌ Invalid choice. Running on default device..." -ForegroundColor Yellow
    flutter run
  }
}

Write-Host ""
Write-Host "🎉 App should be starting now!" -ForegroundColor Green
Write-Host "Use 'r' to hot reload, 'R' to hot restart, 'q' to quit" -ForegroundColor Cyan
