# import subprocess
# import re


# command_output = subprocess.run(["netsh", "wlan", "show", "profile"],capture_output=True).stdout.decode()

# profile_names = (re.findall("All User Profile     : (.*)\r",command_output))

# wifi_list = list()

# if len(profile_names) !=0:
#     for name in profile_names:
#         wifi_profile = dict()
#         profile_info = subprocess.run(["netsh", "wlan", "show", "profile",name],capture_output=True).stdout.decode()

#         if re.search("Security key     : Absent",profile_info):
#             continue
#         else:
#             wifi_profile['ssid'] = name
#             profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name ,"key=clear"])
            
#             password = re.search("Key Content     : (.*)\r",profile_info_pass)

#             if password == None:
#                 wifi_profile['password']=None

#             else:
#                 wifi_list.append(wifi_profile)
# for x in range(len(wifi_list)):
#     print(wifi_list[x])
        

import subprocess

a = subprocess.check_output(['netsh','wlan','show','profile']).decode('utf-8').split('\n')
a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]

for i in a:
    results = subprocess.check_output(
      ['netsh','wlan','show','profile']).decode('utf-8').split('\n')  
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    print(results)

    try:
        print("{:<30}| {:<}".format(i,results[0]))
    except IndexError:
        print("{:<30}| {:<}".format(i, ""))