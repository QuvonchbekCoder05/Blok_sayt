from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from django.utils.timezone import now, timedelta
from django.contrib.auth import authenticate
from users.models.user import User
from users.models.otp import OTP
from users.serializers.user_serializer import UserSerializer
from users.serializers.otp_serializer import OTPSerializer
from rest_framework.permissions import AllowAny

class RegisterView(APIView):
    """
    Foydalanuvchini ro'yxatdan o'tkazish.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Foydalanuvchini yaratish
            email = serializer.validated_data.get('email')
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            user = User.objects.create_user(email=email, username=username, password=password)
            user.is_active = False  # Hisob faolligini vaqtinchalik o'chirish
            user.save()

            # OTP generatsiya qilish
            otp_code = OTP.generate_otp_code()  # Har bir model uchun alohida generate funksiyasi mavjud
            expires_at = now() + timedelta(minutes=10)
            OTP.objects.create(user=user, otp_code=otp_code, expires_at=expires_at)

            # Email yuborish
            send_mail(
                'Tasdiqlash kodi',
                f"Sizning tasdiqlash kodingiz: {otp_code}",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

            return Response({"detail": "Ro'yxatdan muvaffaqiyatli o'tdingiz. Emailingizni tasdiqlang."},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(APIView):
    """
    Foydalanuvchi OTP tasdiqlash.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp_code = serializer.validated_data['otp_code']
            try:
                otp = OTP.objects.get(user__email=email, otp_code=otp_code)
                if otp.is_valid():  # Tugash muddatini tekshirish
                    otp.user.is_active = True  # Hisobni faollashtirish
                    otp.user.save()
                    otp.delete()  # OTP ni o'chirish xavfsizlik uchun
                    return Response({"detail": "OTP tasdiqlandi, hisob faollashtirildi."},
                                    status=status.HTTP_200_OK)
                return Response({"detail": "OTP muddati o'tgan."}, status=status.HTTP_400_BAD_REQUEST)
            except OTP.DoesNotExist:
                return Response({"detail": "Noto'g'ri OTP yoki email."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    Foydalanuvchini tizimga kiritish.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)

        if user and user.is_active:
            # Login muvaffaqiyatli
            send_mail(
                'Tizimga kirish muvaffaqiyatli',
                'Siz tizimga muvaffaqiyatli kirdingiz.',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return Response({
                "detail": "Tizimga muvaffaqiyatli kirdingiz.",
                "token": user.generate_access_token()  # Tokenni generatsiya qilish
            }, status=status.HTTP_200_OK)
        return Response({"detail": "Login yoki parol xato yoki hisob faollashtirilmagan."},
                        status=status.HTTP_401_UNAUTHORIZED)
