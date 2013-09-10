from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pages.home.views.index', name='home'),
    url(r'home/$', 'pages.home.views.index', name='home'),
    url(r'blog/$', 'pages.blog.views.index', name='blog'),
    # url(r'^EllieBlog/', include('EllieBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)