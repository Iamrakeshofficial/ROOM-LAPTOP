from django.urls import path
from . import views

urlpatterns=[
    path('/home',views.Home,name='home'),
    path('/signup',views.User_SignUp,name='signup'),
    path('/login',views.User_Login,name='login'),
    path('/logout',views.User_Logout,name='logout'),
    path('/contact',views.Contact,name='contact'),
    path('/thanks',views.Thanks,name='thanks'),
    path('/add',views.add_Blogs,name='add'),
    path('/update/<int:id>/',views.update_Blogs,name='update'),
    path('/delete/<int:id>/',views.delete_Blogs,name='delete'),
    path('/about',views.About,name='about'),
    path('/pro',views.User_Profile,name='pro')
]