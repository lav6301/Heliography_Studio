from django.urls import path
from .views import user_login,user_logout,user_signup,home, service_detail
from . import views
from .views import contact_view
from django.views.generic import TemplateView

urlpatterns = [
    path('', home, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('service/<int:pk>/', service_detail, name='service_detail'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('gallery/',views.gallery, name='gallery'),
    path('contact/', contact_view, name='contact'),
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
]

