"""TycheBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from Account import views

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="GPLv3 License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Account/',views.Account.as_view()),
    path('Account/<str:pk>',views.Account.as_view()),
    path('Accountcollection/<str:pk>',views.AccountCollection.as_view()),
    path('collection/',views.collectionView.as_view()),
    path('collection/<str:pk>',views.collectionView.as_view()),
    path('WorkArtProperty/<str:pk>',views.WorkArtProperty.as_view()),
    path('WorkArtstatistic/<str:pk>',views.WorkArtstatistic.as_view()),
    path('WorkArtLike/<str:pk>',views.WorkArtLike.as_view()),
    path('WorkArtLiked/<str:pk>',views.WorkArtLiked.as_view()),
    path('WorkArt/',views.WorkArt.as_view()),
    path('WorkArt/<str:pk>',views.WorkArt.as_view()),
    path('WorkArtCollection/<str:pk>',views.WorkArtCollection.as_view()),
    path('WorkArtCollections/<str:pk>',views.collectionworkarts.as_view()),
    path('AccountWorkarts/<str:pk>',views.AccountWorkarts.as_view()),
    path('Accountfavorites/<str:pk>',views.Accountfavorites.as_view()),
    path('WorkArtProperty/<str:pk>',views.WorkArtProperty.as_view()),
    #WorkArtProperty
    #Accountfavorites
    path('search',views.Search.as_view()),
    path('explore',views.Explore.as_view()),
    path('sortNFT',views.SortNFT.as_view()),
    path('sortCollection',views.Sortcollection.as_view()),



    #path('Account/Edit/<int:pk>',views.EditAccount.as_view()),
    #path('Account/Get/<int:pk>',views.GetAccount.as_view()),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
