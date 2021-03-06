from django.urls import path,include
from .  import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [

    path('', views.home, name='home'),
    path('register/', views.signup, name='signup'),
    url(r'^hoods', views.all_hoods, name='hoods'),
    path('account/', include('django.contrib.auth.urls')),
    path('all-hoods/', views.hoods, name='hood'),
    # url(r'^business/view',views.display_business,name = 'viewbiz'),
    url(r'businessses/$', views.businesses, name = 'businesses'),
    url(r'profile/$', views.profile, name = 'profile'),
    path('new-hood/', views.create_hood, name='new-hood'),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
    path('join_hood/<id>', views.join_hood, name='join-hood'),
    path('leave_hood/<id>', views.leave_hood, name='leave-hood'),
    path('single_hood/<hood_id>', views.single_hood, name='single-hood'),
    path('<hood_id>/new-post', views.create_post, name='post'),
    url('<hood_id>/members', views.hood_members, name='members'),
    url(r'^createHood/$', views.createHood, name='createHood'),
    url('search/', views.search_business, name='search'),
    url('^api/businesse/$', views.BusinessList.as_view())

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
