!pip install flask

from flask import Flask, render_template, request, jsonify
import language_tool_python

from chat import chatbot

app = Flask(__name__)

# Initialize LanguageTool
tool = language_tool_python.LanguageTool('en-US')

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
    message = str(request.form['messageText'])
    
    # Handle the grammar correction using LanguageTool
    matches = tool.check(message)
    corrected_text = language_tool_python.utils.correct(message, matches)
    print(corrected_text)
    
    bot_response = chatbot(corrected_text) 
    return jsonify({'status': 'OK', 'answer': bot_response})

if __name__ == "__main__":
    app.run(debug=True)

