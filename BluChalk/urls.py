
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    #path('rest-auth/', include('rest_auth.urls')),
   # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('users/', include('users.urls')),
    path('api/', include('api.urls' )),
    path('courses/', include('api.urls') ),
    path('enrollment/', include('enrollment.urls')),
    path('forums/', include('forums.urls')),
    path('payments/', include('payments.urls')),
    path('assessments/', include('assessments.urls')),
    path('quiz/', include('quiz.urls')),

]
