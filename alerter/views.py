from alerter import app
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from flask.ext.httpauth import HTTPBasicAuth

auth  = HTTPBasicAuth()

alerts = [
        {
            'id': 1,
            'subject': 'an alert',
            'status': 'critical',
        },
        {
            'id': 2,
            'subject': 'another alert',
            'status': 'warning',
        }
    ]

@auth.get_password
def get_password(username):
    if username == 'chris':
        return 'alerta'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
@app.route('/index')
def index():
        return "Hello, World!"

@app.route('/api/v1.0/alerts', methods=['GET'])
@auth.login_required
def get_alerts():
    return jsonify({'alerts': alerts})

@app.route('/api/v1.0/alerts/<int:alert_id>', methods=['GET'])
@auth.login_required
def get_alert(alert_id):
    alert = filter(lambda a: a['id'] == alert_id, alerts)
    if len(alert) == 0:
        abort(404)
    return jsonify({'alert': alert[0]})

@app.route('/api/v1.0/alerts', methods=['POST'])
@auth.login_required
def create_alert():
    alert = {
            'id': alerts[-1]['id'] + 1,
            'subject': 'yet another alert',
            'status': request.json['status'],
            'subject': request.json['subject'],
            }
    alerts.append(alert)
    return jsonify({'alert': alert}), 201

@app.route('/api/v1.0/alerts/<int:alert_id>', methods=['DELETE'])
@auth.login_required
def delete_alert(alert_id):
    alert = filter(lambda a: a['id'] == alert_id, alerts)
    if len(alert) == 0:
        abort(404)

    alerts.remove(alert[0])
    return jsonify({'result': True})
