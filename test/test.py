import requests

token = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODI1MDE0MTcsImlhdCI6MTY1MDk2NTQxNywicmF5IjoiOGM0Y2Q4MTMyMGI3ZTNjOTc4MzM1YWE1MGNlMDc0ZTQiLCJzdWIiOjEwNTQxODl9.GDbD0leE6_W12khX1nZWpDtDvwtS_-dcXjv2-gIJk6EvRUjkT2Ji8we-m_tmp6_nhSvNP3wYgp982EJzKUhMPBYAlm5BiLjXS7QlNfo7GbFdbLDslysoGPFmceD8pbcRdq7ClvP91JvKEySemM0YnXQIpPDV3P9rISn2esF-ottTv4yaJDCaf7rarzGqG3e1yio_KoWheJfY_OIMOrQ9aLnDRUtrPkubimPcMvc6CdbTz1vcGz6LzQHnFtJvGDmdfmSdSMYCqNSRF-80HRTjznFvqE0YeBoPfzEVmebdU4JDtS_eop0L6pX6HWnyxHOnVJrx2ZSrwhikFHmqDELAiQ'
country = 'russia'
operator = 'any'
product = 'twitter'

headers = {
    'Authorization': 'Bearer ' + token,
    'Accept': 'application/json',
}

response = requests.get('https://5sim.net/v1/user/buy/activation/' + country + '/' + operator + '/' + product, headers=headers)
print(response.text)