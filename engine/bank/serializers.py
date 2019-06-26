from rest_framework import serializers
from engine.bank.models import BankInfo


class BankInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankInfo
        fields = (
            "ifsc", "bank_id", "branch", "address", "city",
            "district", "state", "bank_name")
