#!/usr/bin/env python3
"""
================================================================================
LOCAL DEVELOPMENT SERVER
Ethical Alignment API - Run this to test demo.html locally
================================================================================

Usage:
    python app.py

Then visit: http://localhost:5000/demo.html

The server will:
- Serve static HTML/CSS/JS files
- Provide the /api/evaluate endpoint for ethical validation
- Allow testing of the demo interface with real backend responses
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import json
import os
from AI_RED_LETTER_ETHICAL_GUARDRAIL import ARLREG_CORE, ConductProfile, EthicalState

# ===== FLASK APP SETUP =====
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# ===== STATIC FILE SERVING =====
@app.route('/')
def index():
    """Serve index.html"""
    return send_file('index.html', mimetype='text/html')

@app.route('/demo.html')
def demo():
    """Serve demo.html"""
    return send_file('demo.html', mimetype='text/html')

# ===== API ENDPOINTS =====

@app.route('/api/evaluate', methods=['POST'])
def evaluate():
    """
    Main ethical alignment evaluation endpoint
    
    Request body:
    {
        "request": "user prompt to evaluate",
        "context": "optional context about the request",
        "conduct_profile": "COOPERATIVE" (optional, defaults to COOPERATIVE)
    }
    
    Response:
    {
        "status": "ALLOWED" | "BLOCKED",
        "message": "human-readable explanation",
        "reasoning": "detailed reasoning from ethical guardrail",
        "can_execute": true | false
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'request' not in data:
            return jsonify({
                'status': 'BLOCKED',
                'message': 'Missing required field: request',
                'reasoning': 'Request body must contain "request" field'
            }), 400
        
        user_input = data.get('request', '')
        conduct_str = data.get('conduct_profile', 'COOPERATIVE')
        metadata = data.get('metadata', {})
        context = data.get('context', '')
        
        # Default metadata for demo
        if not metadata:
            metadata = {
                'is_beneficial_to_other': True,
                'motivation': 'assistance',
                'power_imbalance': False
            }
        
        # Validate conduct profile
        try:
            conduct = ConductProfile[conduct_str]
        except KeyError:
            return jsonify({
                'status': 'BLOCKED',
                'message': f'Invalid conduct_profile: {conduct_str}',
                'reasoning': f'Must be one of: {", ".join([c.name for c in ConductProfile])}'
            }), 400
        
        # Evaluate request
        ethical_status, reason, details = ARLREG_CORE.evaluate_request(
            user_input=user_input,
            conduct_profile=conduct,
            request_metadata=metadata
        )
        
        # Generate response
        response = ARLREG_CORE.generate_response(user_input, ethical_status, reason)
        
        # Format for demo.html
        return jsonify({
            'status': 'ALLOWED' if ethical_status == EthicalState.APPROVED else 'BLOCKED',
            'message': response['message'],
            'reasoning': response['reasoning'],
            'can_execute': response['can_execute'],
            'protocol': response.get('protocol', 'ARLREG'),
            'details': details
        }), response['status']
    
    except Exception as e:
        return jsonify({
            'status': 'BLOCKED',
            'message': 'Internal server error',
            'reasoning': str(e),
            'can_execute': False
        }), 500


@app.route('/api/manifest', methods=['GET'])
def manifest():
    """
    Return system manifest - lists all ethical rules and protocols
    """
    try:
        manifest = ARLREG_CORE.get_system_manifest()
        return jsonify(manifest), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Ethical Alignment API',
        'version': '2.0.0'
    }), 200


# ===== ERROR HANDLERS =====

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# ===== MAIN =====

if __name__ == '__main__':
    print("""
    ╔════════════════════════════════════════════════════════════════╗
    ║   ETHICAL ALIGNMENT API - LOCAL DEVELOPMENT SERVER              ║
    ║   Powered by Red Letter Protocol (ARLREG v2.0)                  ║
    ╚════════════════════════════════════════════════════════════════╝
    
    🚀 Starting server...
    
    📍 Access points:
       • Demo Interface:  http://localhost:5000/demo.html
       • Main Site:       http://localhost:5000/
       • API Health:      http://localhost:5000/api/health
       • API Manifest:    http://localhost:5000/api/manifest
    
    📝 To test the API from command line:
       
       curl -X POST http://localhost:5000/api/evaluate \\
         -H "Content-Type: application/json" \\
         -d '{
           "request": "Help this person with honest advice",
           "conduct_profile": "COOPERATIVE",
           "metadata": {
             "is_beneficial_to_other": true,
             "motivation": "assistance",
             "power_imbalance": false
           }
         }'
    
    ⚙️  Server running on http://127.0.0.1:5000
       Press CTRL+C to stop
    
    """)
    
    # Run development server
    app.run(host='127.0.0.1', port=5000, debug=True)
