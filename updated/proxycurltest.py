import requests
import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',password='root123',database='coursify')
if con.is_connected():

    rol=input("Enter the role")
    comp=input("enter the company name in which currently working")
    api_key = 'icD6s2qWEm5kNuIDuutLkA'
    headers = {'Authorization': 'Bearer ' + api_key}
    api_endpoint ='https://nubela.co/proxycurl/api/find/company/role/'
    params = {
        'role':rol,
        'company_name':comp,
    }
    response = requests.get(api_endpoint,
                            params=params,
                            headers=headers)

    good=response.json()
    profile_url=good['linkedin_profile_url']
    
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    linkedin_profile_url = profile_url
    headers = {'Authorization': 'Bearer ' + api_key}

    response = requests.get(api_endpoint,params={'url': linkedin_profile_url},headers=headers)

    good=response.json()

    name=good['full_name']
    city=good['city']
    country=good['country_full_name']
    about=good['summary']
    picture=None

    cursor=con.cursor()
    cursor.execute("insert into `basic_info` (`name`,`city`,`country`,`about`,`profile_url`) values (%s,%s,%s,%s,%s);",(name,city,country,about,profile_url,))
    con.commit()
    cursor.close()

else:
    print("not connected")