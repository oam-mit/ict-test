from django.urls import path
from . import views


app_name='decoder'


urlpatterns = [
    path('',views.index,name="index"),
    path('convert_text_to_speech',views.convert_text_to_speech,name="convert_text_to_speech"),
    path('download_output',views.download,name="download_output"),
]
