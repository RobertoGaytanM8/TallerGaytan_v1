from django.urls import path
from cbtis_app import views
urlpatterns = [
    path('',views.VerLista,name='ver_lista'),
]