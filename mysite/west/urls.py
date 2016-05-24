from django.conf.urls import patterns,include,url

urlpatterns=[
    url(r'^$', 'west.views.first_page'),
    url(r'^staff/', 'west.views.staff'),
    url(r'^staff2/','west.views.staff2'),
    url(r'^templay/', 'west.views.templay'),
    url(r'^form/', 'west.views.form'),
    url(r'^investigate/', 'west.views.investigate'),
    url(r'^inve/', 'west.views.inve'),
    url(r'^savestaff/', 'west.views.savestaff'),
]
