"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import  views
urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('feedback/',views.view_feedback,name="feedback"),
    path('delete_feedback/<email>',views.detete_feedback,name="delete_feedback"),
    # path('price/',views.price,name="price"),
    path('products/',views.products,name="products"),
    # path('single/',views.single,name="single"),
    path('usignup/',views.user_signup,name="usignup"),
    path('login/',views.login,name="login"),
    path('uindex/', views.user_index, name="uindex"),
    path('ulogout/',views.user_logout,name="ulogout"),

    #admin
    # path('alog/',views.alog,name="alog"),
    path('aindex/',views.aindex,name="aindex"),
    path('alogout/',views.admin_logout,name="alogout"),
    path('uabout/',views.uabout,name="uabout"),
    path('ucontact/',views.ucontact,name="ucontact"),


    path('addproducts/',views.add_products,name="addproducts"),
    path('viewproducts/',views.view_admin_products,name="viewproducts"),

    path('updateproducts/',views.update_product,name="updateproducts"),
    path('update/<int:id>',views.update,name="update"),
    path('update1/',views.update1,name="update1"),

    path('delete_products/',views.delete_pro,name="delete_products"),
    path('del1/<pname>',views.del1,name="del1"),
    path('user_products/',views.view_user_pro,name="user_products"),
    path('placeorder/<int:id>',views.placeorder,name="placeorder"),
    # path('placeorder/',views.placeorder,name="placeorder"),
    path('bookings/',views.bookings,name="bookings"),
    # path('myorder/',views.myorder,name="myorder"),
    # path('view_myorder/',views.view_myorder,name="view_myorder"),
    path('cancelorder/',views.cancellings,name="cancelorder"),
    path('cancel/<int:id>',views.cancel,name="cancel"),
    path('payment/',views.paypal_pay,name="payment"),
    path('pay/',views.pay,name="pay"),
    path('cart1/<int:id><user>',views.cart1,name="cart1"),
    path('cart/',views.cart2,name="cart"),
    path('del_cart/<int:id>',views.del_cart,name="del_cart"),
    path('view_book/',views.view_book,name="view_book"),
    path('view_cancel/',views.view_cancel,name="view_cancel")








]
