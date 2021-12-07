from django.contrib import admin
from django.urls import path
from fcuser.views import index
from fcuser.views import RegisterView, LoginView
from product.views import ProductList, ProductCreate
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('product/', ProductList.as_view()),
    path('product/create/', ProductCreate.as_view()),
]