from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def get_question(request):
    data = {
        "id": 1,
        "text": "ประเทศไทยมีกี่จังหวัด",
        "choices": [50, 68, 72, 77]
    }
    return JsonResponse(data)

@csrf_exempt
def create_question(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            return JsonResponse(data, status=201)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)
