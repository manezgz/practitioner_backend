from django.shortcuts import render

from django.shortcuts import render
from rest_framework_mongoengine import generics
from .models import Transactions
from .serializers import TransactionSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,DestroyModelMixin
from datetime import datetime, date
from accounts.models import Accounts
from rest_framework.exceptions import ValidationError

class TransactionList(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        iban = self.kwargs.get('iban')
        print(iban)
        return Transactions.objects.filter(iban=iban).order_by('-value_date')

    def get(self, request, *args, **kwargs):

        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        data = request.data if request.data is not None else {}
        data['value_date']=datetime.now()
        print("POST")
        obj = Accounts.objects.get(iban=data['iban'])
        balance=obj.balance
        value=float(data['value'])
        float(value)
        data['balance_ini']=balance

        if data['type']=='REINTEGRO':
            if balance-value>=0:
                obj.balance=balance-value
                obj.save()
            else:
                #No dejamos hacer
                raise ValidationError('Balance not enough')
        elif data['type']=='INGRESO':
            obj.balance=balance+value
            obj.save()
        data['balance_fin']=obj.balance
        #Chequear si podemos que exista el usuario

        return self.create(request, *args, **kwargs)
