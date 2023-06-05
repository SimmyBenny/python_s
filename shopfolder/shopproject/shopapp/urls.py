from django.urls import path,include
from . import views
app_name='shopapp'

urlpatterns = [
    path('',views.allproductcat,name='allproductcat'),
    path('<slug:c_slug>/',views.allproductcat,name='productsbycategory'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatDetail'),
]