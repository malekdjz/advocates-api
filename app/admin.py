from django.contrib import admin
from app.models import *
# Register your models here.

admin.site.register(Advocate)
admin.site.register(Company)
admin.site.register(AdvocateLink)
admin.site.register(CompanyLink)