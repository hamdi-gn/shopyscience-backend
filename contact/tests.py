from email.policy import HTTP
import json
from urllib import response
from rest_framework.authtoken.models import Token
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory

from rest_framework import status

from .models import Conact
from .serializers import ConactSerializer

# Create your tests here.

class RegistrationTestCase(APITestCase):
    
    def test_registration(self):
        data = {"username": "testcase", "email": "test@test.com", "password1": "TestPassWord11**", "password2": "TestPassWord11**"}
        response = self.client.post("/authentication/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
class ContactViewSetTestCase(APITestCase):
     
    list_url = reverse("contacts-list")
    
    def setUp(self):
        self.user = User.objects.create_user(username="hamdi", password="PassWord123**")
        self.token = Token.objects.create(user=self.user)
        self.api_auth()
        
    def api_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token "+self.token.key)
        
    def test_contact_list_auth(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_contact_list_auth(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        
class GetAllcontactsTest(TestCase):
    """ Test module for GET all contacts API """

    def test_get_all_contacts(self):
        # get API response
        response = self.client.get(reverse('contacts-list'))
        # get data from db
        contacts = Conact.objects.all()
        serializer = ConactSerializer(contacts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)