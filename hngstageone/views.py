from django.http import JsonResponse
from django.views import View

class MyApi(View):
    def get(self, request):
        visitor_name = request.GET.get('visitor_name', 'Guest')
        client_ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
        
        # Getting location and temperature
        location = "New York"
        temperature = 11

        api_data = {
            "client_ip": client_ip,
            "location": location,
            "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"
        }
        return JsonResponse(api_data)
