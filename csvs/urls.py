from django.urls import path
from .views import upload_csv_view

app_name = 'csvs'

urlpatterns = [
    path('', upload_csv_view, name="upload-view"),
]

