from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add_db/$', 'add_db.views.add_db'),
    url(r'^add_db/result/$', 'add_db.views.result'),
    url(r'^fill/$', 'project.views.fill'),
    url(r'^form1/$', 'project.views.fdata'),
	url(r'^form1/project.views.fill/$', 'project.views.done'),
	url(r'^form2/project.views.fill/$', 'project.views.done'),
    url(r'^form2/$', 'project.views.cerdata'),
    url(r'^data/$', 'project.views.info'),
    url(r'^index/$', 'project.views.new'),
    url(r'^data/(?P<Roll_Number>\d+)/$', 'project.views.degree'),
    url(r'^filter/$', 'project.views.filter'),
    #url(r'^filter1/$', 'data.views.filter1'),
    url(r'^search/$', 'project.views.search'),
    url(r'^search/result/$', 'project.views.degree'),

)
