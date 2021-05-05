from django.urls import path
from . import views
app_name="WebApp"
urlpatterns = [
    path('item/',views.Items,name='item'),
    path('cre/',views.create,name='cre'),
    path('pro/',views.Cook,name='process'),
    path('dtail/<int:id>/',views.detail,name="dtail"),
    path('dlte/<int:id>/',views.delete,name="dlte"),
    path('reg/',views.Register,name='reg'),
    path('login/',views.Login,name='login'),
    path('',views.Home,name='home'),
    path('success/',views.Success,name='success'),
    path('logout/',views.logout_kc,name="logout"),

]