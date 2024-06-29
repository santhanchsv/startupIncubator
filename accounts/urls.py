from django.urls import path, include
from accounts import models
from accounts import views as accounts_views
from chat import views as chat_views


urlpatterns = [
    path('student-register' , accounts_views.studentRegister , name = 'student-register'),
    path('student-login', accounts_views.studentLogin , name = 'student-login'),
    path('student-details', accounts_views.studentDetails, name = 'student-details'), 
    path('entrepreneur-register' , accounts_views.entrepreneurRegister , name = 'entrepreneur-register'),
    path('entrepreneur-login', accounts_views.entrepreneurLogin , name = 'entrepreneur-login'),
    path('entrepreneur-details', accounts_views.entrepreneurDetails, name = 'entrepreneur-details'),
    path('investor-register' , accounts_views.investorRegister , name = 'investor-register'),
    path('investor-login', accounts_views.investorLogin, name='investor-login'),
    path('investor-details', accounts_views.investorDetails, name = 'investor-details'), 
    path('mentor-register' , accounts_views.mentorRegister , name = 'mentor-register'),
    path('mentor-details', accounts_views.mentorDetails, name = 'mentor-details'),    
    path('mentor-login', accounts_views.mentorLogin , name = 'mentor-login'),
    path('submit-project', accounts_views.submitProjectIdea , name = 'submit-project'),
    path('successful-registration' , accounts_views.registerResponse , name = 'successful-registration'),
    path('dashboard' , accounts_views.dashboard , name = 'dashboard'),
    path('logout' , accounts_views.logoutPage , name = 'logout'),
    path('investor/<int:pk>' , accounts_views.investor_single_details , name = 'investor'),
    path('profile/', accounts_views.dashboard, name='profile'),  
    path('dashboardM' , accounts_views.dashboardM , name = 'dashboardM'),  
    path('dashboardI' , accounts_views.dashboardI , name = 'dashboardI'), 

    path('dashboard', accounts_views.submitProjectIdea , name = 'dashboard'),


    path('home', chat_views.home, name='home'),
    path('<str:room>/', chat_views.room, name='room'),
    path('checkview', chat_views.checkview, name='checkview'),
    path('send', chat_views.send, name='send'),
    path('getMessages/<str:room>/', chat_views.getMessages, name='getMessages'),
]
