from sanic import Sanic
from sanic.response import text
from os import environ

app = Sanic(name='api')

@app.route('/api/callback', methods=['POST'])
async def callback(request):
	if environ.get('secret') != request.json.get('secret'):
		return text('invalid secret')

	if request.json.get('type') == 'confirmation':
		return text(environ.get('confirmation_token', ''))
	
	print(request.json)

	return text('ok')

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000, debug=True)