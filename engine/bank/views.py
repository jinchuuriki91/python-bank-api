from collections import OrderedDict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import ListAPIView
from engine.bank.models import BankInfo
from engine.bank.serializers import BankInfoSerializer


@api_view()
def get_bank_detail(request, ifsc_code):
    bank = BankInfo.objects.get_bank(ifsc_code)
    if bank:
        ser = BankInfoSerializer(bank)
        return Response({
            "status": "success",
            "results": ser.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            "status": "error",
            "message": "Bank with given ifsc code not found"
        }, status=status.HTTP_404_NOT_FOUND)


class GetBankBranches(ListAPIView):

    serializer_class = BankInfoSerializer
    pagination_class = LimitOffsetPagination

    def get(self, request):
        queryset = BankInfo.objects.get_branches(
            bank_name=request.query_params.get("bank_name", ""),
            city=request.query_params.get("city", "")
        )
        page = self.paginate_queryset(queryset)
        if page:
            ser = self.get_serializer(page, many=True)
            return self.get_paginated_response(ser.data)
        ser = self.get_serializer(queryset, many=True)
        return Response({
            "status": "success",
            "results": ser.data
        }, status=status.HTTP_200_OK)
