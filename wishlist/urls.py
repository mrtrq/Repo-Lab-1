from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import getXML
from wishlist.views import getJSON
from wishlist.views import getIdBasedJSON
from wishlist.views import getIdBasedXML
from wishlist.views import register
from wishlist.views import login_user
from wishlist.views import logout_user

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', getXML, name='getXML'),
    path('json/', getJSON, name='getJSON'),
    path('xml/<int:id>', getIdBasedXML, name='getIdBasedXML'),
    path('json/<int:id>', getIdBasedJSON, name='getIdBasedJSON'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

]