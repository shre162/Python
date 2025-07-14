from flask import Flask
'''
it creates an instance of the flask class,
which will be your WSGI application. ex.app instance
'''
##wsgi app
app=Flask(__name__)

##basic router
@app.route("/")
def welcome():
    return "welcome hello hoo"

@app.route("/index")
def index():
    return "welcome"
if __name__=="__main__":
    app.run(debug=True)