from django.urls import path
from basic import views

urlpatterns=[
    path('',views.index,name="index"),
    path('insertData',views.insertData,name="insertData"),
    path('updateData/<int:id>',views.updateData,name="updateData"),
    path('deleteData/<int:id>',views.deleteData,name="deleteData")
]