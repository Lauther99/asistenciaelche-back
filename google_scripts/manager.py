import requests

base_url = "https://script.google.com/macros/s/AKfycbw9w9Bc8ZdEuTexMZORywI5Mf7n2q2QLv0luU4v9Dfdccc-96cDUHDLhuy996Q8C5nc/exec"

def register_workers(user_data):
    register_url = base_url

    headers = {"Content-Type": "application/json"}

    response = requests.post(register_url, json=user_data, headers=headers)
    response_data = response.json()
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    
    return response_data

def update_assistance(data):
    update_url = f"{base_url}?accion=actualizar_asistencias"
    
    headers = {"Content-Type": "application/json"}
    print(data)
    response = requests.post(update_url, json=data, headers=headers)
    
    response_data = response.json()
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    return response_data

def get_user_data(data):
    update_url = f"{base_url}?accion=get_user_data"
    
    headers = {"Content-Type": "application/json"}
    print(data)
    response = requests.post(update_url, json=data, headers=headers)
    
    response_data = response.json()
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    return response_data

def set_photo_embedding(data):
    update_url = f"{base_url}?accion=set_photo_embedding"
    
    headers = {"Content-Type": "application/json"}
    print(data)
    response = requests.post(update_url, json=data, headers=headers)
    
    response_data = response.json()
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    return response_data

def set_keypass(data):
    update_url = f"{base_url}?accion=set_keypass"
    
    headers = {"Content-Type": "application/json"}
    print(data)
    response = requests.post(update_url, json=data, headers=headers)
    
    response_data = response.json()
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    return response_data