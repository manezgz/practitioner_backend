from mongoengine import Document, EmbeddedDocument, fields,ListField


class Accounts(Document):
    iban = fields.StringField(required=True,unique=True)
    owner = fields.StringField(required=True)
    creation_date= fields.DateTimeField(required=True, null=False)
    balance=fields.FloatField(required=True)
    meta = {'strict': False}
