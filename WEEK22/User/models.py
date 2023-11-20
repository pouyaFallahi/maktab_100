from django.db import models
import re

class User(models.Model):
    def phoneNumber_is_valid(self):
       __regex = r'(0|\+98)?([ ]|-|[()]){0,2}9[1|2|3|4]([ ]|-|[()]){0,2}(?:[0-9]([ ]|-|[()]){0,2}){8}'
       check_phone = re.match(__regex, self.user_phoneNumber)
       if check_phone:
           return True
       return False

    user_id = models.IntegerField(unique=True, primary_key= True, serialize=True)
    user_firsName = models.CharField(max_length=250, null=False, blank=False)
    user_lastName = models.CharField(max_length=250, null=False, blank=False)
    user_email = models.EmailField()
    user_phoneNumber = models.CharField(max_length=14)
    if phoneNumber_is_valid:
        pass
    else:
        raise ValueError('chek your phone number')

