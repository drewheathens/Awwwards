from django.conf.urls import url,include
from . import views
# from .views import submission
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.index,name='indexPage'),
    url(r'^projects/(\d+)',views.project,name ='projects'),
    url(r'^new/project$', views.new_project, name='newProject'),
    url(r'^profile/',views.profile,name = 'Profile'),
    url(r'^edit/profile/$',views.edit_profile,name = 'editProfile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^project-detail/(\d+)',views.search_project,name = 'project-detail'),
    url(r'^project-vote/(\d+)',views.vote_project,name = 'project-vote'),
    url(r'^api/project/$', views.ProjectList.as_view()),
    url(r'^api/profile/$', views.ProfileList.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    