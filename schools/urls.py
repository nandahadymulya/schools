from django.contrib import admin
from django.urls import path
from schools import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/', views.api),
    path('api/schools/', views.school_list),
    path('api/schools/<int:id>', views.school_detail),
    path('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)
