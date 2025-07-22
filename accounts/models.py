from django.db import models
from sales.models import Agency
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    agency = models.ForeignKey(
        Agency,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users',
        verbose_name="Agencia"
    )
    is_admin = models.BooleanField(default=False, verbose_name="Es administrador")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    def __str__(self):
        return f"{self.username} ({'Admin' if self.is_admin else 'Usuario'})"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['-created_at']
