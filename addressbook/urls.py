from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'addressbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'base.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),

    # auth
    url(r'^register/$', 'base.views.registerView', name='register'),
    url(r'^login/$', 'base.views.loginView', name='login'),
    url(r'^logout/$', 'base.views.logoutView', name='logout'),

    # contact
    url(r'^detail/(?P<num>[0-9]+)/$', 'base.views.contactDetailView', name='detail'),
    url(r'^delete/(?P<num>[0-9]+)/$', 'base.views.contactDeleteView', name='delete'),
    url(r'^search/$', 'base.views.searchListView', name='search'),
]
