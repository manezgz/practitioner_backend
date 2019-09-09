"""practitionerBank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from users.views import UsersList,UserSingle
from accounts.views import AccountsSingle,AccountsList
from transactions.views import TransactionList
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('currobanco/v1/api/auth/', include('mongo_auth.urls')),
    path('currobanco/v1/api/services/users',UsersList.as_view()),
    path('currobanco/v1/api/services/users/<str:email>',UserSingle.as_view()),
    path('currobanco/v1/api/services/accounts',AccountsList.as_view()),
    path('currobanco/v1/api/services/accounts/user/<str:owner>',AccountsList.as_view()),
    path('currobanco/v1/api/services/accounts/<str:iban>',AccountsSingle.as_view()),
    path('currobanco/v1/api/services/transactions',TransactionList.as_view()),
    path('currobanco/v1/api/services/transactions/<str:iban>',TransactionList.as_view()),
    url(r'currobanco/v1/api/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'currobanco/v1/api/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'currobanco/v1/api/swagger/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
