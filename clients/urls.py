from django.urls import path
from .views import person_list, person_new, person_update, person_delete

urlpatterns = [
    path('list/', person_list, name='person_list'),
    path('new/', person_new, name='person_new'),
    path('update/<int:pk>/', person_update, name='person_update'),
    path('delete/<int:pk>/', person_delete, name='person_delete')
] 
