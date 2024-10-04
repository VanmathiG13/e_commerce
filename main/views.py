from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .solr_client import solr_search
from django.db.models import Q
import re

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductByCategory(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)
        
# class SearchAPIView(APIView):
#     def get(self, request):
#         search_query = request.GET.get('search', '')
#         print(f"Received search query: '{search_query}'")  # Debug line

#         # Initialize price range variables
#         price_range = {
#             'min': None,
#             'max': None
#         }

#         # Extract price filters from the query
#         if 'under' in search_query:
#             match = re.search(r'under\s*(\d+)', search_query)
#             if match:
#                 price_range['max'] = float(match.group(1))
#                 search_query = search_query.replace(match.group(0), '').strip()  # Remove price filter from query

#         if 'above' in search_query:
#             match = re.search(r'above\s*(\d+)', search_query)
#             if match:
#                 price_range['min'] = float(match.group(1))
#                 search_query = search_query.replace(match.group(0), '').strip()  # Remove price filter from query

#         # Perform the exact match search
#         try:
#             products = Product.objects.filter(
#                 Q(product_name__icontains=search_query) | Q(description__icontains=search_query)
#             ).distinct()  # Ensure unique results
            
#             serializer = ProductSerializer(products, many=True)
#             return Response({'results': serializer.data})

#         except Exception as e:
#             print(f"Error during search: {e}")  # Debug line
#             return Response({'error': 'An error occurred during the search.'}, status=500)



class SearchAPIView(APIView):
    def get(self, request):
        search_query = request.GET.get('search', '')
        print(f"Received search query: '{search_query}'")  # Debug line

        # Initialize price range variables
        price_range = {
            'min': None,
            'max': None
        }

        # Extract price filters from the query (under/above)
        if 'under' in search_query:
            match = re.search(r'under\s*(\d+)', search_query)
            if match:
                price_range['max'] = float(match.group(1))
                search_query = search_query.replace(match.group(0), '').strip()  # Remove price filter from query

        if 'above' in search_query:
            match = re.search(r'above\s*(\d+)', search_query)
            if match:
                price_range['min'] = float(match.group(1))
                search_query = search_query.replace(match.group(0), '').strip()  # Remove price filter from query

        # Split search query into keywords
        keywords = search_query.split()

        # Build the query
        product_query = Q()
        for keyword in keywords:
            product_query |= Q(product_name__icontains=keyword) | Q(description__icontains=keyword)

        # Apply price filtering if applicable
        if price_range['min'] is not None:
            product_query &= Q(discounted_price__gte=price_range['min'])
        if price_range['max'] is not None:
            product_query &= Q(discounted_price__lte=price_range['max'])

        try:
            # Fetch the products matching the query
            products = Product.objects.filter(product_query).distinct()

            # Serialize and return the products
            serializer = ProductSerializer(products, many=True)
            return Response({'results': serializer.data})

        except Exception as e:
            print(f"Error during search: {e}")  # Debug line
            return Response({'error': 'An error occurred during the search.'}, status=500)