from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from dashboard.views import Base
from dashboard.views import PageView

urlpatterns = patterns('',
    url(r'^$', Base.as_view(), name='home'),
    url(r'^page/(?P<pk>\d+)/$', PageView.as_view(), name='page-detail'),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
