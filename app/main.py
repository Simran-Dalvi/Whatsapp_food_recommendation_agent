from agent.food_agent import FoodAgent, QUESTIONS, REQUIRED_FIELDS
from agent.memory import ConversationMemory
from recommendation import recommend_food

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
            recommended = recommend_food(preferences)
            print(recommended)

            break

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