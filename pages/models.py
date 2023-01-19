from django.db import models


class StaffManager(models.Manager):
    def get_by_natural_key(self, id, userid, username, firstname, lastname, emailaddress, industry):
        return self.get(id = id, userid=userid, username=username, firstname=firstname, lastname=lastname, emailaddress=emailaddress, industry=industry)

class Staff(models.Model):
    id = models.IntegerField(default=1, primary_key=True)
    userid = models.IntegerField()
    username = models.CharField(max_length=70)
    firstname = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)
    emailaddress = models.CharField(max_length=70)
    industry = models.CharField(max_length=70)


    #This method should always return a natural key tuple 
    #Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):              #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate
        #made this dictionary return whitch will add to the previous dictionary
        return {'id':self.id,'userid': self.userid, 'username': self.username, 'firstname': self.firstname, 'lastname': self.lastname, 'emailaddress': self.emailaddress, 'firstname': self.industry}
    #naturalkey has you app name then the Object
    #natural_key.dependencies = ['myapp.Person']

    def __str__(self):
        return self.id



# Create your models here.
class ContactManager(models.Manager):
    def get_by_natural_key(self, id, status, lifetimevalue, datejoined, notes, emailaddress, firstname, lastname, jobtitle, company, mobilephone, workphone, country, stateprovince, city, address, zip, website, stopmethod, confirmquestionmark, addmethod, signupsource, totalreviewsleft, lastemailratingdone, staffid):
        return self.get(id = id, status=status, lifetimevalue = lifetimevalue, datejoined= datejoined,notes=notes, emailaddress=emailaddress, firstname=firstname, lastname =lastname, jobtitle=jobtitle, company=company, mobilephone = mobilephone, workphone=workphone, country=country, stateprovince=stateprovince, city=city, address=address, zip=zip, website=website, stopmethod=stopmethod, confirmquestionmark=confirmquestionmark, addmethod=addmethod, signupsource=signupsource, totalreviewsleft=totalreviewsleft, lastemailratingdone=lastemailratingdone, staffid=staffid)
class Contact(models.Model):
    id = models.IntegerField(default=1, primary_key=True)
    status = models.CharField(max_length=70)
    lifetimevalue = models.DecimalField(max_digits=5, decimal_places=2)
    datejoined = models.DateTimeField(null=True, blank=False)
    notes = models.CharField(max_length=70)
    emailaddress = models.CharField(max_length=70)
    firstname = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)
    jobtitle = models.CharField(max_length=70)
    company = models.CharField(max_length=70)
    mobilephone = models.CharField(max_length=70)
    workphone = models.CharField(max_length=70)
    country = models.CharField(max_length=70)
    stateprovince = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    address = models.CharField(max_length=70)
    zip = models.CharField(max_length=70)
    website = models.CharField(max_length=70)
    stopmethod = models.CharField(max_length=70)
    confirmquestionmark = models.CharField(max_length=70)
    addmethod = models.CharField(max_length=70)
    signupsource = models.CharField(max_length=70)
    totalreviewsleft = models.CharField(max_length=70)
    lastemailratingdone = models.CharField(max_length=70)

    staffid = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    #bulkimportid = models.ForeignKey(Bulkimport, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.id
    #This method should always return a natural key tuple 
    #Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):              #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate
        #made this dictionary return whitch will add to the previous dictionary
        return {'id':self.id,'status': self.status,'lifetimevalue':self.lifetimevalue, 'datejoined':self.datejoined, 'notes': self.notes, 'emailaddress': self.emailaddress, 'firstname':self.firstname, 'lastname': self.lastname, 'jobtitle':self.jobtitle, 'company': self.company , 'mobilephone': self.mobilephone, 'workphone':self.workphone, 'country':self.country, 'stateprovince': self.stateprovince, 'city':self.city, 'address':self.address, 'zip': self.zip, 'website':self.website, 'stopmethod': self.stopmethod, 'confirmquestionmark': self.confirmquestionmark, 'addmethod':self.addmethod, 'signupsource': self.signupsource, 'totalreviewsleft': self.totalreviewsleft, 'lastemailratingdone':self.lastemailratingdone, 'staffid':self.staffid}
    natural_key.dependencies = ['pages.Staff']
    #natural_key.dependencies = ['pages.Staff', 'pages.Bulkimport']



class TagManager(models.Manager):
    def get_by_natural_key(self, id, name, dateofcreation, type):
        return self.get(id = id, name=name, dateofcreation=dateofcreation, type=type)
    #def get_by_natural_key(self, name, dateofcreation):
    #    return self.get(name=name, dateofcreation=dateofcreation)
