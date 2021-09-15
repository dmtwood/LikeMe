import requests

r =requests.get('https://variety.com/wp-content/uploads/2019/06/shutterstock_3688612b-cropped-1-e1561552698740.jpg')

if r.status_code == 200:
    with open("python.jpg", "wb") as f:
        f.write(r.content)
        f.close()