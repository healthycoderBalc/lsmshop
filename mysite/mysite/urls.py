"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
# from django.urls import re_path as url

from .settings import base
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView




urlpatterns = [
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
     # Python Social Auth URLs 
    path('', include('social.apps.django_app.urls', namespace='social')),
    path('', include('pwa.urls')),
    path('serviceworker', (TemplateView.as_view(
      template_name="browsepages/serviceworker.js", 
      content_type='application/javascript',)), 
      name='serviceworker'),
]


    # Python Social Auth URLs 


if base.DEBUG:
        urlpatterns += staticfiles_urlpatterns()
        urlpatterns += static(base.MEDIA_URL,
                              document_root=base.MEDIA_ROOT)
        