from alerter import app
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request

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

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
@app.route('/index')
def index():
        return "Hello, World!"

@app.route('/api/v1.0/alerts', methods=['GET'])
def get_alerts():
    return jsonify({'alerts': alerts})

@app.route('/api/v1.0/alerts/<int:alert_id>', methods=['GET'])
def get_alert(alert_id):
    alert = filter(lambda a: a['id'] == alert_id, alerts)
    if len(alert) == 0:
        abort(404)
    return jsonify({'alert': alert[0]})

@app.route('/api/v1.0/alerts', methods=['POST'])
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
def delete_alert(alert_id):
    alert = filter(lambda a: a['id'] == alert_id, alerts)
    if len(alert) == 0:
        abort(404)

    alerts.remove(alert[0])
    return jsonify({'result': True})
