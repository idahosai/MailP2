

from rest_framework import serializers
from .models import Contact, Customfeild, Segment, Staff, JoinStaffCustomfeild, JoinStaffContact

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


class JoinStaffContactSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='contactid.id', read_only=True)
    status = serializers.CharField(source='contactid.status', read_only=True)
    lifetimevalue = serializers.IntegerField(source='contactid.lifetimevalue', read_only=True)
    datejoined = serializers.CharField(source='contactid.datejoined', read_only=True)
    notes = serializers.DateTimeField(source='contactid.notes', read_only=True)
    emailaddress = serializers.DateTimeField(source='contactid.emailaddress', read_only=True)
    firstname = serializers.DateTimeField(source='contactid.firstname', read_only=True)
    lastname = serializers.DateTimeField(source='contactid.lastname', read_only=True)
    jobtitle = serializers.DateTimeField(source='contactid.jobtitle', read_only=True)
    company = serializers.DateTimeField(source='contactid.company', read_only=True)
    mobilephone = serializers.DateTimeField(source='contactid.mobilephone', read_only=True)
    workphone = serializers.DateTimeField(source='contactid.workphone', read_only=True)
    country = serializers.DateTimeField(source='contactid.country', read_only=True)
    stateprovince = serializers.DateTimeField(source='contactid.stateprovince', read_only=True)
    city = serializers.DateTimeField(source='contactid.city', read_only=True)
    address = serializers.DateTimeField(source='contactid.address', read_only=True)
    zip = serializers.DateTimeField(source='contactid.zip', read_only=True)
    website = serializers.DateTimeField(source='contactid.website', read_only=True)
    stopmethod = serializers.DateTimeField(source='contactid.stopmethod', read_only=True)
    confirmquestionmark = serializers.DateTimeField(source='contactid.confirmquestionmark', read_only=True)
    addmethod = serializers.DateTimeField(source='contactid.addmethod', read_only=True)
    signupsource = serializers.DateTimeField(source='contactid.signupsource', read_only=True)
    totalreviewsleft = serializers.DateTimeField(source='contactid.totalreviewsleft', read_only=True)
    lastemailratingdone = serializers.DateTimeField(source='contactid.lastemailratingdone', read_only=True)

    class Meta:
        model = JoinStaffContact
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


class ShowSegmentSerializer(serializers.ModelSerializer):
    staffpk = serializers.CharField(required=False)
    class Meta:
        model = Segment
        #what the get will display
        fields = (
        'dateone',
        'datetwo',
        'staffpk'
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
    staffpk = serializers.IntegerField(required=False)
    class Meta:
        model = Segment
        #what the get will display
        fields = (
        'id',
        'name',
        'dateone',
        'datetwo',
        'dateofcreation',
        'staffpk'
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
