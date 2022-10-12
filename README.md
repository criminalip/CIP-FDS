# CIP-FDS
Criminal IP FDS 

Analyzing FDS Data through Criminal IP

- [Description](#description)
- [Getting started](#getting-started)

## Description
This file is a sample code that is meant to analyze data from an FDS perspective, which can also be viewed by being inputted into the Splunk App. This service is available to Criminal IP Global service members. 
Process returning value with ‘/ip/data/’ from [Criminal IP API](https://www.criminalip.io/ko/developer/api/get-ip-data) and generate a log file in json format. 


Partial result value of API
```
$ curl --location --request GET "https://api.criminalip.io/v1/ip/data?ip=1.1.1.1&full=true" --header "x-api-key: <YOUR_API_KEY>"
{16 items
"ip":string"1.1.1.1"
"tags":{9 items
"is_vpn":boolfalse
"is_cloud":boolfalse
"is_tor":boolfalse
"is_proxy":boolfalse
"is_hosting":booltrue
"is_mobile":boolfalse
"is_darkweb":boolfalse
"is_scanner":boolfalse
"is_snort":booltrue
}
"score":{2 items
"inbound":int5
"outbound":int3
}
...

```

Generated Log File
```
{"datetime": "2022-09-28 13:46:34", "ip_score": "Moderate", "IP": "223.38.40.211", "country": "Korea", "as_name": "SK Telecom", "mobile": true, "tag_category": "mobile, vpn", "ip_category": "ddos (Medium), tor"}
```

## Getting started 

### Install
```
$ git clone https://github.com/criminalip/CIP-FDS.git
```

### Usage
Please follow these 3 steps before using this service.

1. Create an API-KEY by signing up for [Criminal IP](https://www.criminalip.io/ko) The API-KEY created must be inputted into `Criminal/core/api/crminalip.py`

2. Input where the log file must be saved in the `file_location` variable of `Criminal/main.py`

3. Install required libraries `requirement.txt`

```
$ pip install -r requirement.txt
```

The example below shows the results of searching 1.1.1.1. You can find various information about this IP address, such as its scoring, country information, as_name etc. 
```
$ python3 main.py 1.1.1.1

{'datetime': '2022-10-05 17:43:25', 'ip_score': 'Safe', 'IP': '1.1.1.1', 'country': 'Australia', 'as_name': 'CLOUDFLARENET', 'cloud': True, 'hosting': True, 'tag_category': 'cloud,hosting', 'ip_category': 'ddos (Medium),MISP,attack (Low)'}
```
