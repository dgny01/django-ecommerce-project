from django.shortcuts import render, redirect,get_object_or_404
from .models import CartItem,Order,Product
from django.views import View
from users.models import UserProfile

# Create your views here.

class AddToCartView(View):
    def post(self, request, product_id):
        if not request.user.is_authenticated:
            return redirect("users:login")

        product = Product.objects.get(id=product_id)
        user_profile = UserProfile.objects.get(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(user=user_profile, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('products:product-detail',pk=product.id)

class CartDetailView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("users:login")

        user_profile = UserProfile.objects.get(user=request.user)
        items = CartItem.objects.filter(user=user_profile)

        total = sum([item.get_total_price() for item in items])
        return render(request, 'cart/cart_detail.html', {'items': items, 'total': total})
    
    def post(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        item_id = request.POST.get('remove_item')  # Formdan gelen ürün id'si
        if item_id:
            cart_item = get_object_or_404(CartItem, id=item_id, user=user_profile)
            cart_item.delete()
        return redirect('cart:cart-detail')


class CheckOutView(View):
    def post(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        items = CartItem.objects.filter(user=user_profile)

        if not items.exists():
            return redirect("products:product-list")

        total = sum([item.get_total_price() for item in items])
        order = Order.objects.create(user=user_profile, total_price=total)
        order.items.set(items)
        items.delete()
        return render(request, 'cart/checkout_success.html', {'order': order})
