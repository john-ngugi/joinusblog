from . import views
from django.urls import path
from blogs.views import blogs,postDetail,intro,blogpost1,aboutus
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #path('', blogs, name='home'),
    path('<slug:slug>/', postDetail, name='post_detail'),
    path('blogs',blogs,name='blogs'),
    path('',intro,name='intro'),
    path('blogpost1',blogpost1,name='blogpost1'),
    path('aboutus',aboutus,name='aboutus'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 