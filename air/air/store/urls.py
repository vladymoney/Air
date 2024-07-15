from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_index, name='product_list_index'),
    path('products/', views.product_list, name='product_list'),

    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('remove-from-cart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('add-to-favorites/<int:pk>/', views.add_to_favorites, name='add_to_favorites'),
    path('favorites/', views.favorites_detail, name='favorites_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('search/', views.product_search, name='product_search'),
path('delivery-terms/', views.delivery_terms_view, name='delivery-terms'),
    path('payment-methods/', views.payment_methods_view, name='payment-methods'),
    path('order-information/', views.order_information_view, name='order-information'),
    path('warranty-claims/', views.warranty_claims_view, name='warranty-claims'),
    path('online-credit/', views.online_credit_view, name='online-credit'),
    path('discounts/', views.discounts_view, name='discounts'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy-policy'),
    path('site-terms/', views.site_terms_view, name='site-terms'),
    path('installation/', views.installation_view, name='installation'),
    path('preliminary-survey/', views.preliminary_survey_view, name='preliminary-survey'),
    path('consultation/', views.consultation_view, name='consultation'),
    path('aircon-maintenance/', views.aircon_maintenance_view, name='aircon-maintenance'),
    path('aircon-service/', views.aircon_service_view, name='aircon-service'),
    path('projects/', views.projects_view, name='projects'),

    path('about-us/', views.about_us_view, name='about-us'),
    path('contact-us/', views.contact_us_view, name='contact-us'),

    path('free-inspection/', views.free_inspection_view, name='free-inspection'),
    path('ac-maintenance/', views.ac_maintenance_view, name='ac-maintenance'),
    path('ac-service/', views.ac_service_view, name='ac-service'),
    path('partners/', views.partners_view, name='partners'),
    path('team/', views.team_view, name='team'),
    path('news/', views.news_view, name='news'),
    path('help/', views.help_view, name='help'),
    path('distributors/', views.distributors_view, name='distributors'),
    path('catalogs/', views.catalogs_view, name='catalogs'),

]
