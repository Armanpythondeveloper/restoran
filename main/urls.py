from django.urls import path
from .import views

urlpatterns = [

    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('booking',views.booking,name='booking'),
    path('contact/',views.contact,name='contact'),
    path('menu/',views.menu,name='menu'),
    path('service/',views.service,name='service'),
    path('team/',views.team,name='team'),
    path('teatimonial/',views.testimonial,name='testimonial'),
    path('book_a_table/',views.book_a_table,name='book_a_table')

]