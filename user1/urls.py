from django.urls import path
from . import views


urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"), 
    path('home/',views.home,name='home'),
    path('menu/',views.menu,name="menu"),
    path('allproduct/',views.allproduct,name="allproduct"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('orders/',views.orders,name="orders"),
    path('product/',views.product,name="product"),
    path('addtocart/',views.addtocart,name="addtocart"),
    path('summary/',views.summary,name="summary"),
    path('update_cart_quantity/', views.update_cart_quantity, name='update_cart_quantity'),
    path('payment/', views.payment, name='payment'),
    path('place_order/', views.place_order, name='place_order'),
]
