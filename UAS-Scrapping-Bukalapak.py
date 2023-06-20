#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[3]:


import requests
import csv
 
key = input('masukkan keyword :')
write = csv.writer(open('hasil/{}.csv'.format(key), 'w', newline=''))
header = ['Nama', 'Harga', 'Stok']
write.writerow(header)
 
url = 'https://api.bukalapak.com/multistrategy-products'
apiurl = 'https://api.bukalapak.com/stores/'
count =0
for page in range(1,2):
    parameter = {
    'prambanan_override': True,
    'keywords': key,
    'limit': 50,
    'offset': 50,
    'page': page,
    'facet': True,
    'access_token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImFjY291bnRzLmp3dC5hY2Nlc3MtdG9rZW4iLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmJ1a2FsYXBhay5jb20vIiwic3ViIjoiNjEyMzM0MDk5IiwiYXVkIjpbImh0dHBzOi8vYWNjb3VudHMuYnVrYWxhcGFrLmNvbSIsImh0dHBzOi8vYXBpLmJ1a2FsYXBhay5jb20iLCJodHRwczovL2FwaS5zZXJ2ZXJtaXRyYS5jb20iXSwiZXhwIjoxNjg3MjUzMDM3LCJuYmYiOjE2ODcyMzg4MTcsImlhdCI6MTY4NzIzODgxNywianRpIjoiX0EtYUVOaEFITjJfQ3pBNDlXVnZtdyIsImNsaWVudF9pZCI6IjIzMWQ0YTg2OTA1ZjBmMjYyYzVlMDNmYyIsInNjb3BlIjoicHVibGljIHVzZXIgc3RvcmUifQ.V28kNEHmLgU2FKRk3NgzNPnrehEgWJR0761XefmQu0JXZDIu6CxHZl1WZcRfaBQZJcn5l_S8g0wnO_TRBdjz2GnTFzlx1fTSDeCBMhD-GirA1_sJJqzs8LmW-Y6BC23fonyAiy3nQdTk5ZNqkw0Ybfv4y4C2GYddsp1UQe2gJNdmQOWa99T4mSWyzlo4FB6A53LE1jF0OdEY3Jw0AEMPxNLOvMb6TFuXhPIoL9AZEpL4Gk0Jl5HdIGLvl1mt-1kvNSvQEyRT8f81C8hDlMC7iWfdJ4HpuRGmfu5rRZ358R-gB5QZnbswBmdRk6oK8wGxyDY-6gXMOizWSmO9TLQbCg'
    }
 
    r = requests.get(url, params=parameter).json()
 
    products = r['data']
    for p in products:
        nama = p['name']
        harga = p['price']
        stok = p['stock']
        count+=1
        print('No :',count, 'nama :',nama, 'harga :',harga, 'stok :', stok)
        write = csv.writer(open('hasil/{}.csv'.format(key), 'a',newline=''))
        data = [nama, harga, stok]
        write.writerow(data)


# In[13]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("hasil\laptop.csv")


plt.plot(data['Stok'])
plt.plot(data['Harga'])

plt.title("Line Chart")

plt.xlabel('stok')
plt.ylabel('harga')

plt.show()


# In[19]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("hasil\laptop.csv")

plt.bar(data['Stok'], data['Harga'])

plt.title("Bar Chart")

plt.xlabel('stok')
plt.ylabel('harga')

plt.show()


# In[ ]:




