from sanic import Sanic
from sanic.response import json, text
from os import environ

app = Sanic(name='api')

@app.route('/api/callback', methods=['POST'])
async def callback(request):
	if request.json.get('type') == 'confirmation':
		return text(environ.get('confirmation_token', ''))

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000, debug=True)