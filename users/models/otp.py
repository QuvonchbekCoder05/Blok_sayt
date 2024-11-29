from django.db import models
from django.utils.timezone import now,timedelta
import random
from users.models.user import User


class OTP(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="otps")
    otp_code = models.CharField(max_length=6)  # 6 xonali tasdiqlash kodi
    created_at = models.DateTimeField(auto_now_add=True)  # Yaratilgan vaqt
    expires_at = models.DateTimeField()  # Tugash muddati

    @staticmethod
    def generate_otp_code():
        """
        Tasdiqlash kodi generatsiya qilish.
        """
       
        return str(random.randint(100000, 999999))

    def is_valid(self):
        return now() <= self.expires_at

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = now() + timedelta(minutes=10)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"OTP for {self.user.email} - {self.otp_code}"
