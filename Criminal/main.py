import multiprocessing
from core.api.criminalip import getipdata
import pycountry
import json
from datetime import datetime 
import sys


file_location = 'input your file location'

def make_log(request_ip,request_time):
    ip_result = {}
    tag_list = []
    vpn_list = []
    ip_category_list = []
    ids_list = []
    try:
        result = getipdata(request_ip)
        score_int = result['score']['inbound']
        score_mapping = {1:'Safe',2:'Low',3:'Moderate',4:'Dangerous',5:'Critical'}
        
        score = score_mapping[score_int]
        if result['whois']['count'] != 0:
            country_code = result['whois']['data'][0]['org_country_code']
            as_name = result["whois"]['data'][0]['as_name']
            country = pycountry.countries.get(alpha_2=country_code).name.split(',')[0]
        else:
            as_name = ""
            country = ""
              
        ip_result['datetime'] = request_time
        ip_result['ip_score'] = score
        ip_result['IP'] = result['ip']
        ip_result['country'] = country
        ip_result['as_name'] = as_name
        tags = result['tags']
        
        for key, value in tags.items():
            if value == True:
                key = key.split('_')[1]
                ip_result[key]=value
                tag_list.append(key)
        
        ip_result['tag_category'] = ','.join(tag_list)
            
        if result['vpn']['count'] != 0:
            for i in range(len(result['vpn']['data'])):
                vpn_name = result['vpn']['data'][i]['vpn_name']
                vpn_list.append(vpn_name)
            vpn_list = list(set(vpn_list))
            ip_result['vpn_name'] = ','.join(vpn_list)

        if result['ip_category']['count'] != 0:
            for i in range(len(result['ip_category']['data'])):
                ip_type = result['ip_category']['data'][i]['type']
                ip_category_list.append(ip_type)
            ip_category_list = list(set(ip_category_list))
            ip_result['ip_category'] = ','.join(ip_category_list)
    
        if result['ids']['count'] != 0:
            for i in range(len(result['ids']['data'])):
                calssfication = result['ids']['data'][i]['classification']
                ids_list.append(calssfication)
            ids_list = list(set(ids_list))
            ip_result['ip_classification'] = ','.join(ids_list)
        
        return ip_result
    except Exception as e:
        print('api error')
        print(e)

        
   
def make_file(ip_address):
    try :
        request_ip = ip_address
        request_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ip_result = make_log(request_ip,request_time)
        print(ip_result)
        with open(file_location,'a+') as f:
            f.write(json.dumps(ip_result) + '\n')
                    
    except Exception as e:
        print('make file error')
        print(e)
    
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Target IP Address Required!\nTry Again.")
    else:
        ip = sys.argv[1]
        make_file(ip)