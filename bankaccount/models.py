from django.db import models

class Account(models.Model):
    bvn = models.BigIntegerField()
    name = models.CharField(max_length=255)
    account_number = models.BigIntegerField()
    balance = models.FloatField()
    date_of_birth = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.name


