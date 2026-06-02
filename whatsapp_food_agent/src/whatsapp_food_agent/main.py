from whatsapp_food_agent.agent.food_agent import FoodAgent, QUESTIONS, REQUIRED_FIELDS
from whatsapp_food_agent.agent.memory import ConversationMemory
from whatsapp_food_agent.recomendations.recommendation import recommend_food
from whatsapp_food_agent.database.database import create_table

agent = FoodAgent()
memory = ConversationMemory()


print("Food Assistant Started")


def main() -> None:
    create_table()

    # while True:
    #     user_message =  input("You: ")

    #     extracted = agent.extract_preferences(user_message)

    #     memory.update(extracted)

    #     preferences = memory.get()

    #     missing = None

    #     for field in REQUIRED_FIELDS:
    #         if preferences[field] is None:
    #             missing = field
    #             break

    #     if missing:

    #         print(f"Bot: {QUESTIONS[missing]}")

    #     else:

    #         print("Bot: Prefrences collected")
    #         print(preferences)
    #         recommended = recommend_food(preferences)
    #         print(recommended)

    #         break

if __name__ == "__main__":
    main()



# from recommendation import recommend_food

# preferences = {
#     'type' : 'veg',
#     'category' : 'Indian',
#     'budget' : 250,
#     'style' : 'spicy'
# }

# preferences2 = {
#     'type' : 'veg',
#     'category' : 'japanese',
#     'budget' : 500,
#     # 'style' : 'spicy'
# }


# dishes = recommend_food(preferences2)

# print("Recommended dishes: \n", dishes)