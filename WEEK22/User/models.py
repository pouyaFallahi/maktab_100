from django.db import models
import re
from django.core.validators import ValidationError, RegexValidator


class Users(models.Model):
    user_id = models.IntegerField(unique=True, primary_key=True, serialize=True)
    user_firsName = models.CharField(max_length=250, null=False, blank=False)
    user_lastName = models.CharField(max_length=250, null=False, blank=False)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=100, null=False, blank=False)
    user_phoneNumber = models.CharField(
        max_length=15,  # Assuming the maximum length for the phone number
        validators=[
            RegexValidator(
                regex=r'^[\+98 | 09 ]\s?(\d{2})\s?(\d{4})(\d{4})$',
                message='Enter a valid Iranian phone number.'
            ),
        ],
    )

    def __str__(self):
        return f'{self.user_firsName} - {self.user_lastName}'




