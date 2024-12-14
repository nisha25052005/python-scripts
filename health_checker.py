import requests

def check_application_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The application at {url} is UP.")
        else:
            print(f"The application at {url} is DOWN. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Could not connect to {url}. The application might be DOWN. Error: {e}")

# Replace with your application URL
app_url = "https://www.google.com"
check_application_health(app_url)
