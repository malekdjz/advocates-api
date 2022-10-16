from rest_framework.serializers import ModelSerializer,SerializerMethodField,HyperlinkedIdentityField
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
    url = HyperlinkedIdentityField(view_name='company-detail')
    
    class Meta:
        model = Company
        fields = ['id','url','name','logo','summary']

class AdvocateForCompanySerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='advocate-detail')
    
    class Meta:
        model = Advocate
        fields = ['id','url','name','profile_pic','short_bio']
        
######################################################################################

class AdvocateSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='advocate-detail')
    company = CompanyForAdvocateSerializer(read_only=True)
    links = AdvocateLinkSerializer(many=True,read_only=True)
    
    class Meta:
        model = Advocate
        fields = ['id','url','name','profile_pic','short_bio','long_bio','advocate_since','links','company']

class CompanySerializer(ModelSerializer):
    links = CompanyLinkSerializer(many=True,read_only=True)
    advocates = AdvocateForCompanySerializer(many=True,read_only=True)
    url = HyperlinkedIdentityField(view_name='company-detail')

    class Meta:
        model = Company
        fields = ['id','url','name','logo','summary','links','advocates']


