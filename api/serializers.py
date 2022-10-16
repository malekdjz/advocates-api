from rest_framework.serializers import ModelSerializer,SerializerMethodField
from app.models import *


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
        request = self.context.get('request')
        url = obj.logo.url
        return request.build_absolute_uri(url)

    def get_url(self,obj):
        request = self.context.get('request')
        id = obj.id
        return request.build_absolute_uri(id)
    
    class Meta:
        model = Company
        fields = ['id','url','name','logo','summary']

class AdvocateForCompanySerializer(ModelSerializer):
    url = SerializerMethodField()
    profile_pic = SerializerMethodField()

    def get_profile_pic(self,obj):
        request = self.context.get('request')
        url = obj.profile_pic.url
        return request.build_absolute_uri(url)

    def get_url(self,obj):
        request = self.context.get('request')
        id = obj.id
        return request.build_absolute_uri(id)
    
    class Meta:
        model = Advocate
        fields = ['id','url','name','profile_pic','short_bio']
        
######################################################################################

class AdvocateSerializer(ModelSerializer):
    url = SerializerMethodField()
    profile_pic = SerializerMethodField()
    company = CompanyForAdvocateSerializer(read_only=True)
    links = AdvocateLinkSerializer(many=True,read_only=True)

    def get_profile_pic(self,obj):
        request = self.context.get('request')
        url = obj.profile_pic.url
        return request.build_absolute_uri(url)

    def get_url(self,obj):
        request = self.context.get('request')
        id = obj.id
        return request.build_absolute_uri(id)
    
    class Meta:
        model = Advocate
        fields = ['id','url','name','profile_pic','short_bio','long_bio','advocate_since','links','company']

class CompanySerializer(ModelSerializer):
    links = CompanyLinkSerializer(many=True,read_only=True)
    advocates = AdvocateForCompanySerializer(many=True,read_only=True)
    logo = SerializerMethodField()
    url = SerializerMethodField()

    def get_url(self,obj):
        request = self.context.get('request')
        id = obj.id
        return request.build_absolute_uri(id)

    def get_logo(self,obj):
        request = self.context.get('request')
        url = obj.logo.url
        return request.build_absolute_uri(url)
    class Meta:
        model = Company
        fields = ['id','url','name','logo','summary','links','advocates']


