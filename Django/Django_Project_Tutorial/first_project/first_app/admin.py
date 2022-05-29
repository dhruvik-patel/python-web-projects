from django.contrib import admin
from first_app.models import Webpage,AccessRecord,Topic
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)
