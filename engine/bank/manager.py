from django.db import models


class BankInfoManager(models.Manager):

    def get_bank(self, ifsc_code):
        try:
            return self.get(ifsc=ifsc_code)
        except self.model.DoesNotExist:
            return None

    def get_branches(self, bank_name="", city=""):
        kwargs = {}
        if bank_name:
            kwargs["bank_name__iexact"] = bank_name
        if city:
            kwargs["city__iexact"] = city
        return self.filter(**kwargs)
