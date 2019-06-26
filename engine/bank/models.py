from django.db import models
from engine.bank.manager import BankInfoManager


class BankInfo(models.Model):

    ifsc = models.CharField(max_length=11, null=False)
    bank_id = models.PositiveIntegerField(null=False)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)
    bank_name = models.CharField(max_length=49)

    objects = BankInfoManager()

    def __str__(self):
        return "%s (%s)" % (self.bank_name, self.ifsc)
