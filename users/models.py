from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(
        max_length=30,
        verbose_name='Имя',
        blank=True
        )
    last_name = models.CharField(
        max_length=30,
        verbose_name='Фамилия',
        blank=True
        )

    def __str__(self):
        return f"{self.user.profile.first_name} {self.user.profile.last_name}"
    
    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'