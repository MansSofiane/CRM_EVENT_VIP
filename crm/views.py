from django.shortcuts import render
from rest_framework import generics, filters
from .models import *
from .serializers import *

from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticated
from django.http import JsonResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

class FormulePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


@permission_classes([AllowAny])
class CollaborateursListView(generics.ListAPIView):
    queryset = Collaborateurs.objects.all()
    serializer_class = CollaborateursSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nom','prenom','type','specialite']
    pagination_class = FormulePagination

@permission_classes([AllowAny])
class ListCollaborateur(generics.RetrieveAPIView):
    queryset = Collaborateurs.objects.all()
    serializer_class = CollaborateursSerializer
    pagination_class = FormulePagination

    def get_object(self):
        try:
            id = self.kwargs['id']
            return Collaborateurs.objects.get(id=id)
        except Collaborateur.DoesNotExist:
            raise Http404
@permission_classes([AllowAny])
class CollaborateurRegistrationView(CreateAPIView):
    serializer_class = CollaborateursSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Collaborateur registered  successfully',
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

@permission_classes([AllowAny])
class CollaborateursDetail(generics.RetrieveAPIView):
    queryset = Collaborateurs.objects.all()
    serializer_class = CollaborateursSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
######
@permission_classes([AllowAny])
class ClientsListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nom_societe','adresse','contact_email']
    pagination_class = FormulePagination

@permission_classes([AllowAny])
class ListClient(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = FormulePagination

    def get_object(self):
        try:
            id = self.kwargs['id']
            return Client.objects.get(id=id)
        except Client.DoesNotExist:
            raise Http404
@permission_classes([AllowAny])
class ClientRegistrationView(CreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Client registered  successfully',
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)
@permission_classes([AllowAny])
class ClientDetail(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
####
class OptionListView(generics.ListAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    pagination_class = FormulePagination
@permission_classes([AllowAny])
class ListOption(generics.RetrieveAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    pagination_class = FormulePagination

    def get_object(self):
        try:
            Option_id = self.kwargs['id']
            return Option.objects.get(id=Option_id)
        except Option.DoesNotExist:
            raise Http404
class OptionRegistrationView(CreateAPIView):
    serializer_class = OptionSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Option registered  successfully',
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

@permission_classes([AllowAny])
class OptionDetail(generics.RetrieveAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
############
@permission_classes([AllowAny])
class FormulesListView(generics.ListAPIView):
    queryset = Formules.objects.all()
    serializer_class = FormulesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['prix','titre']
    pagination_class = FormulePagination
@permission_classes([AllowAny])
class ListFormules(generics.RetrieveAPIView):
    queryset = Formules.objects.all()
    serializer_class = FormulesSerializer
    pagination_class = FormulePagination

    def get_object(self):
        try:
            id = self.kwargs['id']
            return Formules.objects.get(id=id)
        except Formules.DoesNotExist:
            raise Http404

@permission_classes([AllowAny])
class FormulesRegistrationView(CreateAPIView):
    serializer_class = FormulesSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Formules registered  successfully',
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

@permission_classes([AllowAny])
class FormulesDetail(generics.RetrieveAPIView):
    queryset = Formules.objects.all()
    serializer_class = FormulesSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
########""
@permission_classes([AllowAny])
class EvenementsListView(generics.ListAPIView):
    queryset = Evenements.objects.all()
    serializer_class = EvenementsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nom','status','lieu','date']
    pagination_class = FormulePagination
@permission_classes([AllowAny])
class ListEvenements(generics.RetrieveAPIView):
    queryset = Evenements.objects.all()
    serializer_class = EvenementsSerializer
    pagination_class = FormulePagination

    def get_object(self):
        try:
            id = self.kwargs['id']
            return Evenements.objects.get(id=id)
        except Evenements.DoesNotExist:
            raise Http404
@permission_classes([AllowAny])
class EvenementsRegistrationView(CreateAPIView):
    serializer_class = EvenementsSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Evenements registered  successfully',
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

@permission_classes([AllowAny])
class EvenementsDetail(generics.RetrieveAPIView):
    queryset = Evenements.objects.all()
    serializer_class = EvenementsSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#########""
@permission_classes([AllowAny])
class PrestationsListView(generics.ListAPIView):
    queryset = Prestations.objects.all()
    serializer_class = PrestationSerializer
    pagination_class = FormulePagination
@permission_classes([AllowAny])
class ListPrestations(generics.RetrieveAPIView):
    queryset = Prestations.objects.all()
    serializer_class = PrestationSerializer
    pagination_class = FormulePagination
    def get_object(self):
        try:
            id = self.kwargs['id']
            return Prestations.objects.get(id=id)
        except Prestations.DoesNotExist:
            raise Http404
@permission_classes([AllowAny])
class PrestationsRegistrationView(CreateAPIView):
    serializer_class = PrestationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Prestations registered  successfully',
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)
@permission_classes([AllowAny])
class PrestationsDetail(generics.RetrieveAPIView):
    queryset = Prestations.objects.all()
    serializer_class = PrestationSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
