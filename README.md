# WHAT IS MY IP 

![web pic](.github/pic2(v3.1.0).png)

This lightweight and fast script allows you to effortlessly display your public IP address and key network details, such as location and ISP. A practical tool for checking your internet connection status and related information! 🚀




### Features
- Display your public IP address.
- Get geolocation details (country, city, etc.).
- Fast and lightweight.
- Easy to integrate with other tools.
- Option for verbose output with additional info.



## Installation (client)

To install the required dependencies, run the following commands on client:

```bash
pip install pyinstaller
pip install colorama
pip install requests
```


## Installation (server)

To install the required dependencies, run the following commands on server:

```bash
pip install flask
```



## Usage (server)
```bash
python app.py
```



## Usage (client)

To use the script, run the following command:

```bash
python client/whatismyip.py
```



### Command-Line Options
- `--set_url "http://localhost:6263"`: Allows you to specify a custom URL for the server.
- `-v`: Verbose mode, shows more detailed information.
- `-i "IP_ADDRESS"`: Fetch detailed info for any specific IP address.





### Example output 01 
```
 █   █ █ █▄ ▄█ █ █▀▄
 ▀▄▀▄▀ █ █ ▀ █ █ █▀ 

IP : 123.123.123.123
Country : Country
City : City
ISP : Internet service provider
```

### Example output 02
```
 █   █ █ █▄ ▄█ █ █▀▄
 ▀▄▀▄▀ █ █ ▀ █ █ █▀ 

status : success
country : country
countryCode : countryCode
region : region
regionName : regionName
city : city
zip : zip
lat : lat
lon : lon
timezone : timezone
isp : isp
org : org
as : as
query : 123.123.123.123
```

