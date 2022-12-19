

# https://www.holisticseo.digital/python-seo/internet-archive/
# https://virustotal.github.io/vt-py/howtoinstall.html

filename = "filename.txt"

import os.path
import waybackpy # imported the waybackpy.
import vt # imported the virustotal.


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

# https://www.holisticseo.digital/python-seo/internet-archive/
# To save a URL to Wayback Machine with Internet Archive, a URL should have features below.

#     The URL should respond with a 200 HTTP Status Code (OK).
#     The URL Should have actual content on it.
#     The URL should have importance to be archived.


url = "https://www.holisticseo.digital" #determined the URL to be saved.
user_agent = "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Mobile Safari/537.36" #determined the user-agent.


wayback = waybackpy.Url(url, user_agent) # created the waybackpy instance.
archive = wayback.save() # saved the link to the internet archive
print(archive.archive_url) #printed the URL.