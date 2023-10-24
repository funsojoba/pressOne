from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer



# Problematic API written in DRF class-based view
"""
class ItemAPI(APIView):
    def get(self, request, item_id):
        item = Item.objects.get(id=item_id)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""


# Corrected endpoint
class ItemAPI(APIView):
    def get(self, request, item_id=None):
        #NOTE: I believe there's a existing pattern to the code base 
        # I'm just using this approach to allow for my unit test to pass, getting and retrieving 
        # item in the same function
        if item_id:
            try:
                item = Item.objects.get(id=item_id)
                serializer = ItemSerializer(item)
                return Response(serializer.data)
            except Item.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Item not found"})
        else:
            items = Item.objects.all()
            serializer = ItemSerializer(items, many=True)
            return Response(serializer.data)


    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data={'message': "item created successfuly"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)