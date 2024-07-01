from rest_framework.routers import DefaultRouter
from django.urls import path
from products.views import FAQViewSet, BrandViewSet, BannerViewSet, ProductWeightViewSet , ProductList
from products.views import ProductDetailView, ProductColorViewset, ProductView, CategoryView  # ProductColorView



router = DefaultRouter()
# router.register('products', ProductViewSet, basename='products')
router.register('product-colors', ProductColorViewset, basename='product-colors')
router.register('product-weights', ProductWeightViewSet, basename='product-weights')
# router.register('products-lists', ProductListView, basename='product-lists')
router.register('categories', CategoryView, basename='categories')
router.register('faqs', FAQViewSet, basename='faqs')
router.register('banners', BannerViewSet, basename='banners')
router.register('brands', BrandViewSet, basename='brands')
urlpatterns = router.urls
urlpatterns += [
    path('products-list/', ProductList.as_view(), name='products-list'),
    path("products-detail/<int:pk>/", ProductDetailView.as_view(), name='product-detail'),
    path("products/", ProductView.as_view(), name='products')
]


# TODO = Kairat Sūltan, [28.06.2024 12:18]
# Endi detail product serializeri uchun boshqa huddi shunaqa serializer yangidan yozasiz

# Kairat Sūltan, [28.06.2024 14:06]
# Keyin weights uchun serializer yozib nested qilasiz