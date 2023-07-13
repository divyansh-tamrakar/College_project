from .models import ArtisanUser
import csv
from django.db import transaction


# @transaction.atomic
# def import_():
#     with open(r'C:\Users\divya\OneDrive\Desktop\new_data.csv') as csvfile:
#             reader = csv.DictReader(csvfile)
#             for row in reader:
#                 artisan = ArtisanUser()
#                 artisan.Pahchan_card = row['Pahchan_card']
#                 artisan.Mobile_number = row['Mobile_number']
#                 artisan.Gender = row['Gender']
#                 artisan.Address_of_the_Artisan = row['Address_of_the_Artisan'] 
#                 # Set other fields as needed
                
#                 artisan.save()
                
# import_()