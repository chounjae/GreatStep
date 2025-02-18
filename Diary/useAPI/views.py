from django.shortcuts import render
from django.shortcuts import render
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from decouple import config


openai.api_key = config('OPENAI_API_KEY')

@csrf_exempt
def summary(request) : 
    if request.method == 'POST':
        data = json.loads(request.div)
        user_content = data.get('text' , '')
        
        prompt = f"""
        
        입력 받은 문장 : \n{user_content}
        """
        
        try:
            response = openai.ChatCompletion.create(
                model = "gpt-4o",
                messages = [{"role": "system", "content": "게시물 글 요약 하는 ai"},
                            {"role": "user", "content": prompt}],
                
                max_tokens=100, #ai 응답 최대 길이
                temperature=0.5 #답변에 창의성 정도 설정 0.0이 기장 보수적
            )
            
            summary = response['choices'][0]['message']['content'].strip()
            return JsonResponse({'success':True , 'text':summary})
            
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)      

# Create your views here.
