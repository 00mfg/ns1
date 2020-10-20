import requests
import re


def getauth_token():
    url = "http://192.168.26.10/nitro/v1/config/login"
    payload = {"login": {"username": "nsroot", "password": "nsroot"}}
    header = {"Content-Type": "application/vnd.com.citrix.netscaler.login+json"}
    response = requests.post(url, json=payload, headers=header)
    cookie = response.headers.get("Set-Cookie")
    token = re.findall('NITRO_AUTH_TOKEN=.*?;', cookie)[0]
    return token


def get_vip_list():
    url = "http://192.168.26.10/nitro/v1/config/lbvserver"
    header = {"Content-Type" : "application/json", 'Cookie': getauth_token()}
    response = requests.get(url, headers=header).json()
    vip_list = [i['ipv46'] for i in response['lbvserver']]
    return vip_list


def table1_data():
    url = "http://192.168.26.10/nitro/v1/config/nsconnectiontable"
    header = {"Content-Type" : "application/json", 'Cookie': getauth_token()}
    response = requests.get(url, headers=header).json()
    src_list = []
    conn_list = []
    for i in get_vip_list():
        for x in response['nsconnectiontable']:
            if i == x['destip']:
                src_list.append(x['sourceip'])
                conn_list.append([x['destip'], len(set(src_list)), list(set(src_list))])
    return conn_list


def table2_data():
    url = "http://192.168.26.10/nitro/v1/config/nsconnectiontable?args=link:true"
    header = {"Content-Type" : "application/json", 'Cookie': getauth_token()}
    response = requests.get(url, headers=header).json()
    print(response['nsconnectiontable'])



if __name__ == '__main__':
    table2_data()