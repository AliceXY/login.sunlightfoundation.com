from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(
        r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'accounts/login.html'
        },
    ),
    url(r'^profile/$', 'shoelace.apps.accounts.views.profile')

)
