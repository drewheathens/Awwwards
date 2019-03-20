from django.conf.urls import url,include
from . import views
# from .views import submission
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^signup/',views.signup,name='signup'),
    # url(r'^', views.signup, name='signup'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^search/',views.search_results,name='search_results'),
    url(r'^new/post$',views.new_post, name='newPost'),
    url(r'^new/project$',views.new_project, name='new-project'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^edit/profile$',views.edit_profile, name='editProfile'),
    url(r'',views.index, name='index'),
    url(r'^userProfile/(\d+)',views.userprofile,name='userProfile'),
    url(r'^changeProfile/(?P<username>\w{0,50})',views.change_profile,name='changeProfile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
