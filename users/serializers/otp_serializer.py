from rest_framework import serializers

class OTPSerializer(serializers.Serializer):
    """OTP kodini tekshirish uchun serializer."""
    email = serializers.EmailField()
    otp_code = serializers.CharField(max_length=6)
