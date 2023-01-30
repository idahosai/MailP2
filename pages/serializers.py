

from rest_framework import serializers
from .models import Contact

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