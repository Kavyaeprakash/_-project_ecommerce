from django.test import TestCase
from django.urls import reverse,resolve
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.
class Test_Sample(TestCase):
    def setup(self):
        self.client = APIClient
    
    def test_index(self):
        url = reverse('schoolapi:index')
        res = self.client.get(url)
        self.assertEquals(res.data,'congratulations')