# DRF Blog Platform

## Loyiha haqida
Ushbu loyiha blog postlarini boshqarish, multimedia kontentlarini qo‘shish, va foydalanuvchilar bilan muloqot qilish imkoniyatini beradi. Loyihada SOLID tamoyillari va turli dizayn patternlar qo‘llangan.

---

## Funksionallik
- **Maqolalar tizimi**: Turli maqola turlari (oddiy, texnik) bilan ishlash.
- **Multimedia kontent**: Video, audio va rasm qo‘llab-quvvatlanadi.
- **Foydalanuvchilar**: Ro‘yxatdan o‘tish va OTP orqali autentifikatsiya.
- **Izohlar**: Maqolalarga izoh qoldirish va ko‘rish.
- **Kategoryalar**: Maqolalarga kategroiya qoshiosh va kategriya boyicha olish.
- **Tag**: Maqolalarga tag qoshish va teg boyicha olish.
- **Qidiruv**: Maqola va kontentlar bo‘yicha qidiruv.
- **Paginatsiya va filtering**: Maqolada paginatsiya va filtering boyicha amalga oshirilgan.


## Ishga tushirish
1. Virtual muhitni sozlash:
    ```
    python -m venv env
    env\Scripts\activate     # Windows
    ```

2. Kutubxonalarni o‘rnatish:
    ```
    pip install -r requirements.txt
    ```

3. Migratsiyalarni ishga tushirish:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Lokal serverni ishga tushirish:
    ```
    python manage.py runserver
    ```

---

## API Endpointlar

### Foydalanuvchilar
- **Ro‘yxatdan o‘tish**: `POST /api/users/register/`
- **OTP tasdiqlash**: `POST /api/users/verify-otp/`
- **Tizimga kirish**: `POST /api/users/login/`

### Maqolalar
- **Maqolalar ro‘yxati**: `GET /api/articles/`
- **Maqola yaratish**: `POST /api/articles/`

- **Taglar royxatini olish**: `GET /api/tag/`
-  **Taglar yaratish uchun**: `POST /api/tag/`

- **Yangi kategoriya yaratish**: `POST /api/category/`
- **Kategorylaral royxatini olish**: `GET /api/category/`

### Izohlar
- **Izoh qo‘shish**: `POST /api/comments/`

### Qidiruv
- **Qidiruv**: `GET /api/search/`

---

## Dizayn Patternlar
1. **Factory Method**: Maqolalar turlari uchun.
2. **Abstract Factory**: Multimedia turlari uchun.
3. **Singleton**: Konfiguratsiya boshqaruvi uchun.

---

## Hujjatlar
API hujjatlarini Swagger orqali ko‘rishingiz mumkin:
```
http://127.0.0.1:8000/swagger/
