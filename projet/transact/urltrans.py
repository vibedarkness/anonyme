from django.contrib import admin
from django.urls import path


from django.urls import path, re_path
from .views import IndexView, TransactionView, ClientView

app_name = 'transact'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('transaction', TransactionView.as_view(), name='transactions'),
    path('client', ClientView.as_view(), name='client'),
]