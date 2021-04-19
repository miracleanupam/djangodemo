from cart.models import Cart
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Product
from .forms import ProductForm


# Create your views here.
class Dashboard(ListView):
    """
    View to display the homepage/dashboard.
    """
    model = Product
    template_name = 'product/dashboard.html'

    def get_context_data(self, **kwargs):
        """
        Over-riding the default method to insert custom context data for template rendering
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)

        # To distinguish if this is product list or product detail
        context['is_list_view'] = True

        # Insert context of cart only if user is logged in
        if self.request.user.is_authenticated:
            try:
                # Find the cart associated with the user
                cart = self.request.user.cart
            except:
                # If can't find it, create a cart of the user
                cart = Cart.objects.create(user=self.request.user)

            # Now the user has a cart, add it to the context data
            context['cart'] = cart
        return context

    def get_queryset(self):
        """
        Over-riding method to refine which query set should be used for template rendering
        :return:
        """
        # Get the search params
        query = self.request.GET.get('q')

        # Get the 'sort-by' option selected
        sort_by = self.request.GET.get('sort-by')

        if query is not None:
            filters = Q(name__icontains=query) | Q(product_code__icontains=query) | Q(description__icontains=query)
            result = Product.objects.filter(filters)
        else:
            result = Product.objects.all()

        # If someone intercepts the request and changes the sort-by option to something else
        # Our system might behave poorly, so check if 'sort-by' option is within allowed values
        # If not, assign a default value
        if sort_by in ['name', 'price']:
            result = result.order_by(sort_by)
        else:
            result = result.order_by('name')
        return result


class ProductDetail(DetailView):
    """
    View to see the details of a product
    """
    model = Product
    template_name = 'product/detail.html'

    # By what name should the resulting object be passed to template
    context_object_name = 'prod'

    def get_context_data(self, **kwargs):
        """
        Over-riding method to pass custom context data
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)

        # This view is for detail of a product
        context['is_list_view'] = False
        if self.request.user.is_authenticated:
            try:
                cart = self.request.user.cart
            except:
                cart = Cart.objects.create(user=self.request.user)
            context['cart'] = cart
        return context


class AddProductInSystem(View):
    """
    View to add a product to the system. Only the superuser can access it.
    """
    template_name = 'product/add_product_in_system.html'
    form_class = ProductForm

    def get(self, request, *args, **kwargs):
        """
        Method to serve the form for adding new product
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # If the user is not super-user, return a response
        # For now, I have used a JSON, but we can serve a html page
        # saying something like "Unauthorized" or "Not found"
        # We can create a html template for this and serve it as
        # return render(request, 'html_for_unauthorized.html', context={})
        if not request.user.is_superuser:
            return JsonResponse({'status': 'error', 'data': 'Unauthorized'}, status=401)
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """
        Method to handle the submitted form
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        form = self.form_class(request.POST or None, request.FILES or None)

        if not request.user.is_superuser:
            return JsonResponse({'status': 'error', 'data': 'Unauthorized'}, status=401)

        # If the form is valid, save the form, since it is a model form
        # It will save a new object associated with it
        # And then, redirect to the same page with the form again
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add-product')
        context = {
            form: form
        }
        return render(request, self.template_name, context=context)
