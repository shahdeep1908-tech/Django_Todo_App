from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name="todo"),
    path('del/<str:item_id>', views.remove, name="del"),
    path('upt/<str:item_id>', views.update, name="update")
]