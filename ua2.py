device_model = "samsung"  
device_M = "MetroPCS"
application_version = "294.0.0.39.118"  
application_version_code = "591968038"  
density = "3.5"  

user_agent = f"[FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBDM/{{density={density},width=1440,height=2730}};FBLC/en_US;FBRV/{application_version_code};FBMF/{device_M};FBBD/{device_model};FBPN/com.facebook.katana;FBDV/{device_model};FBSV/7.1.1;nullFBCA/armeabi-v7a:armeabi;]"

print(user_agent)
