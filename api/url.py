from django.conf import settings
from django.conf.urls.static import static
from  django.urls import path
from  . import views

urlpatterns = [
    path('',views.Users.as_view() ,name='login'),
    path('info/',views.Infor.as_view() ,name='info'),
    path('insert/',views.Insert.as_view() ,name='info'),
    path('posting/',views.Posting.as_view() ,name='info'),
    path('addposting/',views.AddPosting.as_view() ,name='info'),
    path('insertposation/',views.Posation.as_view() ,name='info'),
    path('Getposation/',views.Getposation.as_view() ,name='info'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)