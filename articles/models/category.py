from django.db import models

class Category(models.Model):
    """
    Maqolalarni kategoriyalarga ajratish uchun model.
    """
    name = models.CharField(max_length=100, unique=True)  # Kategoriya nomi
    description = models.TextField(blank=True, null=True)  # Kategoriya haqida qo'shimcha ma'lumot
    created_at = models.DateTimeField(auto_now_add=True)  # Kategoriya yaratilgan vaqti

    def __str__(self):
        return self.name
