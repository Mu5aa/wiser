import requests

def get_api_info(base_url):
    url = f"http://{base_url}/api/info"
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  
    else:
        return f"Error: {response.status_code} - {response.text}"  
    

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
    
def post_account_claim(base_url, user):
    url = f"http://{base_url}/api/account/claim"
    headers = {
        "Content-Type": "application/json",
    }
    data = {"user": user}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()  
    else:
        return f"Error:{response.text}"  
    
def post_network_wlan(base_url, auth_token, ssid, sec, password):
    url = f"http://{base_url}/api/net/wlans"
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }
    data = {
        "ssid": ssid,
        "sec": sec,
        "password": password
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()  
    else:
        return f"Error: {response.text}"  
    

def post_room_creation(base_url, auth_token, room_name, kind):
    url = f"http://{base_url}/api/rooms"
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }
    data = {
        "name": room_name,
        "kind": kind
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()  
    else:
        return f"Error:{response.text}"  
    
def patch_load_update(base_url, auth_token, load_id, name, room):
    url = f"http://{base_url}/api/loads/{load_id}"
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
    }
    data = {
        "name": name,
        "room": room
    }
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()  
    else:
        return f"Error:{response.text}"  
    

def put_target_state_update(base_url, auth_token, load_id, target_state):
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
