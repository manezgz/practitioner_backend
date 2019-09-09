from mongoengine import Document, EmbeddedDocument, fields,ListField

class Users(Document):
    cod = fields.StringField(required=True,unique=True)
    email = fields.StringField(required=True,unique=True,null=False,blank=False)
    password = fields.StringField(required=True, null=False,blank=False)
    last_name= fields.StringField(required=True, null=False,blank=False)
    first_name= fields.StringField(required=True, null=False,blank=False)
    mobile_phone=fields.StringField(required=False, null=False,blank=False)
    isAdmin=fields.BooleanField(required=False,null=False,blank=False)
    isActive=fields.BooleanField(required=False,null=False,blank=False)
    meta = {'strict': False}
