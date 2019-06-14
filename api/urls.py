from django.urls import path, include

from api.views import RateProduct, getAllProducts


urlpatterns = [
    path('rateProduct/',RateProduct.as_view()),
    path('getProducts/',getAllProducts.as_view(),name='get_Products' ),
 ]