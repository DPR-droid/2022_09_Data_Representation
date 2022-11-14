

# https://www.holisticseo.digital/python-seo/internet-archive/
# https://virustotal.github.io/vt-py/howtoinstall.html

filename = "filename.txt"

import os.path
import waybackpy
import vt


# Create Config file
def create_config_file():
    user_input = input("Press q to quit: ")
    if user_input == "q":
        print("Quitting")
        exit
    else:
        virustotal = input("Virustotal API: ")
        mxtoolbox = input("MXTOOLBOX API: ")
        htmltopdfkey = input("htmltopdfkey API: ")

        text = ('config = {"htmltopdfkey":"' + htmltopdfkey + '","mxtoolbox":"' + mxtoolbox + '","virustotal":"' + virustotal + '"}')
        print(text)
        with open('tester.py', 'w') as f:
            f.write(text)
        


if os.path.isfile(filename):
    print ("File exist")
else:
    print ("File not exist\nPlease have API keys ready")
    create_config_file()


from config import config as cfg

print(cfg)
