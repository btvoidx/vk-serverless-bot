from sanic import Sanic
from sanic.response import text
from os import environ

app = Sanic(name='api')

@app.route('/api/callback', methods=['POST'])
async def callback(request):
	if environ.get('secret', '') != request.json.get('secret', ''):
		return text('invalid secret')

	if request.json.get('type') == 'confirmation':
		return text(environ.get('confirmation_token', ''))
	
	elif request.json.get('type') == 'message_new':
		msg = request.json['object']['text']
		from_id = request.json['object']['from_id']

		if msg:
			requests.get(f"https://api.vk.com/method/messages.send?message={msg}&user_id={from_id}&access_token={environ.get('access_token', '')}&v=5.78").json()

	return text('ok')

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000, debug=True)