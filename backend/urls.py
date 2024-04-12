from django.urls import path
from backend import views
urlpatterns = [
    path('index/',views.index,name="index"),
    path('category/',views.category,name="category"),
    path('save/',views.save,name="save"),
    path('disp/',views.disp,name="disp"),
    path('edit/<int:cid>/',views.edit,name="edit"),
    path('update/<int:cid>/',views.update,name="update"),
    path('delete/<int:cid>/',views.delete,name="delete"),
    path('prod/', views.prod, name="prod"),
    path('psave/', views.psave, name="psave"),
    path('pdisp/',views.pdisp,name="pdisp"),
    path('pedit/<int:pid>/', views.pedit, name="pedit"),
    path('pupdate/<int:pid>/', views.pupdate, name="pupdate"),
    path('pdelete/<int:pid>/', views.pdelete, name="pdelete"),
    path('admin/',views.adlog,name="admin"),
    path('alog/',views.alog,name="alog"),
    path('adlogout/',views.adlogout,name="adlogout"),
    path('contview/',views.contview,name="contview"),
    path('cdel/<int:cid>/',views.cdel,name="cdel"),
]