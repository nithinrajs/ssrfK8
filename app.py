from flask import Flask, request, jsonify, render_template, send_from_directory, redirect, url_for, Response
import requests

#Get Env Variables
def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)


app = Flask(__name__,static_url_path='/static')

#App Routing
@app.route('/')
def index():
        return app.send_static_file('home.html')

@app.route('/search', methods=['POST'])
def search():
	search = request.form['search']
	response = requests.get(search)
	return Response(response.content, mimetype='text/plain')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8080)


