from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Apps(models.Model):
    WEB = 'web'
    MOBILE = 'mobile'
    DJANGO = 'django'
    REACT_NATIVE = 'react native'

    TYPE_CHOICES = (
        (WEB, 'Web'),
        (MOBILE, 'Mobile')
    )

    FRAMEWORK_CHOICES = (
        (DJANGO, 'Django'),
        (REACT_NATIVE, 'React Native')
    )
       
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(choices=TYPE_CHOICES, default=WEB, max_length=10)
    framework = models.CharField(
        choices=FRAMEWORK_CHOICES,
        default=DJANGO,
        max_length=20
    )
    domain_name = models.CharField(max_length=50, null=True, blank=True)
    screenshot = models.ImageField(
        default='app/screenshots/default.jpg',
        upload_to="app/screenshot/default.jpg"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
