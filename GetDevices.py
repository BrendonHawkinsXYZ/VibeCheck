import requests

# Replace 'your_api_key_here' with your actual Govee API key
api_key = 'your_api_key_here'
headers = {
    'Govee-API-Key': "Yours Here",
    'Content-Type': 'application/json'
}

def discover_devices():
    url = "https://openapi.api.govee.com/router/api/v1/user/devices"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to fetch devices', 'status_code': response.status_code}

# Discover devices and print their details
devices_info = discover_devices()
print(devices_info)
