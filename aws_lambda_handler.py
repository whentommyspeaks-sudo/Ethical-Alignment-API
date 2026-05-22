"""
================================================================================
AWS LAMBDA DEPLOYMENT CONFIGURATION
AI Red Letter Ethical Guardrail (ARLREG) v2.0
================================================================================
"""

import json
import os
from typing import Dict, Any

# ===== AWS LAMBDA HANDLER =====
def lambda_handler(event, context):
    """
    Main Lambda handler for ARLREG API endpoints
    Event structure from API Gateway
    """
    
    try:
        # Parse request
        http_method = event['httpMethod']
        path = event['path']
        body = json.loads(event.get('body', '{}'))
        headers = event.get('headers', {})
        
        # Validate API key
        api_key = headers.get('Authorization', '').replace('Bearer ', '')
        if not api_key:
            return {
                'statusCode': 401,
                'body': json.dumps({'error': 'Missing API key'})
            }
        
        # Route requests
        if path == '/v1/validate' and http_method == 'POST':
            return validate_endpoint(body, api_key)
        
        elif path == '/v1/manifest' and http_method == 'GET':
            return manifest_endpoint(api_key)
        
        elif path == '/v1/conduct-check' and http_method == 'POST':
            return conduct_check_endpoint(body, api_key)
        
        elif path == '/health' and http_method == 'GET':
            return {'statusCode': 200, 'body': json.dumps({'status': 'healthy'})}
        
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Endpoint not found'})
            }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }


def validate_endpoint(body: Dict, api_key: str) -> Dict:
    """Validate action against ethical guardrails"""
    from AI_RED_LETTER_ETHICAL_GUARDRAIL import ARLREG_CORE, ConductProfile, EthicalState
    
    try:
        request = body.get('request', '')
        conduct_str = body.get('conduct_profile', 'COOPERATIVE')
        metadata = body.get('metadata', {})
        
        # Convert conduct string to enum
        conduct = ConductProfile[conduct_str]
        
        # Evaluate
        status, reason, details = ARLREG_CORE.evaluate_request(
            user_input=request,
            conduct_profile=conduct,
            request_metadata=metadata
        )
        
        # Generate response
        response = ARLREG_CORE.generate_response(request, status, reason)
        
        return {
            'statusCode': response['status'],
            'body': json.dumps(response),
            'headers': {'Content-Type': 'application/json'}
        }
    
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': f'Validation error: {str(e)}'}),
            'headers': {'Content-Type': 'application/json'}
        }


def manifest_endpoint(api_key: str) -> Dict:
    """Return system manifest"""
    from AI_RED_LETTER_ETHICAL_GUARDRAIL import ARLREG_CORE
    
    manifest = ARLREG_CORE.get_system_manifest()
    
    return {
        'statusCode': 200,
        'body': json.dumps(manifest),
        'headers': {'Content-Type': 'application/json'}
    }


def conduct_check_endpoint(body: Dict, api_key: str) -> Dict:
    """Check user conduct profile"""
    behavior = body.get('behavior', '')
    
    # Simple conduct analysis
    conduct_analysis = {
        'conduct_profile': 'COOPERATIVE',
        'severity': 'low',
        'recommended_action': 'continue',
        'block_request': False
    }
    
    hostile_keywords = ['threat', 'attack', 'harm', 'destroy', 'kill']
    deceptive_keywords = ['lie', 'deceive', 'fake', 'false']
    
    for keyword in hostile_keywords:
        if keyword.lower() in behavior.lower():
            conduct_analysis['conduct_profile'] = 'HOSTILE'
            conduct_analysis['severity'] = 'high'
            conduct_analysis['recommended_action'] = 'de-escalation'
            conduct_analysis['block_request'] = True
            break
    
    for keyword in deceptive_keywords:
        if keyword.lower() in behavior.lower():
            conduct_analysis['conduct_profile'] = 'DECEPTIVE'
            conduct_analysis['severity'] = 'high'
            conduct_analysis['recommended_action'] = 'verification'
            conduct_analysis['block_request'] = True
            break
    
    return {
        'statusCode': 200,
        'body': json.dumps(conduct_analysis),
        'headers': {'Content-Type': 'application/json'}
    }


if __name__ == '__main__':
    print('AWS Lambda handler ready for deployment')
    print('Deploy with: serverless deploy')
