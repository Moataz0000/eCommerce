from . import views
from django.urls import path



app_name = 'orders'


urlpatterns = [
    path('create/', views.order_create, name='oreder_create'),
    path('pay-order/<int:order_id>/', views.order_pay_by_vodafone, name='pay_order'),
    path('payment-success/<int:order_id>/', views.payment_success, name='payment_success'),
    path('admin/pdf/<int:order_id>/', views.admin_order_pdf, name='admin_order_pdf')

]