class Tag(models.Model):
    #this alone works to get it to auto increment, dont add other parameter like default or it will stop it from working
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70,default=' ')
    dateofcreation = models.DateTimeField(null=True, blank=False)
    type = models.CharField(max_length=70,default=' ')

        #metadata is “anything that’s not a field
    class Meta:                   #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate 
        #this is what is actually group in the serialized object's feild column for the specific feild foreighn key attribute
        #Sets of field names that, taken together, must be unique:
        #unique_together can be a single list when dealing with a single set of fields:
        unique_together = ['id', 'name', 'dateofcreation', 'type']
    def __str__(self):
        return str(self.id)
        #return self.name
    #This method should always return a natural key tuple 
    #Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):              #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate
        #made this dictionary return whitch will add to the previous dictionary
        return {'id':self.id, 'name': self.name, 'dateofcreation': self.dateofcreation, 'type':self.type}
        #return {'name': self.name, 'dateofcreation': self.dateofcreation}
    
class AttachedtagManager(models.Manager):
    def get_by_natural_key(self, id, dateofattachement, contactid, tagid):
        return self.get(id = id, dateofattachement=dateofattachement, contactid=contactid, tagid=tagid)
    #def get_by_natural_key(self, dateofattachement, contactid, tagid):
    #    return self.get(dateofattachement=dateofattachement, contactid=contactid, tagid=tagid)
class Attachedtag(models.Model):
    id = models.AutoField(primary_key=True)
    dateofattachement = models.DateTimeField(null=True, blank=False)
    contactid = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)
    tagid = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    #metadata is “anything that’s not a field
    class Meta:                   #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate 
        #this is what is actually group in the serialized object's feild column for the specific feild foreighn key attribute
        #Sets of field names that, taken together, must be unique:
        #unique_together can be a single list when dealing with a single set of fields:
        unique_together = ['id', 'dateofattachement', 'contactid', 'tagid']
    def __str__(self):
        #return self.id
        return str(self.id)
    #This method should always return a natural key tuple 
    #Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):              #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate
        #made this dictionary return whitch will add to the previous dictionary
        return {'id':self.id,'dateofattachement': self.dateofattachement, 'contactid': self.contactid, 'tagid': self.tagid}
        #return {'dateofattachement': self.dateofattachement, 'contactid': self.contactid, 'tagid': self.tagid}
    
    #naturalkey has you app name then the Object
    natural_key.dependencies = ['pages.Contact', 'pages.Tag']




class CustomfeildManager(models.Manager):
    def get_by_natural_key(self, id, name,customfeildintvalue, customfeildstringvalue, dateofcreation, lastcustomfeildupdate):
        return self.get(id = id, name = name, customfeildintvalue = customfeildintvalue, customfeildstringvalue = customfeildstringvalue,dateofcreation=dateofcreation, lastcustomfeildupdate = lastcustomfeildupdate)
class Customfeild(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    customfeildintvalue =  models.IntegerField()
    customfeildstringvalue = models.CharField(max_length=70)
    dateofcreation = models.DateTimeField(null=True, blank=False)
    lastcustomfeildupdate = models.DateTimeField(null=True, blank=False)
    def __str__(self):
        return str(self.id)
    #This method should always return a natural key tuple 
    #Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):              #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate
        #made this dictionary return whitch will add to the previous dictionary
        return {'id':self.id,'name': self.name,'customfeildintvalue':self.customfeildintvalue, 'customfeildstringvalue':self.customfeildstringvalue, 'dateofcreation': self.dateofcreation, 'lastcustomfeildupdate': self.lastcustomfeildupdate}
    


class AttachedcustomfeildManager(models.Manager):
    def get_by_natural_key(self, id, dateofattachement, contactid, customfeildid):
        return self.get(id = id, dateofattachement=dateofattachement, contactid=contactid, customfeildid=customfeildid)
class Attachedcustomfeild(models.Model):
    id = models.AutoField(primary_key=True)
    dateofattachement = models.DateTimeField(null=True, blank=False)
    contactid = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)
    customfeildid = models.ForeignKey(Customfeild, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.id)
    #This method should always return a natural key tuple 
    #Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):              #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate
        #made this dictionary return whitch will add to the previous dictionary
        return {'id':self.id,'dateofattachement': self.dateofattachement, 'contactid': self.contactid, 'customfeildid': self.customfeildid}
    #naturalkey has you app name then the Object
    natural_key.dependencies = ['pages.Contact', 'pages.Customfeild']





