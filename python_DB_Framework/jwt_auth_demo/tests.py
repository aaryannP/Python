from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class JWTAuthenticationTests(APITestCase):

    def setUp(self):
        self.url = reverse('secure_api')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Generate token manually for the test
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

    def test_unauthorized_access(self):
        """
        Test that accessing the secure endpoint without a token returns 401.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authorized_access(self):
        """
        Test that accessing the secure endpoint with a valid token returns 200.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "You are fully authenticated via JWT.")
