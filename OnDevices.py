import requests
import uuid

# Replace 'your_api_key_here' with your actual Govee API key
api_key = 'Yours Here'
url = "https://openapi.api.govee.com/router/api/v1/device/control"

headers = {
    'Content-Type': 'application/json',
    'Govee-API-Key': api_key
}

def toggle_gradient(sku, device, state):
    """Function to toggle the gradient setting of a Govee light."""
    request_id = str(uuid.uuid4())
    
    payload = {
        "requestId": request_id,
        "payload": {
            "sku": sku,
            "device": device,
            "capability": {
                "type": "devices.capabilities.toggle",
                "instance": "gradientToggle",
                "value": state
            }
        }
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        state_str = "on" if state == 1 else "off"
        print(f"Gradient toggle set to {state_str}.")
    else:
        print(f"Failed to set gradient toggle: {response.json()}")

def turn_on_light(sku, device):
    """Function to turn on a Govee light."""
    # Generate a unique request ID
    request_id = str(uuid.uuid4())
    
    # Construct the payload for turning the light on
    payload = {
        "requestId": request_id,
        "payload": {
            "sku": sku,
            "device": device,
            "capability": {
                "type": "devices.capabilities.on_off",
                "instance": "powerSwitch",
                "value": 1
            }
        }
    }
    
    # Send the POST request to the Govee API
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print("Light turned on successfully.")
        turn_light_white(sku, device)  # Call the function to turn the lights white
    else:
        print(f"Failed to turn on light: {response.json()}")

def turn_light_white(sku, device):
    """Function to change the light color to white."""
    # Generate a unique request ID
    request_id = str(uuid.uuid4())
    
    # Convert RGB to a single integer
    r, g, b = 255, 255, 255
    rgb_value = ((r & 0xFF) << 16) | ((g & 0xFF) << 8) | (b & 0xFF)
    
    # Construct the payload for changing the light color to white
    payload = {
        "requestId": request_id,
        "payload": {
            "sku": sku,
            "device": device,
            "capability": {
                "type": "devices.capabilities.color_setting",
                "instance": "colorRgb",
                "value": rgb_value
            }
        }
    }
    
    # Send the POST request to the Govee API
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print("Light color changed to white successfully.")
    else:
        print(f"Failed to change light color: {response.json()}")

# Main execution
if __name__ == "__main__":
    sku = "H607C"
    device = "4D:45:E7:B3:E2:81:D4:CF"
    
    # Turn off the gradient before turning the light white
    toggle_gradient(sku, device, 0)
    
    # Turn on the light
    turn_on_light(sku, device)
    
    # Turn the light white (this is already called within turn_on_light)
    # turn_light_white(sku, device)
