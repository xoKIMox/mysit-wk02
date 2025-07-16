import json
import os
from django.core.management.base import BaseCommand
from quiz.models import Question, Choice
from datetime import datetime
class Command(BaseCommand):
    help = "Load quizzes from quizzrs-1-68.json"
    
    def handle(self , *args, **kwarge ):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        json_path = os.path.join(BASE_DIR, 'C:\พื้นที่สำหรับเรียน\mysit-wk02\mysite\quizzes-1-68.json')

        with open(json_path, encoding='utf-8') as f:
            data = json.load(f)

            for item in data:
                model = item['model']
                fields = item['fields']

                if model == 'quiz.question':
                    q = Question(
                        id=item['pk'],
                        text=fields['text'],
                        published_date=datetime.fromisoformat(fields['published_date'])
                    )
                    q.save()

                elif model == 'quiz.choice':
                    c = Choice(
                        id=item['pk'],
                        question_id=fields['question'],
                        text=fields['text'],
                        correct=fields['correct']
                    )
                    c.save()

        self.stdout.write(self.style.SUCCESS(' Loaded quizzes successfully'))