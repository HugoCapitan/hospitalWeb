from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import IndexView, ProfileView, LoginView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hospitalWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('patients.urls')),
    url(r'', include('appointments.urls')),
	url(r'^login/$', LoginView.as_view(), name='login'),
	url(r'^perfil/$', ProfileView.as_view(), name='profile'),
)


urlpatterns += staticfiles_urlpatterns() 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)