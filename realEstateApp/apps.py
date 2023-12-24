from django.apps import AppConfig


class RealestateappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "realEstateApp"
class UserAppConfig(AppConfig):
    name = 'user'

    def ready(self):
        import user.signals  
