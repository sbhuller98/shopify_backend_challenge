from django.test import TestCase
from .models import Images


# Create your tests here.
class ImagesTestCase(TestCase):
    def setUp(self):
        '''Sets up and creates a test Image object.'''
        Images.objects.create(title="test1", category="testcategory")

    def test_Images_Model(self):
        '''Ensures test image has correct title and category.'''
        obj1 = Images.objects.get(title="test1")
        self.assertFalse(obj1 == None)
        self.assertEqual(obj1.category, "testcategory")
    
    def test_index_view(self):
        '''Ensures index view is reachable.'''
        self.client.login(username="shopifyrocks", password="hireme123")
        response = self.client.get('', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_search_view(self):
        '''Ensures search view is reachable.'''
        self.client.login(username="shopifyrocks", password="hireme123")
        response = self.client.post('/search', {"name": "test", "category": "test"}, follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_delete_view(self):
        '''Ensures delete view is reachable.'''
        self.client.login(username="shopifyrocks", password="hireme123")
        response = self.client.post('/deleteImages', {"valuesToDelete": ""}, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_post_view(self):
        '''Ensures post view is reachable.'''
        self.client.login(username="shopifyrocks", password="hireme123")
        response = self.client.post('/postImage', {"title": "", "category": ""}, follow=True)
        self.assertEqual(response.status_code, 200)
