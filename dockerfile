# Базовый образ Python
FROM python:3.12-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Сначала обновляем pip, setuptools и wheel
RUN pip install --upgrade pip setuptools wheel

# Затем устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Создаём пользователя для запуска приложения (чтобы не запускать от root)
RUN useradd -m djangouser
USER djangouser

# Команда запуска Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
