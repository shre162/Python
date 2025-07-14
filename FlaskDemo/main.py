from flask import Flask,render_template
'''
it creates an instance of the flask class,
which will be your WSGI application. ex.app instance
'''
##wsgi app
app=Flask(__name__)

##basic router
@app.route("/")
def welcome():
    return "<html><h1>welcomee</h1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
if __name__=="__main__":
    app.run(debug=True)