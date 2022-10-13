from django.urls import path
from api import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('advocates/',views.AdvocatesList.as_view(),name='advocates_list'),
    path('advocates/<str:id>',views.AdvocatesDetail.as_view(),name='advocates_detail'),
    path('companies/',views.CompaniesList.as_view(),name='companies_list'),
    path('companies/<str:id>',views.ComapniesDetail.as_view(),name='companies_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)