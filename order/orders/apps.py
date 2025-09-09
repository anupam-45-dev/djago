# orders/apps.py

from django.apps import AppConfig

class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'  # ← Ye exactly aapke folder ke naam ke hisab se hona chahiye

