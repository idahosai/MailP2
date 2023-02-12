

from rest_framework import serializers
from .models import Contact, Customfeild

class CreateContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
        'datejoined',
        'notes',
        'emailaddress',
        'firstname',
        'lastname',
        'jobtitle',
        'company',
        'mobilephone',
        'workphone',
        'country',
        'stateprovince',
        'city',
        'address',
        'zip',
        'website',
        'addmethod'
        )

class CreateCustomfeildSerializer(serializers.ModelSerializer):
    contactpk = serializers.CharField(required=False)
    staffpk = serializers.CharField(required=False)
    class Meta:
        model = Customfeild
        fields = (
        'contactpk',
        'name',
        'customfeildintvalue',
        'customfeildstringvalue',
        'dateofcreation',
        'lastcustomfeildupdate',
        'staffpk'
        )