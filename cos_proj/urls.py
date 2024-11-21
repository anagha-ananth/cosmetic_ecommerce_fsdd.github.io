from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from cos_app.views import add_to_cart, add_to_wishlist, cart, checkout, custom_logout, home, order_confirmation, product_details, wishlist, signup
from cos_app.forms import CustomLoginForm  # Import your custom login form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('product/<int:product_id>/', product_details, name='product_details'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('add-to-wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('cart/', cart, name='cart'),
    path('wishlist/', wishlist, name='wishlist'),
    path('signup/', signup, name='signup'),
    path('logout/', custom_logout, name='logout'),  # Custom logout vie
    path('checkout/', checkout, name='checkout'),
    path('order-confirmation/', order_confirmation, name='order_confirmation'),
    # Login and Logout URLs
    path('login/', 
         LoginView.as_view(
             template_name='login.html',  # Specify the login template
             authentication_form=CustomLoginForm  # Use your custom form
         ), 
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
