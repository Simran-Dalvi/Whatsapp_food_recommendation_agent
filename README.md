# Whatsapp_food_recommendation_agent

This is food recomendation chat bot.
## Phase 1:
* Build the food recommendation engine.

Goal

Create an independent AI-powered food recommendation service that can:

Understand user preferences
Filter menu items
Recommend dishes
Explain recommendations
Work without WhatsApp

Project structure:

```
whatsapp-food-agent/

├── app/
│   ├── main.py
│   ├── recommendation.py
│
├── data/
│   └── menu.csv
│
├── requirements.txt
└── .env
```

## Phase 2 — Build the Conversation Agent

Now add OpenAI.

Structure:
```
app/

├── agent/
│   ├── food_agent.py
│   ├── prompts.py
│
├── services/
│   └── openai_service.py
```

Goal

Run:

python main.py

and chat in the terminal.

Example:

User:
I want Chinese food.

Bot:
What's your budget?

User:
Under 300

Bot:
Do you prefer dine-in or takeaway?

User:
Takeaway

Bot:
Here are my recommendations...

Still no WhatsApp.

```bash
Simran@Jasmine MINGW64 /d/Project/Whatsapp_food_recommendation_agent (main)
$ python app/main.py 
Food Assistant Started
You: Hi! I am so hungry!
Bot: veg or Non-veg?
You: veg please
Bot: What's your budget ?
You: 300 maybe...
Bot: What type of cusine would you like ?
You: idk italian ? would italian have 300 rupees food or should i increase my price?
Bot: Prefrences collected
{'category': 'Italian', 'budget': '300', 'type': 'veg', 'style': None, 'dish': None}
(whatsappchat)
```


fro the code:

```python
from agent.food_agent import FoodAgent, QUESTIONS, REQUIRED_FIELDS
from agent.memory import ConversationMemory

agent = FoodAgent()
memory = ConversationMemory()


print("Food Assistant Started")


def main() -> None:

    while True:
        user_message =  input("You: ")

        extracted = agent.extract_preferences(user_message)

        memory.update(extracted)

        preferences = memory.get()

        missing = None

        for field in REQUIRED_FIELDS:
            if preferences[field] is None:
                missing = field
                break

        if missing:

            print(f"Bot: {QUESTIONS[missing]}")

        else:

            print("Bot: Prefrences collected")
            print(preferences)

            break

if __name__ == "__main__":
    main()

```
<!-- note even if user gives wrong menu... our llm should check for it in the database and give out the correct name in preference. -->

So... here's the thing. 

(whatsappchat) 
Simran@Jasmine MINGW64 /d/Project/Whatsapp_food_recommendation_agent (main)
$ python app/main.py 
Food Assistant Started
You: HI i want something spicy to eat...
Bot: veg or Non-veg?
You: veg maybe
Bot: What's your budget ?
You: 500 for now
Bot: What type of cusine would you like ?
You: Indian Preferably
Bot: Prefrences collected
{'category': 'Indian', 'budget': '500', 'diet': 'veg', 'style': 'spicy', 'dish': None}
['Paneer Tikka Wrap']
(whatsappchat) 

At the end of Phase 2 you'll have:

Terminal Chat
      ↓
GPT extracts information
      ↓
Memory stores preferences
      ↓
Agent asks follow-up questions
      ↓
Recommendation Engine
      ↓
Food Suggestions

This is the first true "agent" version. Phase 3 would be where we introduce tools, so GPT decides when to call:

Menu Search Tool
Recommendation Tool
FAQ Tool

instead of hardcoded logic. That architecture will transition cleanly into WhatsApp later.

## Phase 3