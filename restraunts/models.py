from django.db import models

# Create your models here.

class restraunt(models.Model):
    # Id will be defaulted primary key
    name = models.TextField(max_length=50)
    reg_id = models.TextField(max_length=50)
    contact_no = models.IntegerField
    email_id = models.TextField

