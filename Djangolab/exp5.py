import requests as rq
url="https://dog.ceo/api/breeds/image/random"
res=rq.get(url)
if res.status_code == 200:
    breed_info=res.json()
    print("The Breeds are: ",breed_info['message'])
else:
    print("Failed to fetch Breed data")