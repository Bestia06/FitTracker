# 🗄️ Database Setup Guide

## AWS RDS MySQL Configuration

### Database Connection Details

```bash
# AWS RDS MySQL Instance
Server: fittrackdb.ceja6aik6pl1.us-east-1.rds.amazonaws.com
Database: FitTrackerDB
Username: admin
Password: Alpha*FitTracker*5
Port: 3306 (default)
Region: us-east-1
```

### Connection String Format

```bash
# Full connection string
mysql://admin:Alpha*FitTracker*5@fittrackdb.ceja6aik6pl1.us-east-1.rds.amazonaws.com:3306/FitTrackerDB

# Django DATABASE_URL format
DATABASE_URL=mysql://admin:Alpha*FitTracker*5@fittrackdb.ceja6aik6pl1.us-east-1.rds.amazonaws.com:3306/FitTrackerDB
```

### Django Settings Configuration

```python
# settings.py
import os
from urllib.parse import urlparse

# Parse DATABASE_URL
db_url = urlparse(os.getenv('DATABASE_URL', 'mysql://admin:Alpha*FitTracker*5@fittrackdb.ceja6aik6pl1.us-east-1.rds.amazonaws.com:3306/FitTrackerDB'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_url.path[1:],  # Remove leading slash
        'USER': db_url.username,
        'PASSWORD': db_url.password,
        'HOST': db_url.hostname,
        'PORT': db_url.port or '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```

### Required Python Packages

```bash
# Install MySQL client for Python
pip install mysqlclient

# Or use PyMySQL (pure Python implementation)
pip install PyMySQL
```

### Local Development Setup

For local development, you can use the local MySQL container:

```bash
# Using Docker Compose
docker-compose up db

# Connection details for local development
Host: localhost
Port: 3306
Database: FitTrackerDB
Username: admin
Password: Alpha*FitTracker*5
```

### Production Deployment

For production, use the AWS RDS instance directly:

```bash
# Environment variables for production
DATABASE_URL=mysql://admin:Alpha*FitTracker*5@fittrackdb.ceja6aik6pl1.us-east-1.rds.amazonaws.com:3306/FitTrackerDB
```

### Database Migrations

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Make migrations for new models
python manage.py makemigrations

# Show migration status
python manage.py showmigrations
```

### Backup and Restore

```bash
# Backup database
mysqldump -h fittrackdb.ceja6aik6pl1.us-east-1.rds.amazonaws.com -u admin -p FitTrackerDB > backup.sql

# Restore database
mysql -h fittrackdb.ceja6aik6pl1.us-east-1.rds.amazonaws.com -u admin -p FitTrackerDB < backup.sql
```

### Security Considerations

1. **Network Security**: Ensure your application is running in a VPC that can access the RDS instance
2. **SSL Connection**: Enable SSL for database connections
3. **IAM Authentication**: Consider using IAM database authentication for enhanced security
4. **Encryption**: Ensure RDS encryption is enabled
5. **Backup**: Enable automated backups

### Monitoring and Maintenance

```bash
# Check database connection
python manage.py dbshell

# Monitor database performance
python manage.py shell
>>> from django.db import connection
>>> connection.queries  # View executed queries
```

### Troubleshooting

#### Common Issues

1. **Connection Timeout**
   ```bash
   # Check if RDS instance is accessible
   telnet fittrackdb.ceja6aik6pl1.us-east-1.rds.amazonaws.com 3306
   ```

2. **Authentication Error**
   ```bash
   # Verify credentials
   mysql -h fittrackdb.ceja6aik6pl1.us-east-1.rds.amazonaws.com -u admin -p
   ```

3. **Character Set Issues**
   ```python
   # Add to DATABASES configuration
   'OPTIONS': {
       'charset': 'utf8mb4',
       'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
   }
   ```

### Performance Optimization

1. **Connection Pooling**: Use connection pooling for better performance
2. **Indexing**: Ensure proper indexes on frequently queried fields
3. **Query Optimization**: Monitor slow queries and optimize them
4. **Caching**: Implement Redis caching for frequently accessed data

### Redis Integration (Planned)

```python
# Redis configuration for caching
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.getenv('REDIS_URL', 'redis://localhost:6379/1'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

### Environment Variables Summary

```bash
# Required for database connection
DATABASE_URL=mysql://admin:Alpha*FitTracker*5@fittrackdb.ceja6aik6pl1.us-east-1.rds.amazonaws.com:3306/FitTrackerDB

# Alternative individual settings
DB_ENGINE=django.db.backends.mysql
DB_HOST=fittrackdb.ceja6aik6pl1.us-east-1.rds.amazonaws.com
DB_PORT=3306
DB_NAME=FitTrackerDB
DB_USER=admin
DB_PASSWORD=Alpha*FitTracker*5

# Redis for caching (planned)
REDIS_URL=redis://localhost:6379/0
```
