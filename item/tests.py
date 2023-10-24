from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item

class ItemAPITest(APITestCase):
    def setUp(self):
        # Create some sample items for testing
        self.item1 = Item.objects.create(name='Item 1', price=30, description='Description 1')
        self.item2 = Item.objects.create(name='Item 2', price= 20, description='Description 2')

    def test_get_item_with_right_id_succeeds(self):
        """
            Test getting an item by id succeeds
        """
        response = self.client.get(f'/api/v1/item/{self.item1.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Item 1")
        self.assertEqual(response.data['price'], "30.00")

    def test_get_item_with_wrong_id_fails(self):
        """
            Test getting an item by wrong id returns 404 error
        """
        response = self.client.get('/api/v1/item/3fb314ca-c691-4cc3-85c9-14f7534a219f')  # Assuming 12345 doesn't exist
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['message'], "Item not found")

    def test_get_all_items_succeeds(self):
        """
            Test getting all items succeeds
        """
        response = self.client.get('/api/v1/item/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_item_succeeds(self):
        """
            Test posting a new item succeeds with correct data
        """
        data = {'name': 'New Item', 'price': 30, 'description': 'New Description'}
        response = self.client.post('/api/v1/item/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_post_item_with_wrong_data_fails(self):
        """
            Test posting a new item fails with incorrect data (missing price)
        """
        data = {'name': 'New Item', 'description': 'New Description'}
        response = self.client.post('/api/v1/item/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['price'], ['This field is required.'])
