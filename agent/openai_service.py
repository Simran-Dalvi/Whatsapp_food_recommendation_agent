from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
# print("API key loaded", os.getenv("OPENAI_API_KEY"))
# print("FILE STARTED")
client = OpenAI(
    api_key =os.getenv("OPENAI_API_KEY")
)

def chat_bot(user_msg: str) -> str:
    """
    Send a message to OpenAI and return the response
    """
    # print("inside chat bot")
    response = client.responses.create(
        model="gpt-5.4-mini",
        input = user_msg,
        # temprature = 0
    )

    return response.output_text

def main() -> None:
    print("Now talking to the ChatBot")
    while True:
        # print("getting user input")
        user_input = input("You: ")
        if user_input.lower() == "quiet":
            break
        # print("print response")
        response = chat_bot(user_input)

        print(f"Bot: {response}")

if __name__ == "__main__":
    main()