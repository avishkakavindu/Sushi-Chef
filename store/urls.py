from django.contrib.auth import views as auth_views
from django.urls import path

from store import views

urlpatterns = [
    path('', views.home, name='index'),
    path('login/', views.login, name='login'),
    path('register', views.register, name='register'),
    path('activate/<str:uidb64>/<str:token>/', views.email_verification, name='activate'),

    path(
        'password_reset',
        auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',
                                             html_email_template_name="registration/password_reset_email.html",
                                             email_template_name='registration/password_reset_email.html',
                                             ),
        name='password_reset'
    ),  # allows a user to reset their password by generating a one-time use link
    path(
        'password_reset_done',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),  # after password reset email sent
    path(
        'password_reset_confirm/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),  # present a form to enter new password
    path(
        'password_reset_complete',
        auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'
    ),  # inform success

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
    path('payhere-detail', views.payhere, name='payhere-detail'),

    path('about', views.about, name='about'),
    path('feedback', views.feedback, name='feedback')
]
