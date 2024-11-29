import requests



def set_load_state(base_url, auth_token, load_id, target_state):
    url = f"http://{base_url}/api/loads/{load_id}/target_state"
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }
    print(headers)
    response = requests.put(url, headers=headers, data = f"{target_state}")
    if response.status_code == 200:
        responseStatus = response.json()['status']
        if responseStatus   == 'success':
            return "StateSet"
        else:
            return "StateNotSet"
    else:
        return 'UnexpectedResponse',print(f"{response.text}")