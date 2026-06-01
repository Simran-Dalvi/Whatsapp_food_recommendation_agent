class ConversationMemory:

    def __init__(self):

        self.prefrences = {
            "category": None,
            "budget": None,
            "diet": None,
            "style": None,
            "dish": None
        }

    def update(self, extracted):

        for key, value in extracted.items():
            if value:
                self.prefrences[key] = value

    def get(self):
        return self.prefrences