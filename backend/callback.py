import requests
def callback(data):
    url = f"http://localhost:3000/api/v1/scrape/callback"
    response = requests.post(url, data=data)
     
    if response.status_code == 200:
        return print("Callback called")
   
    return print("Callback failed")