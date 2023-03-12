import json
from django.http import JsonResponse

def api_home(request,*args, **kwargs):
    #request ->HttpRequest -> Django
    #print(dir(request))
    #request.body
    body = request.body #byte string of JSON Data
    data={}
    try:
        data = json.loads(body) #String of json data ->python dictionary
    except:
        pass

    print(data)
    print(data.keys())
    # data['headers']=request.headers #request.META -> 
    print(request.headers)
    data['content_type']=request.content_type
    print(data)
    return JsonResponse({'message':'Hi there, this is your django api response!!!!'})