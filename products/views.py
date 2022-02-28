from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    # start as none to ensure we don't get an error when loading without a search term
    query = None
    categories = None
    sort = None
    direction = None


    if request.GET:
        # checking if sort is in request and if so the parameters for what happens
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            # keeps original fields name 'name' and allows to sort my lower_name
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    # will sort in descending order. - before makes it descending
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # checking whether it exists in request.GET
        if 'category' in request.GET:
            # split into list at the commas
            categories = request.GET['category'].split(',')
            # using __ means we're looking for the name field of the categories
            products = products.filter(category__name__in=categories)
            # filter categories down to the ones whose names is in the list from the url
            categories = Category.objects.filter(name__in=categories)


        if 'q' in request.GET:
            query = request.GET['q']
            # if query is blank
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            # setting up queries so will target either product name or description depending on search term
            # | = or and the i before contains make the searches case insensitive
            # actually filter products after query
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            
    current_sorting = f'{sort}_{direction}'        

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)
