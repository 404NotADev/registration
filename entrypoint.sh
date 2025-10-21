#!/bin/sh

# Останавливаем выполнение при ошибках
set -e

echo "Starting entrypoint..."

# Применяем миграции Django
echo "Applying database migrations..."
python manage.py migrate

# Собираем статические файлы
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Если нужно, можно запускать Celery Beat или Worker здесь
# echo "Starting Celery worker..."
# celery -A myproject worker -l info &

# Передаём управление основной команде (CMD)
exec "$@"
