from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
# from django.contrib.sessions.models import Session
from django.http import JsonResponse
from .middlewares import auth1,loggedin1,prevent_direct_access
from .models import flavourpaan,sweetpaan,specialpaan,paanaroma,Cart,Address,Myorder,Contact
import json
# Create your views here.

@loggedin1
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        default_data = {'username':'','password1':'','password2':''}
        form = UserCreationForm(initial = default_data)
    return render(request,'auth/signup.html',{'form':form})

@loggedin1
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        default_data = {'username':'','password':''}
        form = AuthenticationForm(initial = default_data)
    return render(request,'auth/login.html',{'form':form})

@prevent_direct_access
def logout_view(request):
    logout(request)

    
    return redirect('login')

def home(request):
    meethapaan_objects = sweetpaan.objects.filter(name='Meetha Paan')
    firepaan_objects = specialpaan.objects.filter(name='Fire Paan')
    kesarpaan_objects = flavourpaan.objects.filter(name='Kesar Paan')
    return render(request,'app/home.html',{'meethapaan':meethapaan_objects,'firepaan':firepaan_objects,'kesarpaan':kesarpaan_objects})

def menu(request):
    flavourpaan_objects = flavourpaan.objects.all()
    sweetpaan_objects = sweetpaan.objects.all()
    paanaroma_objects = paanaroma.objects.all()
    special_objects = specialpaan.objects.all()

    return render(request,'app/menu.html',{'flavour_paan':flavourpaan_objects,'sweet_paan':sweetpaan_objects,'aroma_paan':paanaroma_objects,'special_paan':special_objects})

@prevent_direct_access
def allproduct(request):
    product_name = request.GET.get('name','')
    def split1(paan_name):
        for i in paan_name:
            i.offers = i.offers.split(",")
        return paan_name

    if product_name == 'flavourpaan':
        flavourpaan_objects = flavourpaan.objects.all()
        split1(flavourpaan_objects)
        return render(request,'app/allproduct.html',{'paan':flavourpaan_objects,'paan_name':product_name})
    elif product_name == 'sweetpaan':
        sweetpaan_objects = sweetpaan.objects.all()
        split1(sweetpaan_objects)
        return render(request,'app/allproduct.html',{'paan':sweetpaan_objects,'paan_name':product_name})
    elif product_name == 'paanaroma':
        paanaroma_objects = paanaroma.objects.all()
        split1(paanaroma_objects)
        return render(request,'app/allproduct.html',{'paan':paanaroma_objects,'paan_name':product_name})
    elif product_name == 'specialpaan':
        specialpaan_objects = specialpaan.objects.all()
        split1(specialpaan_objects)
        return render(request,'app/allproduct.html',{'paan':specialpaan_objects,'paan_name':product_name})

def about(request):
    return render(request,'app/about.html')

@auth1
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('contactname','')
        email = request.POST.get('contactemail','')
        phone = request.POST.get('contactphone','')
        address = request.POST.get('contactaddress','')
        query = request.POST.get('contactquery','')
        
        if request.user.is_authenticated:
            Contact.objects.create(user = request.user ,name=name,email=email,phone=phone,address=address,query=query)
 
    return render(request,'app/contact.html')

@prevent_direct_access
def product(request):
    paan_name = request.GET.get('paan_name','')
    paan_type = request.GET.get('paan_type','')
    def benefit1(paan_name):
        for i in paan_name:
            i.benefit = i.benefit.split(".")
        return paan_name
    def offer1(paan_name):
        for i in paan_name:
            i.offers = i.offers.split(",")
        return paan_name
    if paan_name == 'flavourpaan':
        filtered_objects = flavourpaan.objects.filter(name=paan_type)
        benefit1(filtered_objects)
        offer1(filtered_objects)
        return render(request,'app/product.html',{'p_details':filtered_objects,'paan_name':paan_name})
    elif paan_name == 'sweetpaan':
        filtered_objects = sweetpaan.objects.filter(name=paan_type)
        benefit1(filtered_objects)
        offer1(filtered_objects)
        return render(request,'app/product.html',{'p_details':filtered_objects,'paan_name':paan_name})
    elif paan_name == 'paanaroma':
        filtered_objects = paanaroma.objects.filter(name=paan_type)
        benefit1(filtered_objects)
        offer1(filtered_objects)
        return render(request,'app/product.html',{'p_details':filtered_objects,'paan_name':paan_name})
    elif paan_name == 'specialpaan':
        filtered_objects = specialpaan.objects.filter(name=paan_type)
        benefit1(filtered_objects)
        offer1(filtered_objects)
        return render(request,'app/product.html',{'p_details':filtered_objects,'paan_name':paan_name})