class GroupManager(models.Manager):
    def get_by_natural_key(self, id, name, dateofcreation, type, numberofsubscribes, numberofunsubscribes, totalsubscribes):
        return self.get(id = id, name=name, dateofcreation=dateofcreation, type=type, numberofsubscribes=numberofsubscribes, numberofunsubscribes=numberofunsubscribes, totalsubscribes=totalsubscribes)
class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    dateofcreation = models.DateTimeField(null=True, blank=False)
    type =  models.CharField(max_length=70)
    numberofsubscribes = models.IntegerField(blank=True,null=True)
    numberofunsubscribes = models.IntegerField(blank=True,null=True)
    totalsubscribes = models.IntegerField(blank=True,null=True)
        #metadata is “anything that’s not a field
    class Meta:                   #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate 
        #this is what is actually group in the serialized object's feild column for the specific feild foreighn key attribute
        #Sets of field names that, taken together, must be unique:
        #unique_together can be a single list when dealing with a single set of fields:
        unique_together = ['id', 'name','dateofcreation','type', 'numberofsubscribes','numberofunsubscribes', 'totalsubscribes']
    def __str__(self):
        return str(self.id)
    #This method should always return a natural key tuple 
    #Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):              #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate
        #made this dictionary return whitch will add to the previous dictionary
        return {'id':self.id,'name': self.name, 'dateofcreation': self.dateofcreation, 'type': self.type, 'numberofsubscribes': self.numberofsubscribes, 'numberofunsubscribes': self.numberofunsubscribes, 'totalsubscribes': self.totalsubscribes}
    

class AttachedgroupManager(models.Manager):
    def get_by_natural_key(self, id, dateofattachement, contactid, groupid):
        return self.get(id = id, dateofattachement=dateofattachement, contactid=contactid, groupid=groupid)
class Attachedgroup(models.Model):
    id = models.AutoField(primary_key=True)
    dateofattachement = models.DateTimeField(null=True, blank=False)
    contactid = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)
    groupid = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
            #metadata is “anything that’s not a field
    class Meta:                   #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate 
        #this is what is actually group in the serialized object's feild column for the specific feild foreighn key attribute
        #Sets of field names that, taken together, must be unique:
        #unique_together can be a single list when dealing with a single set of fields:
        unique_together = ['id', 'dateofattachement','contactid', 'groupid']
    def __str__(self):
        return str(self.id)
    #This method should always return a natural key tuple 
    #Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):              #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate
        #made this dictionary return whitch will add to the previous dictionary
        return {'id':self.id,'dateofattachement': self.dateofattachement, 'contactid': self.contactid, 'groupid': self.groupid}
    #naturalkey has you app name then the Object
    natural_key.dependencies = ['pages.Contact', 'pages.Group']









class FormManager(models.Manager):
    def get_by_natural_key(self, id, name, dateofcreation, status, numberofsubscribes, totalsubscribes):
        return self.get(id = id, name=name, dateofcreation=dateofcreation, status=status, numberofsubscribes=numberofsubscribes, totalsubscribes=totalsubscribes)
class Form(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    dateofcreation = models.DateTimeField(null=True, blank=False)
    status =  models.CharField(max_length=70)
    numberofsubscribes = models.IntegerField(blank=True,null=True)
    totalsubscribes = models.IntegerField(blank=True,null=True)
    class Meta:                   #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate 
        #this is what is actually group in the serialized object's feild column for the specific feild foreighn key attribute
        #Sets of field names that, taken together, must be unique:
        #unique_together can be a single list when dealing with a single set of fields:
        unique_together = ['id', 'name','dateofcreation','status', 'numberofsubscribes','totalsubscribes']
    def __str__(self):
        return str(self.id)
    #This method should always return a natural key tuple 
    #Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):              #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate
        #made this dictionary return whitch will add to the previous dictionary
        return {'id':self.id,'name': self.name, 'dateofcreation': self.dateofcreation, 'status': self.status, 'numberofsubscribes': self.numberofsubscribes, 'totalsubscribes': self.totalsubscribes}
    
    




class AttachedFormManager(models.Manager):
    def get_by_natural_key(self, id, dateofattachement, username, firstname, lastname, emailaddress, industry):
        return self.get(id = id, dateofattachement=dateofattachement, username=username, firstname=firstname, lastname=lastname, emailaddress=emailaddress, industry=industry)
class AttachedForm(models.Model):
    id = models.AutoField(primary_key=True)
    dateofattachement = models.DateTimeField(null=True, blank=False)
    contactid = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)
    formid = models.ForeignKey(Form, on_delete=models.CASCADE, null=True)
    class Meta:                   #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate 
        #this is what is actually group in the serialized object's feild column for the specific feild foreighn key attribute
        #Sets of field names that, taken together, must be unique:
        #unique_together can be a single list when dealing with a single set of fields:
        unique_together = ['id', 'dateofattachement','contactid', 'formid']
    def __str__(self):
        return str(self.id)
    #This method should always return a natural key tuple 
    #Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):              #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate
        #made this dictionary return whitch will add to the previous dictionary
        return {'id':self.id,'dateofattachement': self.dateofattachement, 'contactid': self.contactid, 'formid': self.formid}
    #naturalkey has you app name then the Object
    natural_key.dependencies = ['pages.Contact', 'pages.Form']





