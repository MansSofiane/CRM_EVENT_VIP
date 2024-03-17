from rest_framework import serializers
from .models import *

class CollaborateursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborateurs
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'
        #fields = ['nom_option', 'description', 'cout_additionnel']

class FormulesSerializer(serializers.ModelSerializer):
    option = serializers.SerializerMethodField()
    class Meta:
        model = Formules
        fields = '__all__'
        #fields = ['prix', 'titre', 'option']
    def get_option(self, obj):
        option = obj.option
        return OptionSerializer(option).data

class EvenementsSerializer(serializers.ModelSerializer):
    collaborateur = serializers.SerializerMethodField()
    formules = serializers.SerializerMethodField()
    client = serializers.SerializerMethodField()
    class Meta:
        model = Evenements
        fields = '__all__'
    def get_collaborateur(self, obj):
        collaborateur = obj.collaborateur
        return CollaborateursSerializer(collaborateur).data
    def get_client(self, obj):
        client = obj.client
        return ClientSerializer(client).data
    def get_formules(self, obj):
        formules = obj.formules
        return FormulesSerializer(formules).data

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
class PrestationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestations
        fields = '__all__'