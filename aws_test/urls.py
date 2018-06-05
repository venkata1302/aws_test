from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'aws_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

 #   url(r'^admin/', include(admin.site.urls)),
    url(r'^home/',views.home.as_view(),name = 'home'),
    url(r'^addplayer/',views.add_player,name = 'addplayer'),
    url(r'^playerlist/',views.player_list.as_view(),name = 'playerlist'),

]

if settings.DEBUG is True:
    #urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

