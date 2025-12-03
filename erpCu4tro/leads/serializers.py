from rest_framework import serializers
from .models import Lead
from clients.models import Client
from django.contrib.auth.models import User
class LeadSerializer(serializers.ModelSerializer):
    operator= serializers.PrimaryKeyRelatedField(  
        queryset=User.objects.all(),
    )
    client = serializers.PrimaryKeyRelatedField(  
        queryset=Client.objects.all(),
        required=False,
        allow_null=True,
    )    
    class Meta:
        fields =  ["email", "workflow_status", "operator", "client"]
        model = Lead