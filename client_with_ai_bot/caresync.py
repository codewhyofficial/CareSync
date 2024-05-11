from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import json
import re
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__) 
CORS(app)

# Fetch the API key from environment variables
GENAI_API_KEY = os.getenv("GENAI_API_KEY")

# Configure with the fetched API key
genai.configure(api_key=GENAI_API_KEY)

@app.route('/generate_response', methods=['POST'])
def generate_response():
    try:
        data = request.get_json()
        prompt = data['prompt']

        # Modify prompt
        stringPrompt = json.dumps(prompt)
        prompt_final = f"{stringPrompt} answer this in a short and crisp way as you are a health advisor and more emphasize on organic things and emotionally connected. make your responses a little bit specific and generate the response in easy and small understandable way."

        # Generate response
        model_name = genai.GenerativeModel('gemini-pro')
        response = model_name.generate_content(prompt_final)
        generated_text = response.text
        cleaned_text = re.sub(r'\**\*', '', generated_text)

        return jsonify({'response': cleaned_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
