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
    """ get bag variable if exists in session or create if it doesn't """
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        """ update quantity if it already exists in bag """
        bag[item_id] += quantity
    else:
        """ add item to bag """
        bag[item_id] = quantity
    """ overwrite session with updated version """
    request.session['bag'] = bag
    return redirect(redirect_url)