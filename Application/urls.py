from django.urls import path
from . import views
urlpatterns = [
    path('', views.testview, name="base"),
    path('add', views.add_ticket, name='add'),
    # path('upd/<int:id>/', views.update_ticket, name='update'),
    # path('delete/<int:id>/', views.delete_ticket, name='delete'),
#     path('cadd', views.add_contactus, name='cadd'),
#     path('cupd/<int:id>/', views.update_contactus, name='cupdate'),
#     path('cdelete/<int:id>/', views.delete_contactus, name='cdelete')
#
]