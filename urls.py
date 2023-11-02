from django.urls import path
from .views import ComptiaCoursesView

urlpatterns = [
    path('courses-comptia', ComptiaCoursesView.as_view(), name='comptia-courses'),  # callback url path    
]
