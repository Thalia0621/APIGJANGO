from django.contrib import admin
from django.urls import path
from tienda import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
#router=DefaultRouter()
#router.register('tienda',categoryViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('categories/', views.categorieslist ),
    path('categories/<int:id>', views.detailcate),
    path('customers/', views.customerslist ),
    path('customers/<int:id>', views.customersdetail),
    path('products/', views.productslist ),
    path('products/<int:id>', views.productsdetail),
    path('order/', views.orderlist ),
    path('order/<int:id>', views.orderdetail),
    path('orderDetail/', views.orderDetaillist ),
    path('orderDetail/<int:id>', views.orderDetaildetail),

]

