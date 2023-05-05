from django.urls import path, include
from . import views

urlpatterns = [
    # Pagina inicial:
    path('', views.index, name='index'),
    # Url do campo de pesquisa:
    path('busca/', views.busca, name='busca'),
    # Pagina de ver os detalhes do contato:
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),

]