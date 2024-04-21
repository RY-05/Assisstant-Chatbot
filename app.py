from flask import Flask, render_template, request, jsonify
import openai
import datetime

app = Flask(__name__)

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

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    user_input = request.form["user_input"]
    response = ""

    if "remind me to" in user_input.lower():
        reminder = user_input.lower().replace("remind me to ", "")
        add_reminder(reminder)
        response = "Reminder added!"
    elif user_input.lower() == "show reminders":
        reminders = get_reminders()
        if reminders:
            response = "Your reminders for today:<br>"
            for reminder in reminders:
                response += "- " + reminder + "<br>"
        else:
            response = "You have no reminders for today."

    else:
        response = openai.Completion.create(
            engine="davinci",
            prompt=user_input + "\nAssistant:"
        ).choices[0].text.strip()

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
