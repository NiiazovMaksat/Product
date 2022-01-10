import delete as delete
from django.urls import path

from webapp.views import main_page, view_page, edit_page, create_page, delete

urlpatterns = [
    path('', main_page, name="main"),
    path('view/<int:pk>', view_page, name="view"),
    path('edit/<int:pk>', edit_page, name="edit"),
    path('delete/<int:pk>', delete, name="delete"),
    path('create', create_page, name="create")]