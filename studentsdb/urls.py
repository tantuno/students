from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView, TemplateView

from .settings import MEDIA_ROOT, DEBUG

from students.views.students import StudentUpdateView, StudentDeleteView
from students.views.groups import GroupDeleteView, groups_add,groups_edit, groups_list
from students.views.journal import JournalView


js_info_dict = {
    'packages':('students',),
}

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n\.js$', 'django.views.i18n.javascript_catalog', js_info_dict),
    # Students urls
    url(r'^$', 'students.views.students.students_list', name='home'),
    url(r'^students/add/$', 'students.views.students.students_add', name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),

    # Groups urls
    url(r'^groups/$', login_required(groups_list), name='groups'),
    url(r'^groups/add/$', login_required(groups_add), name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', 'students.views.groups.groups_edit', name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$', GroupDeleteView.as_view(), name='groups_delete'),

    # Journal urls
    url(r'^journal/$', JournalView.as_view(), name='journal'),
    url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),
    url(r'^admin/', include(admin.site.urls)),

    # Exam urls
    url(r'^exams/$', 'students.views.exams.exam_list', name='exams'),
    url(r'^exams/add/$', 'students.views.exams.exam_add', name='exam_add'),
    url(r'^exams/(?P<eid>\d+)/edit/$', 'students.views.exams.exam_edit', name='exam_edit'),
    url(r'^exams/(?P<eid>\d+)/delete/$','students.views.exams.exam_delete', name='exam_delete'),
    url(r'^exams/(?P<eid>\d+)/result/$', 'students.views.exams.exam_result', name='exam_result'),

    #Contact Admin Form
    url(r'^contact-admin/$', 'students.views.contact_admin.contact_admin', name='contact_admin'),

    #User Related urls
    url(r'^users/profile/$', login_required(TemplateView.as_view(template_name='registration/profile.html')), name='profile'),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'home'},
        name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'),
        name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls',
        namespace='users')),

    #Social Auth Related urls
    url('^social/', include('social.apps.django_app.urls', namespace='social')),

)
if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
