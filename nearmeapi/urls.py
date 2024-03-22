from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from rest_framework.authtoken import views as auth_views
from index.views import UserInfoListCreate, UserInfoDetail, ProductCategoryListCreate, ProductCategoryDetail, ProductListCreate, ProductDetail, \
CustomRegisterView, CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/userinfo/', UserInfoListCreate.as_view(), name='userinfo-list-create'),
    path('api/userinfo/<int:pk>/', UserInfoDetail.as_view(), name='userinfo-detail'),

    path('api/productcategory/', ProductCategoryListCreate.as_view(), name='productcategory-list-create'),
    path('api/productcategory/<int:pk>/', ProductCategoryDetail.as_view(), name='productcategory-detail'),

    path('api/products/', ProductListCreate.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),


    #Access
    path('api/login/', auth_views.obtain_auth_token, name='login'),
    path('api/register/', CustomRegisterView.as_view(), name='register'),
    path('api/logout/', CustomLogoutView.as_view(), name='logout'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns= urlpatterns+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)