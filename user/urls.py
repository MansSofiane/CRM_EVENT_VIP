from django.urls import path,include
from .views import *

urlpatterns = [
	path('User',UserRegistrationView.as_view(),name='Add_User'),
	path('User',UsersList.as_view(),name='get_User'),
	path('User/<uuid:id>/', ListUser.as_view(), name='user-detail'),
	path('signin/',UserLoginView.as_view()),

]