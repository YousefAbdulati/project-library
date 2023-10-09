from django.urls import path, include
from django.contrib.auth.decorators import login_required

from accounts.views import profile, register, UserListGenericView, UpdateUserGenericView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', profile, name='profile.html'),
    path('register/', register, name='register.html'),
    path('index/', UserListGenericView.as_view(), name='uesrs.html'),
    path('<int:pk>/edit', UpdateUserGenericView.as_view(), name='users.edit'),

]