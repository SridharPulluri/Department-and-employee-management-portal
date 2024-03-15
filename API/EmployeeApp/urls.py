# from django.conf.urls import url
# from EmployeeApp import views

# urlpatterns = [
#     url(r'^ department/$',views.departmentApi),
#     url(r'^ department/([0-9]+)$', views.departmentApi)
# ]

from django.urls import path, re_path
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('department/', views.departmentApi),
    re_path(r'^department/([0-9]+)$', views.departmentApi),
    
    path('employee/', views.employeeApi),
    re_path(r'^employee/([0-9]+)$', views.employeeApi),

    path('SaveFile',views.SaveFile)
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
