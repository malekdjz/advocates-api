from django.urls import path
from api import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('advocates/',views.AdvocatesList.as_view(),name='advocates'),
    path('advocates/<str:pk>',views.AdvocatesDetail.as_view(),name='advocate-detail'),
    path('companies/',views.CompaniesList.as_view(),name='companies'),
    path('companies/<str:pk>',views.ComapniesDetail.as_view(),name='company-detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
