#DALVIK UA_GENERATE_CODE

import platform
import random

def generate_custom_user_agent():
    android_versions = ["Android 9", "Android 10", "Android 11", "Android 12"]
    selected_android_version = random.choice(android_versions)

    manufacturers = [
        "TECNO", "Samsung", "Xiaomi", "Vivo",
       
    ]
    selected_manufacturer = random.choice(manufacturers)

    android_models = {
        "TECNO": ["KE5", "Model2", "Model3"],
        "Samsung": ["Galaxy S21", "Galaxy Note 20", "Galaxy A52"],
        "Xiaomi": ["Redmi Note 10", "POCO X3"],
        "Vivo":["vivo 1906" , "vivo 1806", "vivo 1808","V2214", "V2021"],
        }

    selected_model = random.choice(android_models.get(selected_manufacturer, []))

    device_names = {
        "TECNO": "TecnoDevice",
        "Samsung": "SamsungDevice",
        "Xiaomi": "XiaomiDevice",
        "Vivo": "VivoDevice",
       
    }

    device_name = device_names.get(selected_manufacturer, "DefaultDevice")

    build_number = random.randint(1000, 9999)

    app_packages = ["com.facebook.katana", "com.facebook.ocra", "com.facebook.mlite","com.facebook.lite","com.facebook.adsmanager"]
    selected_app_package = random.choice(app_packages)

    density_version = round(random.uniform(1.0, 3.0), 1)
    height_version = random.randint(500, 2000)
    width_version = random.randint(300, 1500)

    user_agent = (
        f"Dalvik/2.1.0 (Linux; U; {selected_android_version} Build/{build_number}; {selected_manufacturer} {selected_model})"
        f" [FBAN/{random.randint(100, 999)}.{random.randint(1, 9)}.{random.randint(0, 9)}.0;FBBV/{random.randint(100000000, 999999999)};FBRV/{random.randint(0, 9)};"
        f"{selected_app_package};FBLC/en_US;FBMF/{selected_manufacturer};FBBD/{selected_manufacturer};FBDV/{selected_model};"
        f"FBSV/{random.randint(8, 12)};FBCA/armeabi-v7a:armeabi;FBDM/{{density={density_version},width={width_version},height={height_version}}};FB_FW/{random.randint(1, 3)};]"
    )

    return user_agent

# Example usage
custom_user_agent = generate_custom_user_agent()
print(custom_user_agent)