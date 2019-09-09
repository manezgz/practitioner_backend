from django.shortcuts import render
from rest_framework_mongoengine import generics
from .models import Accounts
from .serializers import AccountSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,DestroyModelMixin
from datetime import datetime, date

class AccountsList(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Accounts.objects.all()
    serializer_class = AccountSerializer
    def get_queryset(self):
        owner=None
        try:
            owner = self.kwargs['owner']
        except:
            ower=None;
        if owner !=None:
            return Accounts.objects.filter(owner=owner)
        else:
            return Accounts.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        data = request.data if request.data is not None else {}
        print("POST")
        data['creation_date']=datetime.now()
        #Chequear si podemos que exista el usuario
        return self.create(request, *args, **kwargs)


class AccountsSingle(ListModelMixin, CreateModelMixin, GenericAPIView,DestroyModelMixin):
    queryset = Accounts.objects.all()
    serializer_class = AccountSerializer
    lookup_field='iban'

    def get_object(self, queryset=None):
        iban = self.kwargs.get('iban')
        obj = Accounts.objects.get(iban=iban)
        return obj

    def delete(self, request, *args, **kwargs):
        print("DELETE")
        return self.destroy(request, *args, **kwargs)
