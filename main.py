import subprocess
import re
import os


while True:
    list_elements = subprocess.run(['netsh', 'wlan', 'show', 'profiles'])
    print(list_elements)
    target: str = input("Target: ")

    command_output = subprocess.run(['netsh', 'wlan', 'show', 'profile', target], capture_output=True).stdout.decode()

    wifi_profile = dict()

    if re.search("Security key {11}: Absent", command_output):
        pass
    else:
        wifi_profile["ssid"] = target
        info_pass = subprocess.run(["netsh", "wlan", "show", "profile", target, "key=clear"],
                                   capture_output=True).stdout.decode()
        password = re.search("Key Content {12}: (.*)", info_pass)
        if password is None:
            wifi_profile["password"] = None
        else:
            parola: str = password[1].replace("\r", "")
            wifi_profile["password"] = parola

    print(wifi_profile)
    input("ENTER pt a continua.....")
    os.system("cls")

