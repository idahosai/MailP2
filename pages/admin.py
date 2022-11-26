from django.contrib import admin

# Register your models here.

#to show in adins site do this
from .models import Attachedtag
from .models import Tag
from .models import Attachedcustomfeild
from .models import Customfeild
from .models import Attachedgroup
from .models import Group
from .models import Form
from .models import AttachedForm
# and then you register that by doing the follwoing:
admin.site.register(Attachedtag)
admin.site.register(Tag)
admin.site.register(Attachedcustomfeild)
admin.site.register(Customfeild)
admin.site.register(Attachedgroup)
admin.site.register(Group)
admin.site.register(AttachedForm)
admin.site.register(Form)