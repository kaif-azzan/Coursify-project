import requests
import csv
import json
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
linkedin_profile_url = 'https://www.linkedin.com/in/monson-verghese/'
api_key = '0ckfUqFtlYDhx9mqFBZSTg'
headers = {'Authorization': 'Bearer ' + api_key}

response = requests.get(api_endpoint,
                        params={'url': linkedin_profile_url},
                        headers=headers)

profile_data=response.json()
#name=profile_data['full_name']
#city=profile_data['city']
#country=profile_data['country']
#education=profile_data['education']

#data_list=[]
#
#data_list.append(name)
#data_list.append(city)
#data_list.append(country)

new_list=[]
summary=profile_data['summary']
new_list.append(summary)

f=open('sum.csv','w')
k=csv.writer(f)
k.writerow(new_list)
f.close

#f=open('test.csv','w')
#d=csv.writer(f)
#d.writerow(data_list)
#f.close