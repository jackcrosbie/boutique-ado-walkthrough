from django.shortcuts import render, redirect

# Create your views here.
def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


""" submit form to this view with item_id and quantity """
def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    """ get bag variable if exists in session or create if it doesn't """
    bag = request.session.get('bag', {})

    """ single item id for each item but can still track sizes """
    if size:
        """ if an item is already in the bag need to check if same item with same id and size exists and then increment"""
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity


    """ overwrite session with updated version """
    request.session['bag'] = bag
    return redirect(redirect_url)