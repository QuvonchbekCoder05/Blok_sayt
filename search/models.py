from django.db import models

class SearchTerm(models.Model):
    term = models.CharField(max_length=255, unique=True)  # Qidiruv so'zi
    count = models.PositiveIntegerField(default=0)  # Qancha marta qidirilganini aniqlash uchun 

    def __str__(self):
        return self.term
