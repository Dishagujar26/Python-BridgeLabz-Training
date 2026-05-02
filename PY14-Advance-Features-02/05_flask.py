from flask import  Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello Disha</h1>"

app.run()

# Flask in python - web framework in python that allows you to create web applications. It is a micro framework that is lightweight and easy to use. 
# It is used to create web applications in python. 

# pip install flask - install flask