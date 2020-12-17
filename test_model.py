import requests

if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/predict'
    data = [{'A': 3.0, 'B': 5.0}, {'A': 1.0, 'B': 1.0}]
    r = requests.post(url, json=data)
    print(r.json())
