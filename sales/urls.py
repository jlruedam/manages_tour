from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    
    # Menu
    path('menu', views.menu, name='menu'),

    # Sales
    path('sales/', views.sale_list, name='sale_list'),
    path('sales/create/', views.create_sale, name='sale_create'),
    # path('sales/sale_tour/<int:tour_id>', views.sale_tour, name='sale_tour'),
    path('sales/<int:pk>/edit/', views.sale_update, name='sale_update'),
    path('sales/<int:pk>/delete/', views.sale_delete, name='sale_delete'),


    # Agencies
    path('agencies/', views.agency_list, name='agency_list'),
    path('agencies/create/', views.agency_create, name='agency_create'),
    path('agencies/<int:pk>/edit/', views.agency_update, name='agency_update'),
    path('agencies/<int:pk>/delete/', views.agency_delete, name='agency_delete'),

    # Tours
    path('tours/', views.tour_list, name='tour_list'),
    path('tours/tour/<int:id>', views.tour, name='tour'),
    path('tours/create/', views.tour_create, name='tour_create'),
    path('tours/<int:pk>/edit/', views.tour_update, name='tour_update'),
    path('tours/<int:pk>/delete/', views.tour_delete, name='tour_delete'),

    # Clients
    path('clients/', views.client_list, name='client_list'),
    path('clients/create/', views.client_create, name='client_create'),
    path('clients/<int:pk>/edit/', views.client_update, name='client_update'),
    path('clients/<int:pk>/delete/', views.client_delete, name='client_delete'),

    # # Vendors
    # path('vendors/', views.vendor_list, name='vendor_list'),
    # path('vendors/create/', views.vendor_create, name='vendor_create'),
    # path('vendors/<int:pk>/edit/', views.vendor_update, name='vendor_update'),
    # path('vendors/<int:pk>/delete/', views.vendor_delete, name='vendor_delete'),
    # Clients
    
    path('payments/create/', views.client_create, name='payment_create'),
    
    # Referrers
    path('referrers/create/', views.referrer_create, name='referrer_create'),
]
