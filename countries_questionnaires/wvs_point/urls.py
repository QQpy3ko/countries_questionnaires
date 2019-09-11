from django.urls import path

from .views import *


urlpatterns = [
    path('', wvs_point_about, name='wvs_point_about'),
    path('questionnaire', wvs_point_test, name='wvs_point_questionnaire'),
    path('result', wvs_point_result, name='wvs_point_result')
]