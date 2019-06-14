from rest_framework import serializers
from api.models import Products

### Products Serializer ####

class ProductsSerializer(serializers.ModelSerializer):    
   class Meta:
      model = Products
      fields=('name', 'price','rating')  # or '__all__'

