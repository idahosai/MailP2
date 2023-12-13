

from rest_framework import serializers
from .models import Contact, Customfeild, Segment, Staff, JoinStaffCustomfeild, JoinStaffContact, Attachedsegment, Email, Attachedemail, Inboxparticipants, Inbox

from django.contrib.auth.models import User



class Inboxparticipants2InboxSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='userid.id', read_only=True)
    lastmessage = serializers.CharField(source='userid.lastmessage', read_only=True)
    userid = serializers.IntegerField(source='userid.userid', read_only=True)
    
    class Meta:
        model = Inboxparticipants
        fields = (
        'id',
        'lastmessage',
        'userid',
        )


class User2Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username', 
            'first_name',
            'last_name',
            'email'
            )


class AttachedemailemailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='emailid.id', read_only=True)
    name = serializers.CharField(source='emailid.name', read_only=True)
    numberofcontactssentto = serializers.IntegerField(source='emailid.numberofcontactssentto', read_only=True)
    dateofcreation = serializers.DateTimeField(source='emailid.dateofcreation', read_only=True)
    subjecttitle = serializers.CharField(source='emailid.subjecttitle', read_only=True)
    opens = serializers.IntegerField(source='emailid.opens', read_only=True)
    
    
    class Meta:
        model = Attachedemail
        fields = (
        'id',
        'name',
        'numberofcontactssentto',
        'dateofcreation',
        'subjecttitle',
        'opens'
        )


class EmailSerializer(serializers.ModelSerializer):
    #staffpk = serializers.CharField(required=False)
    class Meta:
        model = Email
        fields = (
            #'staffpk',
            'id',
            'name',
            'numberofcontactssentto',
            'dateofcreation',
            'subjecttitle',
            'opens'
        )


class GetIsRegisteredEmailApisSerializer(serializers.ModelSerializer):
    #put in a "," if it's just 1 feild to allow it
    class Meta:
        model = Contact
        fields = (
            'emailaddress',
        )


class Staff2Serializer(serializers.ModelSerializer):
    #these are the post the show up below in the screen
    #it doesn't send the password on send
    password = serializers.CharField(required=False)
    class Meta:
        model = Staff
        fields = (
            'userid',
            'username',
            'firstname',
            'lastname',
            'emailaddress',
            'password',
            'industry'       
            )

class Staff3Serializer(serializers.ModelSerializer):
    #these are the post the show up below in the screen
    #it doesn't send the password on send
    id = serializers.CharField(required=False)
    class Meta:
        model = Staff
        fields = (
            'userid',
            'username',
            'firstname',
            'lastname',
            'emailaddress',
            'id',
            'industry'       
            )


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
    staffpk = serializers.CharField(required=False)
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



class AttachedsegmentSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='segmentid.id', read_only=True)
    name = serializers.CharField(source='segmentid.name', read_only=True)
    dateone = serializers.DateTimeField(source='segmentid.dateone', read_only=True)
    datetwo = serializers.DateTimeField(source='segmentid.datetwo', read_only=True)
    dateofcreation = serializers.DateTimeField(source='segmentid.dateofcreation', read_only=True)
    
    staffpk = serializers.CharField(required=False)
    class Meta:
        model = Attachedsegment
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
