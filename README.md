# 🔐 Авторизация (Django + DRF + JWT)

## 📋 Описание проекта

RESTful API на базе **Django** и **Django REST Framework** для безопасного управления пользователями и аутентификации с использованием **JWT (JSON Web Tokens)**.

Проект также включает систему **аудита (логирования)** успешных входов пользователей.
Каждое событие входа записывается в отдельную базу данных с указанием:

* пользователя,
* времени входа,
* IP-адреса,
* и User-Agent.

Для администраторов предусмотрен защищённый API-эндпоинт для получения логов с фильтрацией и пагинацией.

---

## ⚙️ Технологии

* **Python**
* **Django**
* **Django REST Framework**
* **djangorestframework-simplejwt**
* **Celery**
* **Redis**
* **Docker**
* **drf-spectacular (Swagger / Redoc)**

---

## 🚀 Установка и запуск через Docker

### 1️⃣ Клонирование репозитория

```bash
git clone https://github.com/404NotADev/registration.git
cd registration
```

### 2️⃣ Сборка и запуск контейнеров

```bash
docker-compose up --build
```

После успешного запуска приложение будет доступно по адресу:

```
http://127.0.0.1:8000/
```

---

## 🔑 Основные API эндпоинты

| Метод         | URL                           | Описание                                                          |
| ------------- | ----------------------------- | ----------------------------------------------------------------- |
| **POST**      | `/api/v1/users/register/`     | Регистрация нового пользователя                                   |
| **POST**      | `/api/v1/auth/token/`         | Авторизация и получение JWT-токенов                               |
| **POST**      | `/api/v1/auth/token/refresh/` | Обновление токена                                                 |
| **GET/PATCH** | `/api/v1/users/me/`           | Просмотр и редактирование профиля (требуется JWT)                 |
| **GET**       | `/api/v1/logs/login/`         | Получение логов входов пользователей (с фильтрацией и пагинацией) |

---

## 🧾 Модель логов входа

```python
class LoginLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=255)
```

### 🔄 Триггер логирования

Каждый успешный логин через `/api/v1/auth/token/` автоматически записывается в таблицу `LoginLog`.

---

## 📘 Документация API

| Тип                  | URL                  |
| -------------------- | -------------------- |
| **Schema (OpenAPI)** | `/api/schema/`       |
| **Swagger UI**       | `/api/docs/swagger/` |
| **Redoc UI**         | `/api/docs/redoc/`   |

---

## 📦 Стандарты и требования

* Код соответствует стандарту **PEP 8**
* Используется **JWT-аутентификация**
* Реализована **пагинация** и **фильтрация** логов
* Запуск и настройка производятся через **Docker**

---

## 👨‍💻 Автор

**Имналиев Даниэл**
📧 Email: [imanalievdanielsamarovich@gmail.com](mailto:imanalievdanielsamarovich@gmail.com)
🌐 GitHub: [404NotADev](https://github.com/404NotADev)

---

## 🧭 Планы на развитие (ToDo)

* Добавить админ-панель для просмотра логов входов
* Реализовать удаление старых логов через Celery
* Настроить CI/CD (GitHub Actions)

---

## 🪪 Лицензия

Проект распространяется под лицензией **MIT**.

---

📂 Структура проекта (основные файлы):

```
registration/
├── users/
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── logs/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── marketplace/
│   └── settings.py
├── manage.py
└── docker-compose.yml
```
