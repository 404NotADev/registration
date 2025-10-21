from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from logs.models import LoginLog
from logs.tasks import create_login_log  # импортируем Celery задачу

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # Создаём сериализатор и валидируем данные
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user  # ✅ пользователь получен здесь

        # Генерируем JWT-токены
        response = Response(serializer.validated_data, status=200)

        # Асинхронное логирование через Celery
        create_login_log.delay(
            user.id,
            self.get_client_ip(request),
            request.META.get('HTTP_USER_AGENT', '')
        )

        return response

    def get_client_ip(self, request):
        """Возвращает IP-адрес клиента"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


