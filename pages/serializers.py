

from rest_framework import serializers
from .models import Contact, Customfeild, Segment, Staff, JoinStaffCustomfeild

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = (
            'id',
            'userid',
            'username',
            'firstname',
            'lastname',
            'emailaddress',
            'industry'       
            )





class JoinStaffCustomfeildSerializer(serializers.ModelSerializer):
    #customfeildid__id = models.ForeignKey(Customfeild, on_delete=models.CASCADE, null=True)
    #this gives the whole bunch
    id = serializers.CharField(source='customfeildid.id', read_only=True)
    name = serializers.CharField(source='customfeildid.name', read_only=True)
    customfeildintvalue = serializers.IntegerField(source='customfeildid.customfeildintvalue', read_only=True)
    customfeildstringvalue = serializers.CharField(source='customfeildid.customfeildstringvalue', read_only=True)
    dateofcreation = serializers.DateTimeField(source='customfeildid.dateofcreation', read_only=True)
    lastcustomfeildupdate = serializers.DateTimeField(source='customfeildid.lastcustomfeildupdate', read_only=True)
    #idd = serializers.SlugRelatedField(read_only=True,slug_field="id")
    #name = serializers.SlugRelatedField(read_only=True,slug_field="name")
    #customfeildintvalue = serializers.SlugRelatedField(read_only=True,slug_field="customfeildintvalue")
    #customfeildstringvalue = serializers.SlugRelatedField(read_only=True,slug_field="customfeildstringvalue")
    #dateofcreation = serializers.SlugRelatedField(read_only=True,slug_field="dateofcreation")
    #lastcustomfeildupdate = serializers.SlugRelatedField(read_only=True,slug_field="lastcustomfeildupdate")
    
    
    
    #i need to check to see if the below code is correct data type
    #id = serializers.CharField(source='customfeildid.id')
    #name = serializers.CharField(source='customfeildid')
    #customfeildintvalue = serializers.IntegerField(source='customfeildid')
    #customfeildstringvalue = serializers.CharField(source='customfeildid')
    #dateofcreation = serializers.DateTimeField(source='customfeildid')
    #lastcustomfeildupdate = serializers.DateTimeField(source='customfeildid')
    
    #customfeildid__name = serializers.CharField()
    #customfeildid__customfeildintvalue = serializers.CharField()
    
    class Meta:
        model = JoinStaffCustomfeild
        fields = (
            'id',
            'name',
            'customfeildintvalue',
            'customfeildstringvalue',
            'dateofcreation',
            'lastcustomfeildupdate'
       
            )








class CreateContactSerializer(serializers.ModelSerializer):
    staffpk = serializers.CharField(required=False)
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
        'addmethod',
        'staffpk'
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
    staffpk = serializers.CharField(required=False)
    class Meta:
        model = Customfeild
        fields = (
        'id',
        'name',
        'customfeildintvalue',
        'customfeildstringvalue',
        'dateofcreation',
        'lastcustomfeildupdate',
        'staffpk'
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
