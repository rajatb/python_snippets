#Parse the url
#Find the has variable
#Sort it with alpha
#get only the values
#concatinate
#calculate the hash


import urlparse
import hmac
import hashlib

URL = "http://api.example.com/callback.php?customer_id=3453523454&id=70bae1905f7844a3a012a5f4173021db&hash=28f3b28b09b2578db06ee371990b5a02882523eba954d5a1b57afe2c7e7d3f10&value=20&type=Coins"

#parse the url
querystring = urlparse.urlparse(URL).query
querystring_dict = dict(urlparse.parse_qsl(querystring))
verify_value = querystring_dict.pop('hash')
keys_list = querystring_dict.keys()
keys_list.sort()
new_string = ""
for keys in keys_list:
    new_string+=querystring_dict[keys]
print new_string

digest_m = hmac.new(b'7dbcfd2a42134f47bfb72daa02f85ec9',msg=new_string,digestmod=hashlib.sha256).hexdigest()
print hmac.compare_digest(verify_value,digest_m)