from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CheckoutForm
from .models import Product, Cart, CartItem, Favorite


def product_list_index(request):
    products = Product.objects.all()
    return render(request, 'product_list_index.html', {'products': products})



def product_list(request):
    # Fetch distinct manufacturers and subcategories for filter options
    manufacturers = Product.objects.values_list('manufacturer', flat=True).distinct()
    sub_categories = Product.objects.values_list('sub_category', flat=True).distinct()

    # Get selected manufacturers and subcategories from request
    selected_manufacturers = request.GET.getlist('manufacturer')
    selected_sub_categories = request.GET.getlist('sub_category')

    # Start with all products
    products = Product.objects.all()

    # Filter products by selected manufacturers and subcategories
    if selected_manufacturers:
        products = products.filter(manufacturer__in=selected_manufacturers)
    if selected_sub_categories:
        products = products.filter(sub_category__in=selected_sub_categories)

    # Paginate the product list
    paginator = Paginator(products, 12)  # Show 12 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Prepare context for the template
    context = {
        'page_obj': page_obj,
        'manufacturers': manufacturers,
        'sub_categories': sub_categories,
        'selected_manufacturers': selected_manufacturers,
        'selected_sub_categories': selected_sub_categories,
    }

    # Check if the request is an AJAX request for partial updates
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'product_grid.html', context)
    else:
        return render(request, 'product_list.html', context)

from bs4 import BeautifulSoup

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    products = Product.objects.all()

    # Clean up description using Beautiful Soup
    if product.short_description:
        soup = BeautifulSoup(product.short_description, 'html.parser')
        cleaned_description = soup.get_text()  # Extract text without HTML tags
    else:
        cleaned_description = ''

    return render(request, 'product_detail.html', {'product': product, 'products': products, 'desc': cleaned_description})

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    session_id = request.session.session_key
    if not session_id:
        request.session.create()
        session_id = request.session.session_key

    cart, _ = Cart.objects.get_or_create(session_id=session_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

def cart_detail(request):
    session_id = request.session.session_key
    cart = Cart.objects.filter(session_id=session_id).first()
    total = 0
    cart_items = []
    if cart:
        for item in cart.cartitem_set.all():
            item.subtotal = item.product.price * item.quantity
            total += item.subtotal
            cart_items.append({
                'product': item.product,
                'quantity': item.quantity,
                'subtotal': item.subtotal
            })
    return render(request, 'cart_detail.html', {'cart_items': cart_items, 'total': total})


def remove_from_cart(request, pk):
    session_id = request.session.session_key
    if not session_id:
        return redirect('cart_detail')

    cart = Cart.objects.filter(session_id=session_id).first()
    if cart:
        cart_item = CartItem.objects.filter(cart=cart, product_id=pk).first()
        if cart_item:
            cart_item.delete()

    return redirect('cart_detail')


def add_to_favorites(request, pk):
    product = get_object_or_404(Product, pk=pk)
    session_id = request.session.session_key
    if not session_id:
        request.session.create()
        session_id = request.session.session_key

    Favorite.objects.get_or_create(session_id=session_id, product=product)
    return redirect('favorites_detail')

def favorites_detail(request):
    session_id = request.session.session_key
    favorites = Favorite.objects.filter(session_id=session_id)
    return render(request, 'favorites_detail.html', {'favorites': favorites})


from django.shortcuts import render, redirect
from .forms import CheckoutForm  # Import your CheckoutForm
from .models import Cart  # Import your Cart model


def checkout(request):
    session_id = request.session.session_key
    cart = Cart.objects.filter(session_id=session_id).first()
    total = 0
    cart_items = []
    if cart:
        for item in cart.cartitem_set.all():
            item.subtotal = item.product.price * item.quantity
            total += item.subtotal
            cart_items.append({
                'product': item.product,
                'quantity': item.quantity,
                'subtotal': item.subtotal
            })

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Process the form data
            # For demonstration, assuming saving order logic here

            # Redirect to a success page or process further
            return redirect('order_success')  # Replace 'order_success' with your actual success URL
    else:
        form = CheckoutForm()

    return render(request, 'checkout.html', {'form': form, 'cart_items': cart_items, 'total': total})


from django.db.models import Q


def product_search(request):
    manufacturers = Product.objects.values_list('manufacturer', flat=True).distinct()
    sub_categories = Product.objects.values_list('sub_category', flat=True).distinct()
    query = request.GET.get('q', '').strip()  # Get search query and remove leading/trailing spaces
    if query:
        products = Product.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = Product.objects.none()  # Return empty queryset if query is empty

    print(f"Search Query: '{query}'")  # Debug print to check the search query

    context = {
        'query': query,
        'products': products,
        'manufacturers': manufacturers,
        'sub_categories': sub_categories,
    }
    return render(request, 'product_search.html', context)


def delivery_terms_view(request):
    return render(request, 'delivery_terms.html')

def payment_methods_view(request):
    return render(request, 'payment_methods.html')

def order_information_view(request):
    return render(request, 'order_information.html')

def warranty_claims_view(request):
    return render(request, 'warranty_claims.html')

def online_credit_view(request):
    return render(request, 'online_credit.html')

def discounts_view(request):
    return render(request, 'discounts.html')

def privacy_policy_view(request):
    return render(request, 'privacy_policy.html')

def site_terms_view(request):
    return render(request, 'site_terms.html')

def installation_view(request):
    return render(request, 'installation.html')

def preliminary_survey_view(request):
    return render(request, 'preliminary_survey.html')

def consultation_view(request):
    return render(request, 'consultation.html')

def aircon_maintenance_view(request):
    return render(request, 'aircon_maintenance.html')

def aircon_service_view(request):
    return render(request, 'aircon_service.html')

def projects_view(request):
    return render(request, 'projects.html')


def about_us_view(request):
    # Your logic for rendering the about us page goes here
    return render(request, 'about_us.html')  # Assuming you have a template named 'about_us.html'


def contact_us_view(request):
    # Your logic for rendering the contact us page goes here
    return render(request, 'contact_us.html')  # Assuming you have a template named 'contact_us.html'



def free_inspection_view(request):
    # Your logic for rendering the free inspection page goes here
    return render(request, 'free_inspection.html')  # Assuming you have a template named 'free_inspection.html'



def ac_maintenance_view(request):
    # Your logic for rendering the AC maintenance page goes here
    return render(request, 'ac_maintenance.html')  # Assuming you have a template named 'ac_maintenance.html'

def ac_service_view(request):
    # Your logic for rendering the AC service page goes here
    return render(request, 'ac_service.html')  # Assuming you have a template named 'ac_service.html'

def partners_view(request):
    return render(request, 'partners.html')

def team_view(request):
    return render(request, 'team.html')



def news_view(request):
    return render(request, 'news.html')

def help_view(request):
    return render(request, 'help.html')


def distributors_view(request):
    return render(request, 'distributors.html')

def catalogs_view(request):
    return render(request, 'catalogs.html')


