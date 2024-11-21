# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, Wishlist
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .forms import CustomSignupForm

def signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = CustomSignupForm()
    return render(request, 'signup.html', {'form': form})

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)  # Log the user out
    return redirect('login')  

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_details.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    print(f"Cart items for user {request.user}: {Cart.objects.filter(user=request.user)}")
    
    return redirect('cart')

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('wishlist')

@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})

@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cart
from .models import Order

from django.shortcuts import render, redirect
from .models import Cart, Order

from django.shortcuts import render, redirect
from .models import Cart, Order

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        # Get shipping details from the form
        address = request.POST['address']
        phone = request.POST['phone']

        # Create Order entries for each cart item
        for item in cart_items:
            Order.objects.create(
                user=request.user,
                product=item.product,
                quantity=item.quantity,
                address=address,
                phone=phone,
                total_price=item.product.price * item.quantity
            )

        # Clear the user's cart after checkout
        #cart_items.delete()

        # Redirect to the order confirmation page with the necessary data
        return redirect('order_confirmation')

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

# Ensure the order_confirmation view receives the correct context
@login_required
def order_confirmation(request):
    # Get the cart items for the logged-in user
    cart_items = Cart.objects.filter(user=request.user)

    # If no items in cart, redirect back to cart page
    if not cart_items.exists():
        return redirect('cart')

    # Calculate the total price
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    # Create an Order record for each cart item
    for item in cart_items:
        Order.objects.create(
            user=request.user,
            product=item.product,
            quantity=item.quantity,
            total_price=item.product.price * item.quantity
        )

    # Capture the order summary before deleting the cart items
    order_summary = [
        {
            'product': item.product,
            'quantity': item.quantity,
            'price': item.product.price,
            'total_price': item.product.price * item.quantity
        }
        for item in cart_items
    ]

    # After placing the order, delete the cart items
    cart_items.delete()

    # Pass the order details to the confirmation page
    return render(request, 'order_confirmation.html', {
        'order_summary': order_summary,  # Pass the order summary to the template
        'total_price': total_price
    })