@prevent_direct_access   
def addtocart(request):
    if request.method == 'GET':
        paan_name = request.GET.get('paan_name','')
        paan_id = request.GET.get('paan_id','')
        def authenticateuser_addtocart():
           
            name = ''
            price = ''
            image = ''
            quantity = 1
            for i in filtered_object:
                name = i.name
                price = i.price
                image = i.image

            if request.user.is_authenticated:
                user = request.user
                check = Cart.objects.filter(user=user,name=name)
                if not check.exists():
                    Cart.objects.create(user=user, name=name, price=price, image=image, quantity=quantity)

            else:
                return redirect('login')


        if paan_name == 'flavourpaan':
            filtered_object = flavourpaan.objects.filter(id=paan_id)
            authenticateuser_addtocart()  
        elif paan_name == 'sweetpaan':
            filtered_object = sweetpaan.objects.filter(id=paan_id)
            authenticateuser_addtocart()
        elif paan_name == 'paanaroma':
            filtered_object = paanaroma.objects.filter(id=paan_id)
            authenticateuser_addtocart()
        elif paan_name == 'specialpaan':
            filtered_object = specialpaan.objects.filter(id=paan_id)
            authenticateuser_addtocart()


    if request.user.is_authenticated:
        filteruser = Cart.objects.filter(user=request.user)
    else:
        filteruser = None
        return redirect('login')
    
    check = Cart.objects.filter(user=request.user)
    if(not check):
        return redirect('home')
    return render(request,'app/addtocart.html',{'filteruser':filteruser})


@prevent_direct_access
def summary(request):
    showaddress = Address.objects.filter(user=request.user)
    if request.method == 'POST':
        nameaddress = request.POST.get('name-address','')
        phoneaddress = request.POST.get('phone-address','')
        addressaddress = request.POST.get('address-address','')
        address2address = request.POST.get('address2-address','')
        cityaddress = request.POST.get('city-address','')
        stateaddress = request.POST.get('state-address','')
        zipaddress = request.POST.get('zip-address','')
        if request.user.is_authenticated:
            user = request.user
            Address.objects.create(user=user, name=nameaddress, phone=phoneaddress, address=addressaddress, address2=address2address,city=cityaddress,state=stateaddress,zip=zipaddress) 
    return render(request,'app/summary.html',{'showaddress':showaddress})

@prevent_direct_access
def update_cart_quantity(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))

        if quantity == 0:
            try:
                order = Cart.objects.get(pk=product_id)
                order.delete()
                return JsonResponse({'success': True})
            except Cart.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Order does not exist'})
                
        
        return JsonResponse({'success': True})  # Quantity is not zero, no action required

    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@prevent_direct_access
def payment(request):
    return render(request,'app/payment.html')


@auth1
def orders(request):
    myorders = Myorder.objects.filter(user=request.user)
    
    return render(request,'app/orders.html',{'orders':myorders})

@prevent_direct_access
def place_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            paancart = data.get('paancart')

            for item in paancart.values():
                address_instance = Address.objects.get(id=item['addressid'])
                Myorder.objects.create(
                    user=request.user,
                    p_id=item['productid'],
                    address=address_instance,
                    p_name=item['productname'],
                    p_price=item['price'],
                    p_quantity=item['quantity'],
                    p_image=item['image'],
                    p_deliverytime = item['deliverytime'],
                )

            carts = Cart.objects.filter(user=request.user)
            for cart in carts:
                cart.delete()

            return JsonResponse({'message': 'Order placed successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid request body'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


