class ConversationMemory:

    def __init__(self):

        self.prefrences = {
            "category": "",
            "budget": "",
            "type": "",
            "style": "",
            "dish": ""
        }

    def update(self, extracted):

        for key, value in extracted.items():
            if value:
                self.prefrences[key] = value

    def get(self):
        return self.prefrences