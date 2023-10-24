# pressOne

## Task description

I was presented with an endpoint that was throwing error and task with the responsiblity of fixing it accordingly

the problematic code
```
# Problematic API written in DRF class-based view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer

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
```

the first thing I noticed was two return statements in the post method which would result in an error. To fix this I removed the second return statement and added a validation using the serializer's is_valid() method. That way, I can check if the data is valid and return the appropriate response.

For the get method, there was no validation or error handling. To make it more robust, I added a try/except block to handle any exceptions while retrieving the item by id. If an item is not found, it returns a 404 response.


I made up a Django boilerplate app so as to properly run and test the app.

I also added 5 unit tests to test the GET and POST methods.

___

Please run the following codes
* `python manage.py runserver` to start the development server
* `python manage.py test` to run the unit tests
