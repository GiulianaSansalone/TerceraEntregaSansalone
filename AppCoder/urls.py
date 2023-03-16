from django.urls import path
from AppCoder.views import vista1, test_template
urlpatterns = [
    path('vista1/', vista1),
    path('template/', test_template)
]