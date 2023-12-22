from django.conf import settings
from django.contrib.auth.models import UserManager, AbstractUser, Group, Permission
from realEstateApp.models import Property
from django.db import models

class CustomUserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        extra_fields.setdefault('username', uuid.uuid4().hex)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    email = models.EmailField(verbose_name='email',max_length=255, unique=True)
    profile_photo = models.ImageField(upload_to='images', null=True, blank=True)
    favorite_properties = models.ManyToManyField(Property, related_name='custom_user_favorite_properties', blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",
        blank=True,
        help_text='The groups this user belongs to.'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True,
        help_text='Specific permissions for this user.'
    )

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email

class UserFavorites(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='custom_user_favorite_property')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_favorites')
    
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.property.title} - {self.user.email}"
