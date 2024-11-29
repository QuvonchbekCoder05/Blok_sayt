from django.db import models

class SiteConfiguration(models.Model):
    articles_per_page = models.PositiveIntegerField(default=10)  # Maqolalar soni uchun 
    allowed_file_types = models.JSONField(default=list)  # Ruxsat etilgan fayl turlari uchun 
    max_file_size = models.PositiveIntegerField(default=10485760)  # Maksimal fayl hajmi uchun 

    def save(self, *args, **kwargs):
        if not SiteConfiguration.objects.exists():
            super().save(*args, **kwargs)
        else:
            raise ValueError("Maqola  faqat bitta yozuvga ega bo'lishi kerak!")

    @classmethod
    def get_instance(cls):
        config, created = cls.objects.get_or_create()
        return config

    def __str__(self):
        return "Site Configuration qismi"
