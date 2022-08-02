from django.urls import path #ADD FOR ME
from . import views #ADD FOR ME
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPageView
from django.contrib.auth.views import LogoutView
#No se creo una view para el logout simplemente se importo la clase aqui y se agrego la url el cual recibe como parametro a donde ira el usuario al solicitar la url de logout

#ADD FOR ME
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name= 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name= 'logout'),
    #next_page hace referencia a donde se redirigira al usuario cuando haga logout

    path('register/', RegisterPageView.as_view(), name= 'register'),

    path('', TaskList.as_view(), name= 'tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name= 'task'),
    #Esta ultima url seria con task y el primary key de la palabra
    path('task-create/', TaskCreate.as_view(), name= 'task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name= 'task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name= 'task-delete'),
]
