from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'registeruser.views.home', name='home'),
<<<<<<< HEAD
    url(r'^frontpage', 'registeruser.views.frontpage', name='frontpage'),
    url(r'^add-course/$', 'registeruser.views.addcourse', name='addcourse'),
    url(r'^search-form/$', 'registeruser.views.search_form', name='search_form'),
    url(r'^search/$','registeruser.views.search',name='search'),
=======
>>>>>>> a9c74d4ccfc05e6a99b0c910acbdeb553577e62d
    # url(r'^MOOCClient/', include('MOOCClient.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
<<<<<<< HEAD



=======
>>>>>>> a9c74d4ccfc05e6a99b0c910acbdeb553577e62d