class BulkimportManager(models.Manager):
    def get_by_natural_key(self, id, importlocation, details, status, datetime, whatshouldwedo, notifywhenreviewcompleted, notifywhenreviewcompletedyesbox, howsubscribersacquired, howsubscribersacquiredotherbox, anotheremailprovider, anotheremailprovideryesdropdown, filename, staffid):
        return self.get(id = id, importlocation=importlocation, details = details, status= status,datetime=datetime, whatshouldwedo=whatshouldwedo, notifywhenreviewcompleted=notifywhenreviewcompleted, notifywhenreviewcompletedyesbox=notifywhenreviewcompletedyesbox, howsubscribersacquired=howsubscribersacquired, howsubscribersacquiredotherbox=howsubscribersacquiredotherbox, anotheremailprovider=anotheremailprovider, anotheremailprovideryesdropdown=anotheremailprovideryesdropdown, filename=filename, staffid=staffid)

class Bulkimport(models.Model):
    id = models.AutoField(primary_key=True)
    importlocation = models.CharField(max_length=70)
    details = models.CharField(max_length=70)
    status = models.CharField(max_length=70)
    datetime = models.DateTimeField(null=True, blank=False)
    whatshouldwedo = models.CharField(max_length=70)
    notifywhenreviewcompleted = models.CharField(max_length=70)
    notifywhenreviewcompletedyesbox = models.CharField(max_length=70)
    howsubscribersacquired = models.CharField(max_length=70)
    howsubscribersacquiredotherbox = models.CharField(max_length=70)
    anotheremailprovider = models.CharField(max_length=70)
    anotheremailprovideryesdropdown = models.CharField(max_length=70)
    filename = models.CharField(max_length=70)
    file = models.FileField(blank=True)
    staffid = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    #i need to edit this to vp **********
   
  

    def __str__(self):
        return str(self.id)
    #This method should always return a natural key tuple 
    #Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):              #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate
        #made this dictionary return whitch will add to the previous dictionary
        return {'id':self.id,'importlocation': self.importlocation, 'details':self.details,'status': self.status,'datetime':self.datetime, 'whatshouldwedo':self.whatshouldwedo, 'notifywhenreviewcompleted': self.notifywhenreviewcompleted, 'notifywhenreviewcompletedyesbox':self.notifywhenreviewcompletedyesbox, 'howsubscribersacquired':self.howsubscribersacquired, 'howsubscribersacquiredotherbox': self.howsubscribersacquiredotherbox, 'anotheremailprovider':self.anotheremailprovider, 'anotheremailprovideryesdropdown': self.anotheremailprovideryesdropdown, 'filename':self.filename, 'staffid':self.staffid}
    natural_key.dependencies = ['pages.Staff']





class AttachedAllManager(models.Manager):
    def get_by_natural_key(self, id, dateofattachement, attachedtagid, attachedcustomfeildid, attachedformid, attachedgroupid, bulkimportid, staffid):
        return self.get(id = id, dateofattachement=dateofattachement, attachedtagid = attachedtagid, attachedcustomfeildid= attachedcustomfeildid,attachedformid=attachedformid, attachedgroupid=attachedgroupid, bulkimportid=bulkimportid, staffid=staffid)
