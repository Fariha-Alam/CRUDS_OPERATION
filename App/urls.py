

from django.urls import path
from App import views
from .views import *

urlpatterns = [
   path('',first,name='first'),

   path('create/', create, name='create'),
   path('delete/<int:id>', views.deletedata, name='deletedata'),
   path('see_profile/<int:id>', views.see_profile, name='see_profile'),
   path('update_profile/<int:id>', views.update_profile, name='update_profile'),
   #path('update/<int:id>', update.as_view(), name='update'),

   
]
