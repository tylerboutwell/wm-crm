from django.urls import path

from .views import views, user_views

app_name = "crm_app"
urlpatterns = [
    path("", user_views.home, name="home"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("recent_orders/", views.recent_orders_generic.as_view(), name="recent orders"),
    path("customer/<int:pk>/", views.CustomerView, name="customer detail"),
    path("customer/<int:pk>/transactions", views.CustomerTransactionsView, name="customer transactions"),
    path("transaction/<int:pk>/", views.TransactionView, name="transaction detail"),
    path("logout/", user_views.logout_user, name="logout"),
]