"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from firstapp import views
from django.urls import re_path
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from firstapp.views import BuildingListView
from firstapp.views import ArchiListView
from firstapp.views import StyleListView

urlpatterns = [
    path('', views.base),
    path('accounts/', include('django.contrib.auth.urls')),
    path('test/', views.test_main),
    path('about/', TemplateView.as_view(template_name="firstapp/about.html",
                                        extra_context={"header": "О сайте"})),
    path('contact/', TemplateView.as_view(template_name="firstapp/contact.html")),
    path('products/<int:productid>/', views.products),
    path('users/', views.users),
    path('building/<int:request_id>/', views.buildings),
    path('archi/<int:request_id>/', views.archis),
    path('style/<int:request_id>/', views.styles),
    path('photoes/', views.cabinet),
    path('images/', views.user_page),
    url(r'^admin/', admin.site.urls),
    url(r'^publishers/$', BuildingListView.as_view()),
    url(r'^buildings/$', views.BuildingListView.as_view(), name='buildings'),
    url(r'^archis/$', views.ArchiListView.as_view(), name='archis'),
    url(r'^styles/$', views.StyleListView.as_view(), name='styles'),
    path('comment_edit/<int:request_id>/<int:comment_id>/', views.comment_edit),
    path('comment_delete/<int:request_id>/<int:comment_id>/', views.comment_delete),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

