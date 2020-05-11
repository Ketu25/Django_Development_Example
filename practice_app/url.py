from practice_app import views
from django.conf.urls import url

app_name = 'practice_app'

urlpatterns = [

    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]