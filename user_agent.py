from flask import Flask
from user_agent import generate_user_agent

app = Flask('app')

@app.route('/generate-user-agent/')
def Markk():
	user_agent = str(''.join(generate_user_agent() for i in range(1)))
	return {"result":user_agent}
app.run()