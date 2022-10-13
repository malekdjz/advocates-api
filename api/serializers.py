from rest_framework.serializers import ModelSerializer,SerializerMethodField
from app.models import *
from django.conf import settings

from core.settings import MEDIA_URL, SITE_URL


class AdvocateLinkSerializer(ModelSerializer):
    class Meta:
        model = AdvocateLink
        fields = ['name','url']

class CompanyLinkSerializer(ModelSerializer):
    class Meta:
        model = CompanyLink
        fields = ['name','url']
    
######################################################################################

class CompanyForAdvocateSerializer(ModelSerializer):
    url = SerializerMethodField()
    logo = SerializerMethodField()

    def get_logo(self,obj):
        return SITE_URL + MEDIA_URL + str(obj.logo)

    def get_url(self,obj):
        return SITE_URL+'/companies/'+str(obj.id)
    
    class Meta:
        model = Company
        fields = ['id','name','logo','url','summary','links']

class AdvocateForCompanySerializer(ModelSerializer):
    url = SerializerMethodField()
    profile_pic = SerializerMethodField()

    def get_profile_pic(self,obj):
        return SITE_URL + MEDIA_URL + str(obj.profile_pic)

    def get_url(self,obj):
        return SITE_URL+'/advocates/'+str(obj.id)
    
    class Meta:
        model = Advocate
        fields = ['id','name','profile_pic','url','short_bio']
        
######################################################################################

class AdvocateSerializer(ModelSerializer):
    url = SerializerMethodField()
    profile_pic = SerializerMethodField()
    company = CompanyForAdvocateSerializer(read_only=True)
    links = AdvocateLinkSerializer(many=True,read_only=True)

    def get_profile_pic(self,obj):
        return SITE_URL + MEDIA_URL + str(obj.profile_pic)

    def get_url(self,obj):
        return SITE_URL+'/advocates/'+str(obj.id)
    
    class Meta:
        model = Advocate
        fields = ['id','name','profile_pic','url','short_bio','long_bio','advocate_since','company','links']

class CompanySerializer(ModelSerializer):
    links = CompanyLinkSerializer(many=True,read_only=True)
    advocates = AdvocateForCompanySerializer(many=True,read_only=True)
    logo = SerializerMethodField()

    def get_logo(self,obj):
        return SITE_URL + MEDIA_URL + str(obj.logo)
    class Meta:
        model = Company
        fields = ['id','name','logo','summary','links','advocates']


