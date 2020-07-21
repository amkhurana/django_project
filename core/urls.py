from django.urls import path
# from .views import item_list, about, index, cart, shop_single, thankyou, about

from .views import (
    ItemDetailView,
    CartView,
    CheckoutView,
    OrderSummaryView,
    AboutView,
    HomeView,
    ContactView,
    ItemDetailView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cart/', CartView.as_view(), name='cart'),
    path('meet/', ContactView.as_view(), name='contact'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('accounts/profile/', HomeView.as_view(), name='logins'),
    path('itemdetail/<slug>/', ItemDetailView.as_view(), name='item-detail'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('about/', AboutView.as_view(), name='about'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),

]

# path('itemdetail/<slug>/', add_to_cart, name='add-to-cart'),
#  path('product/<slug>/', ItemDetailView.as_view(), name='product'),

# urlpatterns = [
#     path('', item_list, name='item_list'),
#     path('about', about, name='about'),
#     path('index', index, name='index'),
#     path('cart', cart, name='cart'),
#     path('contact', contact, name='contact'),
#     path('shop_single', shop_single, name='shop_single'),
#     path('thankyou', thankyou, name='thankyou')

# ]

# path('request-refund/', RequestRefundView.as_view(), name='request-refund')
# path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
# OrderSummaryView,
#  path('item_list', item_list, name='item_list'),
