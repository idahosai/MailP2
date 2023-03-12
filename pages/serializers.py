

from rest_framework import serializers
from .models import Contact, Customfeild, Segment

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

    
class CreateCustomfeild2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customfeild
        fields = (
        'id',
        'name',
        'customfeildintvalue',
        'customfeildstringvalue',
        'dateofcreation',
        'lastcustomfeildupdate',
        )


class CreateContact2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
        'id',
        'status',
        'lifetimevalue',

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

        'stopmethod',
        'confirmquestionmark',
        'addmethod',
        'signupsource',
        'totalreviewsleft',
        'lastemailratingdone'
        )



class CreateSegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        #what the get will display
        fields = (
        'id',
        'name',
        'dateone',
        'datetwo',
        'dateofcreation'
        )



class CreateContactEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
        'id',
        'status',
        'lifetimevalue',

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

        'stopmethod',
        'confirmquestionmark',
        'addmethod',
        'signupsource',
        'totalreviewsleft',
        'lastemailratingdone'
        )
