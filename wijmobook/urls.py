from django.conf.urls import patterns, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
def view(pattern, template, name):
    return url(pattern, TemplateView.as_view(template_name=template), name=name)

urlpatterns = patterns('',
    view(r'^$', 'index.html', 'home'),
    view(r'^preface/', 'preface.html', 'preface'),
    view(r'^reviews/', 'reviews.html', 'reviews'),
    url(r'^screenshots/', 'wijmobook.views.gallery', name='gallery'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('wijmobook.contact',
    url(r'^contact/$', 'contact_form', name="contact_form"),
    view(r'^contact/success/$', 'index.html', "contact_success"),
)
