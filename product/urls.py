from django.urls import path

from .views import *

urlpatterns = [
    path('list_create/', product_list_create),
    # path('create/', product_create),
    # path('list/', product_list),
    # path('detail/<int:pk>/', product_detail),   
    # path('update/<int:pk>/', product_update),   
    # path('partila_update/<int:pk>/', product_partial_update),   
    # path('delete/<int:pk>/', product_delete),   
    path('product_dupud/<int:pk>/', product_detail_update_partialupdate_delete),   
]