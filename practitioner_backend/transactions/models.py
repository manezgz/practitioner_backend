from django.db import models
from mongoengine import Document, EmbeddedDocument, fields,ListField
from datetime import datetime, date

class Transactions(Document):
    value_date=fields.DateTimeField(required=True, null=True,default=datetime.now())
    iban=fields.StringField(required=True, null=True)
    value=fields.FloatField(required=True, null=True)
    type=fields.StringField(required=True, null=True)
    balance_ini=fields.FloatField(required=True, null=True)
    balance_fin=fields.FloatField(required=True, null=True)
