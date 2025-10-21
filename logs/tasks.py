from celery import shared_task
from .models import LoginLog
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def create_login_log(user_id, ip_address, user_agent):
    user = User.objects.get(id=user_id)
    LoginLog.objects.create(
        user=user,
        ip_address=ip_address,
        user_agent=user_agent
    )
