# Whatsapp_food_recommendation_agent

This is food recomendation chat bot.
Phase 1:
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

Phase 2 — Build the Conversation Agent

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