from django.urls import path
from . import views as movies_views

app_name = "movies"
urlpatterns = [
    path('', movies_views.index, name='index'),
    path('about/', movies_views.about, name='about'),
    path('catalog/', movies_views.catalog, name='catalog'),
    path('contacts/', movies_views.contacts, name='contacts'),
    path('details/', movies_views.details, name='details'),
    path('forgot/', movies_views.forgot_password, name='forgot_password'),
    path('profile/', movies_views.profile, name='profile'),
    path('signin/', movies_views.signin, name='signin'),
    path('signup/', movies_views.signup, name='signup'),
    path('404/', movies_views.error_404, name='error_404'),
]
