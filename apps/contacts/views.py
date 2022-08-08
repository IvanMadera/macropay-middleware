from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from operator import itemgetter
import json

# Create your views here.
@csrf_exempt
def contacts(request):
    if request.method == "GET":
        with open('./apps/contacts/fakedatabase.js', 'r') as file:
            data = json.load(file)
        data = sorted(data, key=itemgetter('name'))
        return JsonResponse(data, status=200, safe=False)
    else:
        return JsonResponse({"message":"Method not allowed"}, status=405)

@csrf_exempt
def contact_detail(request, pk):
    if request.method == "GET":
        with open('./apps/contacts/fakedatabase.js', 'r') as file:
            data = json.load(file)
        for i in data:
            if i['id'] == pk:
                return JsonResponse(i, status=200, safe=False)
        return JsonResponse({"message":"contact does not exist"}, status=404, safe=False)
    else:
        return JsonResponse({"message":"Method not allowed"}, status=405)


@csrf_exempt
def contact(request):
    if request.method == "POST":
        data = json.loads(request.body)
        with open('./apps/contacts/fakedatabase.js', 'r') as file:
            new_data = json.load(file)
            new_data.append(data)
        with open('./apps/contacts/fakedatabase.js','w') as file:
            json.dump(new_data,file)
        return JsonResponse(data, status=201)
    else:
        return JsonResponse({"message":"Method not allowed"}, status=405)

def error(request, exception):
    return JsonResponse({"message":"Error 404 Not found"}, status=404)