from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from product.models import Product


class AddToCart(View):
    """
    View to add products to the cart
    """
    def post(self, request):
        pk = request.POST.get('pk')
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'error', 'data': 'Unauthenticated'}, status=401)
        cart = request.user.cart
        prod = Product.objects.get(pk=pk)
        if prod not in cart.items.all():
            cart.items.add(prod)
            cart.save()

        cart_json = cart.to_dict()
        return JsonResponse({'status': 'success', 'cart': cart_json}, status=200)


class RemoveFromCart(View):
    """
    View to remove product from a cart
    """
    def post(self, request):
        pk = request.POST.get('pk')
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'error', 'data': 'Unauthenticated'}, status=401)

        cart = request.user.cart
        prod = Product.objects.get(pk=pk)
        if prod in cart.items.all():
            cart.items.remove(prod)
            cart.save()

        cart_json = cart.to_dict()
        return JsonResponse({'status': 'success', 'cart': cart_json}, status=200)


class ShowCartDetail(View):
    """
    View to show details of the cart
    """
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/auth/login')

        cart = request.user.cart
        return render(request, 'cart/cart.html', {'cart': cart})
