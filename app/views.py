from app import app
from flask import render_template,request,jsonify
from get_user_alerts import get_user_alerts,save_alert,save_service
from create_alert import create_alert

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/search', methods=['POST'])
def get_results():
	 data = request.data
	 return data


@app.route('/api/post-alert', methods=['POST'])
def post_alert():
    content = request.get_json()
    print content
    save_alert(content)
    return ''

@app.route('/api/post-service', methods=['POST'])
def post_service():
    content = request.get_json()
    print content
    save_service(content)
    return ''

@app.route('/api/get-user-alerts/<service>/<area>')
def alerts(service, area):
	return jsonify(get_user_alerts(service, area))

# @app.route('/create-alert/<service>/<area>/<name>')
# def route_create_alert(service, area, name):
# 	return create_alert(service, area, name)
