from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views
from book.views import (welcome, CreateAllbooksGenericView
                         , AllbooksListGenericView, AllbooksDetailGenericView
                         ,UpdateAllbooksGenericView, DeleteAllbooksGenericView,view)

urlpatterns = [
    path('create/generic', CreateAllbooksGenericView.as_view(), name='allbooks.create'),
    path('allbooks', AllbooksListGenericView.as_view(), name='allbooks.index'),
    path('<int:pk>', AllbooksDetailGenericView.as_view(), name='allbooks.show'),
    path('<int:pk>/edit', login_required(UpdateAllbooksGenericView.as_view()), name='allbooks.edit'),
    path('<int:pk>/delete', login_required(DeleteAllbooksGenericView.as_view()), name='allbooks.delete'),
    path('welcome', welcome, name='welcome.html'),
    path('borrowedbooks/', views.view, name='borrowedbooks'),

]