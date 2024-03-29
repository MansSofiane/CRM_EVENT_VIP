from django.shortcuts import render
from rest_framework import generics, filters, viewsets
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
from datetime import datetime, timedelta


from spond import spond
import asyncio



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
    serializer_class = EvenementsPostSerializer
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
######"""  Event Semain et plus et brouillon"
@permission_classes([AllowAny])
class EvenementsAmeliorationView(APIView):
    def get(self, request, format=None):
        deux_derniers_evenements = Evenements.objects.order_by('-date')[:2]
        if len(deux_derniers_evenements) < 2:
            return Response({})

        dernier_evenement, avant_dernier_evenement = deux_derniers_evenements
        amelioration = ((dernier_evenement.benifice - avant_dernier_evenement.benifice) / avant_dernier_evenement.benifice) * 100
        return Response({'amelioration': amelioration})

@permission_classes([AllowAny])
class EvenementsBrouillonListView(generics.ListAPIView):
    serializer_class = EvenementsSerializer
    def get_queryset(self):
        return Evenements.objects.filter(status='Brouillon')

@permission_classes([AllowAny])
class EvenementsAvenirListView(generics.ListAPIView):
    serializer_class = EvenementsSerializer

    def get_queryset(self):
        today = datetime.now().date()
        return Evenements.objects.filter(date__gte=today)

@permission_classes([AllowAny])
class EvenementsSemaineListView(generics.ListAPIView):
    serializer_class = EvenementsSerializer

    def get_queryset(self):
        today = datetime.now().date()
        next_week = today + timedelta(days=7)
        return Evenements.objects.filter(date__range=[today, next_week])
#######EventColaborateur
@permission_classes([AllowAny])
class EventColaborateurByIventViewSet(generics.ListAPIView):
    serializer_class = EventColaborateurSerializer
    def get_queryset(self):
        event_id = self.kwargs.get('id')
        queryset = EventColaborateur.objects.filter(evenements_id=event_id)
        return queryset
    def get(self, request, *args, **kwargs):
        event_id = self.kwargs.get('id')
        queryset = EventColaborateur.objects.filter(Evenements_id=event_id, collaborateur__type='Artist')
        count = queryset.count()
        return Response({
            'count_collaborateur': count,
            'results': EventColaborateurSerializer(queryset, many=True).data
        })
@permission_classes([AllowAny])
class EventColaborateurViewset(viewsets.ModelViewSet):
    queryset = EventColaborateur.objects.all()
    serializer_class = EventColaborateurpostSerializer
     
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
@permission_classes([AllowAny])
class SpondData(APIView):
    def get(self, request, format=None):
        username = 'saidhr20@gmail.com'
        password = '123crmevent'
        group_id = '44031F6EEB37424D9E6CB0ECE68BB624'
        client = spond.Spond(username=username, password=password)
        try:
            
            group = s.get_group(group_id)
            #client.login()
            #events = client.get_events()
            #groups = client.get_groups()
            spond_data = {
                'groups': groups
            }

            return Response(spond_data)
        except Exception as e:
            return Response({'message': f'Erreur lors de la récupération des données à partir de Spond: {str(e)}'}, status=500)