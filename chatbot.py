import openai
import datetime

# Set up OpenAI API key
openai.api_key = "your_openai_api_key_here"

# Initialize the to-do list
todo_list = []

def add_reminder(reminder):
    # Add reminder to the to-do list
    todo_list.append({"task": reminder, "date": datetime.datetime.now()})

def get_reminders():
    # Get reminders for today
    today = datetime.datetime.now().date()
    reminders = [task["task"] for task in todo_list if task["date"].date() == today]
    return reminders

def chat_with_assistant():
    print("Welcome! How can I assist you today?")
    while True:
        user_input = input("You: ")
        
        # Check for exit command
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        # Check for adding reminder command
        elif "remind me to" in user_input.lower():
            reminder = user_input.lower().replace("remind me to ", "")
            add_reminder(reminder)
            print("Reminder added!")

        # Check for getting reminders command
        elif user_input.lower() == "show reminders":
            reminders = get_reminders()
            if reminders:
                print("Your reminders for today:")
                for reminder in reminders:
                    print("-", reminder)
            else:
                print("You have no reminders for today.")
        
        # Handle other queries using ChatGPT
        else:
            response = openai.Completion.create(
                engine="davinci", 
                prompt=user_input + "\nAssistant:"
            )
            print("Assistant:", response.choices[0].text.strip())

if __name__ == "__main__":
    chat_with_assistant()
