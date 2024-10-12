from flask import Flask, render_template, request, jsonify
from langchain_groq import ChatGroq

app = Flask(__name__)

# Define the API key directly in the code.
api_key = "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"

# Create a ChatGroq client using the embedded API key.
llm = ChatGroq(
    temperature=0,
    api_key=api_key,
    model_name="llama3-70b-8192"
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']

    # Generate a response using the Groq API for a personal assistant.
    input_prompt = f"""
    You are a personal assistant designed to help users manage their daily tasks, answer questions, and provide information on various topics. Your primary goal is to assist users in their daily lives by providing accurate and relevant information. If a user asks a question outside of your capabilities, respond politely with a friendly message, encouraging them to ask about something you can assist with.

    User: "{user_input}"
    Assistant:
    """

    # Invoke the Groq model.
    response = llm.invoke(input_prompt)
    
    return jsonify({'response': response.content})

if __name__ == '__main__':
    app.run(debug=True)
