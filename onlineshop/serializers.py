 from rest_framework import serializers
 from .models import order
 
 
 class OrderSerializar(serializers.ModelSerializer):
     
    class Meta:
        model = order
        fields = '__all__'