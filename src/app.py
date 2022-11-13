from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "I am viraj. I hosted this application today 13 Nov. 2022"

if __name__ == '__main__':
	app.run()