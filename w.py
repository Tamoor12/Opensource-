import random

def generate_user_agent():
    android_versions = ["4.4.2", "5.0", "5.1", "6.0", "7.0", "8.0", "9.0", "10.0", "11.0", "12.0"]
    os_version = random.choice(android_versions)

    device_models = [
        "SM-G3518", "SM-G920F", "SM-G930F", "SM-G950F", "SM-G960F", "SM-G970F", "SM-G975F", "SM-N950F", "SM-N960F",
        "Nokia-1", "Nokia-2", "Nokia-3", "Pixel-3", "Pixel-4",
        "Tecno-Camon12", "Tecno-Spark5", "Tecno-Phantom9",
        "Infinix-Hot9", "Infinix-Smart4", "Infinix-Note7",
        "Realme-X2", "Realme-6", "Realme-C11",
        "Redmi-Note9", "Redmi-9", "Redmi-Note8",
        "HTC-OneM9", "HTC-U11", "HTC-Desire12",
        "Vive-Pro", "Vive-Cosmos", "Vive-Focus",
        "Lenovo-K6", "Lenovo-Z6", "Lenovo-A7000",
        "Moto-G7", "Moto-E6", "Moto-Z4"
    ]
    device_model = random.choice(device_models)

    fb_app_version = f"{random.randint(1, 999)}.{random.randint(0, 9)}.{random.randint(0, 9)}.{random.randint(0, 9)}"

    user_agent = (
        f"Dalvik/1.6.0 (Linux; U; Android {os_version}; {device_model} Build/JLS36C) "
        f"[FBAN/FB4A;FBAV/{fb_app_version};FBPN/com.facebook.katana;FBLC/en_US;FBBV/{random.randint(111111111, 999999999)};FBCR/T-Mobile;FBMF/{device_model};FBBD/{device_model};FBDV/{device_model};FBSV/{os_version};FBCA/{random.choice(['x86', 'armeabi-v7a'])};"
        f"FBDM/{{density=1.5,width=720,height=1244}};FB_FW/1;FBRV/{random.randint(190000000, 199999999)};]"
    )
    return user_agent
auto_generated_user_agent = generate_user_agent()
print(auto_generated_user_agent)
