from django.urls import path
from . import views
# urlpatterns = [
#     # path('',views.show,name='show'),
#     path('',views.converter,name='converter'),
#     path('history/',views.all_history,name='history'),
#     from django.urls import path
# from . import views

urlpatterns = [
    path('', views.converter, name='converter'),
    # path('history/', views.history, name='history'),
    path('all_history/', views.all_history, name='all_history'),  # 👈 Add this
    path('clean/', views.clean, name='clean'),  # 👈 Add this
]
