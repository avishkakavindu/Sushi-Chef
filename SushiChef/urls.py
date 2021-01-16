"""SushiChef URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from store import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),

    path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),             # allows a user to reset their password by generating a one-time use link
    path('password_reset_done', auth_views.PasswordChangeDoneView.as_view(), name='password_reset_done'),   # after password reset email sent
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # present a form to enter new password
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),    # inform success


    path('profile', views.profile, name="profile"),
    path('order_history', views.order_history, name='order_history'),
    path('order/<str:order_id>', views.order, name='order'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('my_reviews', views.review, name='review'),
    path('my_coupons', views.coupon, name='coupon'),

    path('menu', views.menu, name='menu'),
    path('promo', views.promo, name='promo'),
    path('product/<str:product_id>', views.product_detail, name="product"),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)