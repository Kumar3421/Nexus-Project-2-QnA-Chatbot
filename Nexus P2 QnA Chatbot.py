import random

class AdmissionChatbot:
    def __init__(self):
        self.admission_info = {
            "procedures": "The admission process involves submitting an application, transcripts, and letters of recommendation.",
            "requirements": "Typical requirements include a high school diploma, standardized test scores, and recommendation letters.",
            "deadlines": "Admission deadlines vary by college, but they are usually in the early months of the year. It's advisable to check with the specific college for accurate information."
        }
        self.previous_context = {}

    def greet(self):
        return "Hello! I'm the College Admission Chatbot. How can I assist you with your admission queries?"

    def farewell(self):
        return "Good luck with your college admission! If you have more questions, feel free to ask later."

    def respond_to_question(self, question):
        if "procedures" in question.lower():
            return self.admission_info["procedures"]
        elif "requirements" in question.lower():
            return self.admission_info["requirements"]
        elif "deadlines" in question.lower():
            return self.admission_info["deadlines"]
        elif "bye" in question.lower():
            return self.farewell()
        else:
            return "I'm not sure how to respond to that. Can you ask me something related to college admission?"

    def ask_user_questions(self):
        user_input = input("What would you like to know about college admission? ")
        return {"user_query": user_input}

    def chat(self):
        print(self.greet())

        while True:
            user_responses = self.ask_user_questions()
            self.previous_context.update(user_responses)

            print("\nLet me find the information for you...")
            print("User Query:", user_responses["user_query"])

            print("\nResponding to your question...")
            response = self.respond_to_question(user_responses["user_query"])
            print(response)

            if "bye" in user_responses["user_query"].lower():
                break

if __name__ == "__main__":
    admission_chatbot = AdmissionChatbot()
    admission_chatbot.chat()
