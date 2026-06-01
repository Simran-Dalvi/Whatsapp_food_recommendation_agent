import json
from .openai_service import chat_bot
from .prompts import EXTRACTION_PROMPT

REQUIRED_FIELDS = [
        "diet",
        "budget",
        "category"
    ]

QUESTIONS = {
    "category" : "What type of cusine would you like ?",
    "budget" : "What's your budget ?",
    "diet" : "veg or Non-veg?"
}

class FoodAgent:

    def extract_preferences(self, user_message):

        messages = [
            {
                "role" : "system",
                "content" : EXTRACTION_PROMPT
            },
            {
                "role" : "user",
                "content" : user_message
            }
        ]

        response = chat_bot(messages)

        try:
            return json.loads(response)
        
        except:
            return {}
        
    def get_missing_field(self, prefrences):
        for field in REQUIRED_FIELDS:
            if not prefrences.get(field):
                return field
        
        return None
    
    def get_question_for_missing_field(self, field):

        return QUESTIONS.get(
            field,
            "Could you tell me a little more?"
        )
        
    

