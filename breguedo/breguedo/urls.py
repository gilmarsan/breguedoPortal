"""breguedo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('advogado.urls')),
    path('advogado/', include('advogado.urls')),
    path('artigo/', include('advogado.urls')),
    path('contato/', include('advogado.urls')),
    path('videos/', include('advogado.urls')),
    path('direitocrianca/', include('advogado.urls')),
    path('juris/', include('advogado.urls')),
    path('plast/', include('advogado.urls')),
    path('rasc/', include('advogado.urls')),
    path('quadrinhos/', include('advogado.urls')),
    path('tiras/', include('advogado.urls')),
    path('ilustracao/', include('advogado.urls')),
    path('poema/', include('advogado.urls')),
    path('conto/', include('advogado.urls')),
    path('microconto/', include('advogado.urls')),
    path('video_ek/', include('advogado.urls')),
    path('desenho_ek/', include('advogado.urls')),
    path('estoria_ek/', include('advogado.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)