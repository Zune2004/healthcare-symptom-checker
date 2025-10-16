from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Setup Gemini
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Missing GEMINI_API_KEY")
    exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

# Medical prompt - keeps things educational
MEDICAL_PROMPT = """You are a helpful educational health information assistant.

DISCLAIMER: This is EDUCATIONAL ONLY. NOT medical advice. See a real doctor.

When someone describes symptoms:
1. List 2-4 possible conditions (general info only)
2. Explain what each might mean
3. Say when to see a doctor
4. If it sounds serious (chest pain, can't breathe), say go to ER now

Keep it simple and clear. Always remind them to see a doctor."""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/check-symptoms', methods=['POST'])
def analyze():
    try:
        body = request.get_json()
        symptoms = body.get('symptoms', '').strip()
        
        # Basic validation
        if not symptoms:
            return jsonify({'error': 'Please tell me your symptoms'}), 400
        
        if len(symptoms) < 10:
            return jsonify({'error': 'Need more details about your symptoms'}), 400
        
        # Ask gemini
        full_prompt = f"{MEDICAL_PROMPT}\n\nSymptoms: {symptoms}\n\nProvide educational information about these symptoms."
        
        response = model.generate_content(full_prompt)
        result_text = response.text
        
        return jsonify({
            'success': True,
            'analysis': result_text,
            'warning': 'Remember: This is educational info only. Always see a doctor for real medical advice.'
        })
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': f'Something went wrong: {str(e)}'}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)