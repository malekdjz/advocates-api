from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from app.models import *
from api.serializers import *
# Create your views here.
class Index(APIView):
    def get(self,request):
        return Response({
            'advocates':request.build_absolute_uri('/advocates'),
            'comapnies':request.build_absolute_uri('/companies'),
            'parameters':'possible get parameters are: page | limit (20 by default)| query'
            })

class AdvocatesList(APIView):
    def get(self,request):
        params = request.GET
        query = params.get('query','')
        limit = params.get('limit','')

        queryset = Advocate.objects.filter(name__icontains=query)
        paginate = PageNumberPagination()
        try:
            limit = int(limit)
        except:
            pass
        else:
            paginate.page_size = abs(limit)
        results = paginate.paginate_queryset(queryset=queryset,request=request)
        serializer = AdvocateSerializer(results,many=True,context={'request':request})
        response = paginate.get_paginated_response(data=serializer.data)

        return response

class AdvocatesDetail(APIView):
    def get(self,request,pk):
        try:
            advocate = Advocate.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AdvocateSerializer(advocate,context={'request':request})
        return Response(serializer.data)


class CompaniesList(APIView):
    def get(self,request):
        params = request.GET
        query = params.get('query','')
        limit = params.get('query','')
        queryset = Company.objects.filter(name__icontains=query)
        paginate = PageNumberPagination()
        try:
            int(limit)
        except:
            pass
        else:
            paginate.page_size = limit
        results = paginate.paginate_queryset(queryset=queryset,request=request)
        serializer = CompanySerializer(results,many=True,context={'request':request})
        response = paginate.get_paginated_response(data=serializer.data)

        return response

class ComapniesDetail(APIView):
    def get(self,request,pk):
        try:
            company = Company.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CompanySerializer(company,context={'request':request})
        return Response(serializer.data)
