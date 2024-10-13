from django.urls import path
from .views import Test,UserRegister,UserLoginView,UserLogoutView,AdminView,StaffView,TeacherView,StudentView
urlpatterns = [
    path('test/',Test.as_view()),
    path('register/',UserRegister.as_view()),
    path('login/',UserLoginView.as_view()),
    path('logout/',UserLogoutView.as_view()),
    path('admin/',AdminView.as_view()),
    path('staff/',StaffView.as_view()),
    path('teacher/',TeacherView.as_view()),
    path('student/',StudentView.as_view()),
]
