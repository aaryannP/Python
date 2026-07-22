import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_DB_Framework.settings')
django.setup()

from foodiespot.models import Cuisine, Restaurant

# Clear existing objects if any
Restaurant.objects.all().delete()
Cuisine.objects.all().delete()

# Add Cuisines
c1 = Cuisine.objects.create(name='Italian', description='Authentic Italian cuisine')
c2 = Cuisine.objects.create(name='Mexican', description='Spicy and flavorful Mexican dishes')

# Add Restaurants
Restaurant.objects.create(name='Pasta Paradise', location='Downtown', rating=4.5, cuisine=c1)
Restaurant.objects.create(name='Pizza Corner', location='Uptown', rating=3.8, cuisine=c1)
Restaurant.objects.create(name='Taco Fiesta', location='City Center', rating=4.2, cuisine=c2)

# Query: Get all restaurants with a rating above 4.0 and print their names
top_restaurants = Restaurant.objects.filter(rating__gt=4.0)

print("Restaurants with rating > 4.0:")
for r in top_restaurants:
    print(f"- {r.name} (Rating: {r.rating})")
