##building url dynamically
##variable rules
##jinja2 template engine- 3 methods
'''
1. {{ }} expression to print output in html
2. {%..%} conditions, for loops
3. {#..#} this is for comments
'''


from flask import Flask,render_template,request,redirect,url_for
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

@app.route('/submit1',methods=['GET','POST'])
def submit1():
    if request.method=='POST':
        name=request.form['name']
        return f'hello {name}!'
    return render_template('form.html')


##variable rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template('result.html',results=res)


@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    exp={'score':score,"res":res}
    return render_template('result1.html',results=exp)

## if condition
@app.route('/successif/<int:score>')
def successif(score):
    

    return render_template('result.html',results=score)




@app.route('/fail/<int:score>')
def fail(score):
    

    return render_template('result.html',results=score)


@app.route('/submit', methods=['GET','POST'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        C=float(request.form['C'])
        Datascience=float(request.form['Datascience'])

        total_score=(science+maths+C+Datascience)/4
    else:
        return render_template('getresult.html')    
    return redirect(url_for('successres', score=total_score))
    

    return render_template('result.html',results=score)






if __name__=="__main__":
    app.run(debug=True)