import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from utils.groq_client import generate_completion
from utils.prompts import get_campaign_prompt, get_sales_pitch_prompt, get_lead_scoring_prompt

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/campaign', methods=['POST'])
def generate_campaign():
    try:
        data = request.json
        product = data.get('product')
        audience = data.get('audience')
        platform = data.get('platform')
        
        if not all([product, audience, platform]):
            return jsonify({'error': 'Missing required fields'}), 400
            
        prompt = get_campaign_prompt(product, audience, platform)
        result = generate_completion(prompt)
        
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/pitch', methods=['POST'])
def generate_pitch():
    try:
        data = request.json
        product = data.get('product')
        persona = data.get('persona')
        
        if not all([product, persona]):
            return jsonify({'error': 'Missing required fields'}), 400
            
        prompt = get_sales_pitch_prompt(product, persona)
        result = generate_completion(prompt)
        
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/score', methods=['POST'])
def score_lead():
    try:
        data = request.json
        lead_name = data.get('lead_name')
        budget = data.get('budget')
        need = data.get('need')
        urgency = data.get('urgency')
        
        if not all([lead_name, budget, need, urgency]):
            return jsonify({'error': 'Missing required fields'}), 400
            
        prompt = get_lead_scoring_prompt(lead_name, budget, need, urgency)
        # Using json_mode=True for structured data
        result = generate_completion(prompt, json_mode=True)
        
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
