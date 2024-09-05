
from django.urls import path
from .import views
urlpatterns = [
    path("", views.home,name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('thank-you/', views.thank_you_view, name='thank_you'),  # Optional thank you page

]
