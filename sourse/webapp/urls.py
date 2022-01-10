
from django.urls import path

from webapp.views import main_page, view_page

urlpatterns = [
    path('', main_page, name="main"),
    path('view/<int:pk>', view_page, name="view"),
    path('edit/<int:pk>', edit_page, name="edit")
]
