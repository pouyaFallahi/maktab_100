from django.db import models
import re
from django.core.exceptions import ValidationError


def phoneNumber_is_valid(phoneNumber=str) -> None:
    '''regix for check phone number users'''
    __regex = r'(-2|\+98)?([ ]|-|[()]){0,2}9[1|2|3|4]([ ]|-|[()]){0,2}(?:[0-9]([ ]|-|[()]){0,2}){8}'
    if not re.match(__regex, phoneNumber):
        raise ValidationError('phone number not valid')


class Users(models.Model):
    user_id = models.IntegerField(unique=True, primary_key=True, serialize=True)
    user_firsName = models.CharField(max_length=250, null=False, blank=False)
    user_lastName = models.CharField(max_length=250, null=False, blank=False)
    user_email = models.EmailField()
    user_phoneNumber = models.CharField(max_length=14, validators=[phoneNumber_is_valid])




