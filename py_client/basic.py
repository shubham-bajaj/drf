import requests
# endpoint ="http://httpbin.org/status/200/"
# endpoint = "http://httpbin.org/anything"
endpoint  ="http://localhost:7000/api/"

get_response = requests.get(endpoint,params={'abc':123},json={'query':'hello world'}) #HTTP Request
#form data json data
# print(get_response.text)#print raw text response
# print(get_response.status_code)

#REST API -> Web API 

# Javascript Object Notation ~python dict

print(get_response.json())
# print(get_response.status_code)
