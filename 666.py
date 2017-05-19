# import requests
# url = "https://api.vk.com/method/users.get?user_ids=pshnpdrs666"
# response = requests.get(url)
# data = response.json()
# print(data['response'][0]['uid'])
# print(data['response'][0])

# url = "https://api.vk.com/method/users.get?user_ids=pshnpdrs666&fields=last_seen,status"
# response = requests.get(url)
# data = response.json()
# print(data['response'][0]['status'])
# print(data['response'][0]['last_seen'])

# uid = data['response'][0]['uid']
# url = 'https://api.vk.com/method/wall.get?owner_id=%d' %uid
# print(url)
# response = requests.get(url)
# data = response.json()
# posts = data['response'][1]
# post_count= data['response'][0]
# #url = "https://api.vk.com/method/users.get?user_ids=pshnpdrs666"print(posts)


# url = "https://api.vk.com/method/users.getFollowers?user_id=pshnpdrs666&fields=sex,bdate"
# response = requests.get(url)
# data = response.json()
# print(data)

'''
import vk
session = vk.Session()
api = vk.API(session)
print(api.users.get(user_ids=1))


'''
import vk
session = vk.Session(access_token = '34409d426b632f59f925651a286b54f872c223a40102c16c66dd7d4a3a102540872503ad3daf29e9b15e6')
api = vk.API(session)
l = api.friends.get()
print(l)
r = api.status.set(text = 'Hi')
print(r)

'''


import requests 
token = '0bfb458ccd40fc5fbc12bd95db5b4480fbb3162242b79e8b302e3780c82bdbc7a9bdb355344ecff00e86d'
url = 'http://www.vktops.com/statusy-o-zhenshchinakh/'
r = requests.get(url)
html = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
a = soup.select('.statusesList .statusesList-item div.text')[0].text
print(a)
url = 'https://api.vk.com/method/status.set?text=%s&v=5.52&access_token=bff8ff9dbff8ff9dbfa7c761cdbfa29429bbff8bff8ff9de7303f1c0873a7c9db2cc1da' %a
r = requests.get(url)
print(r.json())


https://oauth.vk.com/blank.html#access_token=34409d426b632f59f925651a286b54f872c223a40102c16c66dd7d4a3a102540872503ad3daf29e9b15e6&expires_in=86400&user_id=162765493
https://oauth.vk.com/authorize?client_id=5925812&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=wall,friends,status&response_type=token&v=5.52
'''