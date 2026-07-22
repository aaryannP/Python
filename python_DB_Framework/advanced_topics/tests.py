from django.test import TestCase
from django.urls import reverse

class AdvancedTopicsTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('advanced_home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
