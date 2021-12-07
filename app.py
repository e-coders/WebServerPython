import os
try:
	from flask import Flask
except:
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nInstalling Required Dependencies: Flask 2.0.2 with it's required dependencies. Installing...\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	os.system("python -m pip install flask")

app = Flask(__name__)

@app.route("/")
def home():
	return "<h1>Welcome to my own server</h1>\n<p>This is a server, hosted on the web with Flask for free & easily!!</p>\n<p>Wow! I'm live on the web and got our package from the Python file!!</p>\n<p>This will works only on the localhost:8000 server, or whatever you will choose in the line 14 of your python file.</p>\n<p><b>Tip:</b> Use Backward Slash and n without spaces to add a line break in the source of our site!</p>"

if __name__ == '__main__':
	app.run(debug=True,port=8000)
