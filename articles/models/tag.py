from django.db import models

class Tag(models.Model):
    """
    Maqolalarga teglar qo'shish uchun model.
    """
    name = models.CharField(max_length=100, unique=True)  # Teg nomi, takrorlanmas bo'lishi kerak
    created_at = models.DateTimeField(auto_now_add=True)  # Teg yaratilgan vaqti

    def __str__(self):
        return self.name