class AttachedAll(models.Model):
    id = models.AutoField(primary_key=True)
    dateofattachement = models.DateTimeField(null=True, blank=False)
    attachedtagid = models.ForeignKey(Attachedtag, on_delete=models.CASCADE, null=True)
    attachedcustomfeildid = models.ForeignKey(Attachedcustomfeild, on_delete=models.CASCADE, null=True)
    attachedformid = models.ForeignKey(AttachedForm, on_delete=models.CASCADE, null=True)
    attachedgroupid = models.ForeignKey(Attachedgroup, on_delete=models.CASCADE, null=True)
    bulkimportid = models.ForeignKey(Bulkimport, on_delete=models.CASCADE, null=True)
    staffid = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.id)
    #This method should always return a natural key tuple 
    #Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):              #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate
        #made this dictionary return whitch will add to the previous dictionary
        return {'id':self.id,'dateofattachement':self.dateofattachement, 'attachedtagid':self.attachedtagid, 'attachedcustomfeildid': self.attachedcustomfeildid, 'attachedformid':self.attachedformid, 'attachedgroupid':self.attachedgroupid, 'bulkimportid':self.bulkimportid, 'staffid':self.staffid}
    natural_key.dependencies = ['pages.Attachedtag', 'pages.Attachedcustomfeild', 'pages.AttachedForm', 'pages.Attachedgroup', 'pages.Bulkimport', 'pages.Staff']
#i need to edit this to vp **********








"""

class AttachedtagfrombulkimportManager(models.Manager):
    def get_by_natural_key(self, id, dateofattachement, bulkimportid, tagid):
        return self.get(id = id, dateofattachement=dateofattachement, bulkimportid=bulkimportid, tagid=tagid)
class Attachedtagfrombulkimport(models.Model):
    id = models.IntegerField(default=1, primary_key=True)
    dateofattachement = models.DateTimeField(null=True, blank=False)
    bulkimportid = models.ForeignKey(Bulkimport, on_delete=models.CASCADE, null=True)
    tagid = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.id
    #This method should always return a natural key tuple 
    #Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):              #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate
        #made this dictionary return whitch will add to the previous dictionary
        return {'id':self.id,'dateofattachement': self.dateofattachement, 'bulkimportid':self.bulkimportid, 'tagid': self.tagid}
    #naturalkey has you app name then the Object
    natural_key.dependencies = ['pages.Bulkimport', 'pages.Tag']

class AttachedcustomfeildfrombulkimportManager(models.Manager):
    def get_by_natural_key(self, id, dateofattachement, bulkimportid, Customfeildid):
        return self.get(id = id, dateofattachement=dateofattachement, bulkimportid=bulkimportid, Customfeildid=Customfeildid)
class Attachedcustomfeildfrombulkimport(models.Model):
    id = models.IntegerField(default=1, primary_key=True)
    dateofattachement = models.DateTimeField(null=True, blank=False)
    bulkimportid = models.ForeignKey(Bulkimport, on_delete=models.CASCADE, null=True)
    Customfeildid = models.ForeignKey(Customfeild, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.id
    #This method should always return a natural key tuple 
    #Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):              #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate
        #made this dictionary return whitch will add to the previous dictionary
        return {'id':self.id,'dateofattachement': self.dateofattachement, 'bulkimportid':self.bulkimportid, 'Customfeildid': self.Customfeildid}
    #naturalkey has you app name then the Object
    natural_key.dependencies = ['pages.Bulkimport', 'pages.Customfeild']


class AttachedcustomfeildfrombulkimportManager(models.Manager):
    def get_by_natural_key(self, id, dateofattachement, bulkimportid, groupid):
        return self.get(id = id, dateofattachement=dateofattachement, bulkimportid=bulkimportid, groupid=groupid)
class Attachedgroupfrombulkimport(models.Model):
    id = models.IntegerField(default=1, primary_key=True)
    dateofattachement = models.DateTimeField(null=True, blank=False)
    bulkimportid = models.ForeignKey(Bulkimport, on_delete=models.CASCADE, null=True)
    groupid = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.id
    #This method should always return a natural key tuple 
    #Then, when you call serializers.serialize(), you provide use_natural_foreign_keys=True or use_natural_primary_keys=True arguments
    def natural_key(self):              #removed the neccessary feild from here  if u get the error "TypeError: Object of type SchoolProgram is not JSON serializable". remove it in other places below too cus thats more immediate
        #made this dictionary return whitch will add to the previous dictionary
        return {'id':self.id,'dateofattachement': self.dateofattachement, 'bulkimportid':self.bulkimportid, 'groupid': self.groupid}
    #naturalkey has you app name then the Object
    natural_key.dependencies = ['pages.Bulkimport', 'pages.Group']
"""
