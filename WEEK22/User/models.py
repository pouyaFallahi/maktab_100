from django.db import models
import re
from django.core.validators import ValidationError, RegexValidator


# def phoneNumber_is_valid(phoneNumber=str) -> None:
#     ''' regix for check phone number users '''
#     __regex = r'^\+98\s?(\d{2})\s?(\d{4})-(\d{4})$'
#     if not re.match(__regex, phoneNumber):
#         raise ValidationError('phone number not valid')


class Users(models.Model):
    user_id = models.IntegerField(unique=True, primary_key=True, serialize=True)
    user_firsName = models.CharField(max_length=250, null=False, blank=False)
    user_lastName = models.CharField(max_length=250, null=False, blank=False)
    user_email = models.EmailField()
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




