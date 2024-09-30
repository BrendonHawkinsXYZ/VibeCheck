import requests
import uuid

# Configuration and API Keys
govee_api_key = 'Yours Here'
govee_url = "https://openapi.api.govee.com/router/api/v1/device/control"
govee_headers = {
    'Content-Type': 'application/json',
    'Govee-API-Key': govee_api_key
}

# Function to toggle gradient setting
def toggle_gradient(sku, device, state):
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
    
    response = requests.post(govee_url, json=payload, headers=govee_headers)
    
    if response.status_code == 200:
        state_str = "on" if state == 1 else "off"
        print(f"Gradient toggle set to {state_str}.")
    else:
        print(f"Failed to set gradient toggle: {response.json()}")

# Main execution
if __name__ == "__main__":
    sku = "H607C"
    device = "4D:45:E7:B3:E2:81:D4:CF"
    toggle_gradient(sku, device, 1)  # Turn on gradient
