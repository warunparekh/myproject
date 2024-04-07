from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404

from .models import Product  # Import your product model
from .serializers import ProductSerializer  # Import your product serializer

class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()  # Fetch all products
        serializer = ProductSerializer(products, many=True)  # Serialize data
        return Response(serializer.data)  # Return response with serialized data

def product_list(request):
    products = Product.objects.all().order_by('id')  # Fetch all products, order by ID
    for product in products:
        if product.discount_data:
            discounted_price = product.original_price * (1 - product.discount_data)
            product.discounted_price = discounted_price
    context = {'products': products}
    return render(request, 'shopping/product_list.html', context)


def product_detail(request, product_id): # Accept 'product_id' as parameter
    product = get_object_or_404(Product, pk=product_id) # Use 'product_id' to retrieve the product
    return render(request, 'shopping/product_detail.html', {'product': product})
