import os
import django

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# Initialize Django
django.setup()

# Now you can import and use your models
from base.models import OrderItem

QS = OrderItem.objects.all()
# print(QS[0].get_product_info())

d = {}
for i in range(len(QS)):
    d[i+1] = QS[i].get_product_info()
idx = d.keys()
print(idx)
df = pd.DataFrame(d, index=[1, 2, 3])
df = df.T
df.columns = ['category', 'brand', 'rating']
