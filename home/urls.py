from django.urls import path
from .views import home, phones, laptops, watchs, phone_details,  watch_delete, laptop_delete, phone_delete ,\
laptop_details, watch_details, watch_update, laptop_update, phone_update, watch_create_form, phone_create_form, laptop_create_form



urlpatterns = [
    path('', home, name='home'),
    path('phones/', phones, name='phones'),
    path('laptops/', laptops, name='laptops'),
    path('watches/', watchs, name='watches'),
    path('phone_details/<int:pk>/', phone_details, name='phone_details'),
    path('laptop_details/<int:pk>/', laptop_details, name='laptop_details'),
    path('watch_details/<int:pk>/', watch_details, name='watch_details'),
    path('phone_create/', phone_create_form, name='phone_create'),
    path('laptop_create/', laptop_create_form, name='laptop_create'),
    path('watch_create/', watch_create_form, name='watch_create'),
    path('phone_update/<int:pk>/', phone_update, name='phone_update'),
    path('laptop_update/<int:pk>/', laptop_update, name='laptop_update'),
    path('watch_update/<int:pk>/', watch_update, name='watch_update'),
    path("watch_delete/<int:pk>/", watch_delete, name='watch_delete'),
    path("phone_delete/<int:pk>/", phone_delete, name='phone_delete'),
    path("laptop_delete/<int:pk>/", laptop_delete, name='laptop_delete')
]

