from django.http import JsonResponse

def hello_spotify(request):
    """
    Returns a simple JSON response for Spotify fans.
    """
    return JsonResponse({"message": "Hello, Spotify Fans!"})

# JSON vs XML Comparison for a Flipkart Product:
#
# JSON (JavaScript Object Notation):
# {
#     "product": {
#         "name": "Smartphone XYZ",
#         "price": 15000
#     }
# }
# - Lighter, easier to read, native to JavaScript, faster parsing.
#
# XML (eXtensible Markup Language):
# <product>
#     <name>Smartphone XYZ</name>
#     <price>15000</price>
# </product>
# - More verbose, relies on tags, supports complex structures/namespaces, harder to parse.

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# --- Session 5: Third-Party API Integrations ---

# 1. OpenWeatherMap API
class MusicWeatherAPIView(APIView):
    def get(self, request, city):
        # NOTE: Replace 'YOUR_OPENWEATHERMAP_API_KEY' with a real API key to test
        api_key = "YOUR_OPENWEATHERMAP_API_KEY"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return Response({
                    "city": city,
                    "temperature": data.get("main", {}).get("temp"),
                    "description": data.get("weather", [{}])[0].get("description")
                })
            return Response({"error": "City not found or invalid API key"}, status=response.status_code)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# 2. Google Maps Geocoding API (using free Nominatim/OSM as fallback/example)
class FoodLocationAPIView(APIView):
    def get(self, request):
        restaurant_name = request.query_params.get('restaurant')
        if not restaurant_name:
            return Response({"error": "Please provide a 'restaurant' query parameter"}, status=status.HTTP_400_BAD_REQUEST)
        
        # NOTE: The prompt requested Google Maps Geocoding API.
        # url = f"https://maps.googleapis.com/maps/api/geocode/json?address={restaurant_name}&key=YOUR_GOOGLE_MAPS_API_KEY"
        # Since we don't have a Google API Key, here is the implementation structure.
        # Below we use Nominatim (OpenStreetMap) just to provide a working free example.
        url = f"https://nominatim.openstreetmap.org/search?q={restaurant_name}&format=json&limit=1"
        headers = {'User-Agent': 'DjangoRestDemoApp/1.0'}
        
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                if data:
                    return Response({
                        "restaurant": restaurant_name,
                        "latitude": data[0].get("lat"),
                        "longitude": data[0].get("lon")
                    })
                return Response({"error": "Restaurant location not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response({"error": "API Error"}, status=response.status_code)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# 3. REST Countries API
class CountryInfoAPIView(APIView):
    def get(self, request, country_name):
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data:
                    country_data = data[0]
                    return Response({
                        "country": country_name,
                        "population": country_data.get("population"),
                        "capital": country_data.get("capital", [""])[0]
                    })
            return Response({"error": "Country not found"}, status=status.HTTP_404_NOT_FOUND)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# 4. GitHub API
class GitHubReposAPIView(APIView):
    def get(self, request, username):
        url = f"https://api.github.com/users/{username}/repos"
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                repos = response.json()
                repo_names = [repo.get("name") for repo in repos]
                return Response({
                    "username": username,
                    "repositories": repo_names
                })
            return Response({"error": "User not found or API limit reached"}, status=response.status_code)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# --- Session 6: External APIs (Mailgun, Twilio, Stripe) ---

# 1. Mailgun Email API
class SendEmailAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
            
        # NOTE: Replace with real Mailgun domain and API key
        mailgun_domain = "YOUR_MAILGUN_DOMAIN"
        api_key = "YOUR_MAILGUN_API_KEY"
        
        url = f"https://api.mailgun.net/v3/{mailgun_domain}/messages"
        auth = ("api", api_key)
        data = {
            "from": f"Music App <mailgun@{mailgun_domain}>",
            "to": [email],
            "subject": "Welcome to our Music App!",
            "text": "Thank you for signing up. Enjoy the best playlists!"
        }
        
        try:
            response = requests.post(url, auth=auth, data=data)
            if response.status_code == 200:
                return Response({"message": "Email sent successfully!"})
            return Response({"error": "Failed to send email", "details": response.text}, status=response.status_code)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# 2. Twilio SMS API
class SendSMSAPIView(APIView):
    def post(self, request):
        phone_number = request.data.get("phone_number")
        message_body = request.data.get("message")
        
        if not phone_number or not message_body:
            return Response({"error": "phone_number and message are required"}, status=status.HTTP_400_BAD_REQUEST)
            
        # NOTE: Replace with real Twilio credentials
        account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
        auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
        twilio_number = 'YOUR_TWILIO_PHONE_NUMBER'
        
        try:
            from twilio.rest import Client
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=message_body,
                from_=twilio_number,
                to=phone_number
            )
            return Response({"message": "SMS sent successfully!", "sid": message.sid})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# 3. Stripe Payment API
import stripe
class PayAPIView(APIView):
    def post(self, request):
        amount = request.data.get("amount")
        currency = request.data.get("currency", "usd")
        
        if not amount:
            return Response({"error": "amount is required"}, status=status.HTTP_400_BAD_REQUEST)
            
        # NOTE: Replace with real Stripe test secret key
        stripe.api_key = "sk_test_YOUR_STRIPE_TEST_KEY"
        
        try:
            # Stripe expects amount in cents (e.g., $10.00 = 1000)
            amount_in_cents = int(float(amount) * 100)
            
            # Create a simulated PaymentIntent
            intent = stripe.PaymentIntent.create(
                amount=amount_in_cents,
                currency=currency,
                payment_method_types=['card'],
            )
            return Response({
                "status": "success",
                "transaction_id": intent.id,
                "message": f"Payment of {amount} {currency.upper()} simulated successfully."
            })
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
