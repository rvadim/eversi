from django.conf.urls import patterns, include, url
from django.contrib import admin

from dashboard.views import Base

urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Base.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
