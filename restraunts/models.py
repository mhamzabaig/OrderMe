from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class restraunt(models.Model):
    # Id will be defaulted primary key
    name = models.TextField(max_length=50)
    reg_id = models.TextField(max_length=50)
    contact_no = models.IntegerField(blank=True,null=True)
    email_id = models.TextField(max_length=50,blank=False,null=True)

    res_owner = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
