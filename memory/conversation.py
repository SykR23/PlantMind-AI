class ConversationMemory:

    def __init__(self):
        self.messages = []

    def add_user_messages(self, message: str):
        self.messages.append(
            {
                "role": "user",
                "content": message
            }
        )

    def add_assistant_message(self, message: str):
        self.messages.append(
            {
                "role": "user",
                "content": message
            }
        )

    def get_history(self):
        return self.messages

    def clear(self):
        self.messages = []