from django.urls import path
from .views import *

urlpatterns = [
    path('collaborateurs/', CollaborateursListView.as_view(), name='collaborateurs-list'),
	path('collaborateurs/<int:id>/', ListCollaborateur.as_view(), name='collaborateurs-detail'),
	path('ADDcollaborateurs', CollaborateurRegistrationView.as_view(), name='collaborateurs-ADD'),
	path('editcollaborateurs/<int:pk>/', CollaborateursDetail.as_view(), name='clients-edit'),


    path('options/', OptionListView.as_view(), name='options-list'),
    path('options/<int:id>/', ListOption.as_view(), name='options-detail'),
    path('ADDoptions/', OptionRegistrationView.as_view(), name='options-ADD'),
    path('editoptions/<int:pk>/', OptionDetail.as_view(), name='clients-edit'),

    path('formules/', FormulesListView.as_view(), name='formules-list'),
    path('formules/<int:id>/', ListFormules.as_view(), name='formules-detail'),
    path('ADDformules/', FormulesRegistrationView.as_view(), name='formules-ADD'),
    path('editformules/<int:pk>/', FormulesDetail.as_view(), name='clients-edit'),

    path('evenements/', EvenementsListView.as_view(), name='evenements-list'),
    path('evenements/<int:id>/', ListEvenements.as_view(), name='evenements-detail'),
    path('ADDevenements/', EvenementsRegistrationView.as_view(), name='evenements-ADD'),
	path('editevenements/<int:pk>/', EvenementsListView.as_view(), name='clients-edit'),


    path('ADDclients/', ClientRegistrationView.as_view(), name='clients-ADD'),
    path('clients/', ClientsListView.as_view(), name='clients-list'),
    path('clients/<int:id>/', ListClient.as_view(), name='clients-detail'),
    path('editclient/<int:pk>/', ClientDetail.as_view(), name='clients-edit'),

    path('ADDPrestations/', PrestationsRegistrationView.as_view(), name='Prestations-ADD'),
    path('Prestations/', PrestationsListView.as_view(), name='Prestations-list'),
    path('Prestations/<int:id>/', ListPrestations.as_view(), name='Prestations-detail'),
	path('editPrestations/<int:pk>/', PrestationsDetail.as_view(), name='clients-edit'),


]