from django.urls import path
from . import views
app_name='demoapp'
urlpatterns = [
   path('',views.index,name='index'),
   path('movie/<int:movie_id>/',views.detail,name='detail'),
   path('add/',views.add,name='add'),
   path('update/<int:id>/',views.update,name='update'),
   path('delete/<int:id>/', views.delete, name='deleattete'),

]