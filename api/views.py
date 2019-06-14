from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from api.models import Products, Rating
from rest_framework.response import Response
from rest_framework import status
from api.serializers import  ProductsSerializer
from django.db.models import Sum

# Create your views here.

#Rate Product API
class RateProduct(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self,request):
		user = request.user
		rating = request.data.get('rating')
		product_id =request.data.get('product_id')
		if rating and product_id:
			try:
				product = Products.objects.get(id=product_id)
			except Exception as e:
				return Response(data=[{"message":"Please provide valid product id"}],status=status.HTTP_400_BAD_REQUEST)
			product_rated = Rating.objects.filter(user=user).filter(product=product)
			if product_rated:
				return Response(data=[{"message":"You have already rated this product"}],status=status.HTTP_400_BAD_REQUEST)
			new_rating =Rating.objects.create(user=user, rating=rating, product=product)
			#Calculate average rating
			rating_count =  Rating.objects.filter(product=product).count()
			sum_rating = Rating.objects.filter(product=product).aggregate(Sum('rating'))['rating__sum']
			average_rating = float(sum_rating/rating_count)
			#update product rating
			product.rating = average_rating
			product.save()
			return Response(data=[{"message":"The product has been successfully rated"}] ,status=status.HTTP_200_OK)
		else:
			return Response(data=[{"message":"Please provide the required params"}],status=status.HTTP_400_BAD_REQUEST)


#Get All Products API
class getAllProducts(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self,request,format=None):
		queryset = Products.objects.all()
		serializer = ProductsSerializer(queryset, many=True)
		return Response(serializer.data)

