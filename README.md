# CIP-FDS
Criminal IP FDS 

FDS Analaysis by Criminal IP /  Criminal IP를 통해 FDS 데이터 분석 

- [Description](#description)
- [Getting started](#getting-started)

## Description
해당 파일은 Criminal IP Global service를 사용하는 고객들 중 FDS 관점에서 데이터를 분석하기 위해 작성된 sample code 이며, 이 데이터를 Splunk App 에 넣어서 보는 것도 가능합니다.
[Criminal IP API](https://www.criminalip.io/ko/developer/api/get-ip-data) 중 '/ip/data/'를 사용하여 리턴되는 값을 가공하여 json format의 log file을 생성하게 합니다.


API 결과값 일부분 
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

가공된 Log file
```
{"datetime": "2022-09-28 13:46:34", "ip_score": "Moderate", "IP": "223.38.40.211", "country": "Korea", "as_name": "SK Telecom", "mobile": true, "tag_category": "mobile, vpn", "ip_category": "ddos (Medium), tor"}
```

## Getting started 

### Install
```
$ git clone https://github.com/criminalip/CIP-FDS.git
```

### Usage
사용 하기에 앞서 3가지 작업이 필요합니다.

1. [Criminal IP](https://www.criminalip.io/ko)에 가입을 해서 API-KEY를 생성해야 합니다. 생성하신 API-KEY는 `Criminal/core/api/crminalip.py`에 입력해 주셔야합니다.

2. `Criminal/main.py`의 `file_location` 변수에 log file을 저장하고자 하는 위치를 넣어주셔야 합니다.

3. 필요 Library들을 설치합니다. (requirement.txt)

```
$ pip install -r requirement.txt
```

아래 예제는 1.1.1.1을 검색을 한 결과 입니다. IP의 스코어링, 국가 정보, as_name 등 여러 정보들을 확인할 수 있습니다. 
```
$ python3 main.py 1.1.1.1

{'datetime': '2022-10-05 17:43:25', 'ip_score': 'Safe', 'IP': '1.1.1.1', 'country': 'Australia', 'as_name': 'CLOUDFLARENET', 'cloud': True, 'hosting': True, 'tag_category': 'cloud,hosting', 'ip_category': 'ddos (Medium),MISP,attack (Low)'}
```
