from flask import Flask , redirect , url_for , render_template,request

app = Flask(__name__)

# Jinja is a web template engine for the Python programming language
# '''
# {%...%} for statements
# {{...}} for expressions
# {#...#} for comments
# '''
    
@app.route('/')
def home():
    # we can use any html file we want using render_template(file_name), for this we must create a folder 
    # named 'templates' in the same directory as this file and create html files there.
    return render_template('index.html')

@app.route('/passed/<int:score>')
def passed(score):
    res = ''
    if score >= 50:
        res = 'PASS'
    else: 
        res = 'FAIL'
    dicto = {'score':score , 'res':res}
    return render_template('result 1.html',result = dicto)
    ##########################################################################################################################
    # we can write the if else condition using {{ }} expression in result.html
    # return render_template('result 2.html',result = score)
    ##########################################################################################################################


 
@app.route('/submit',methods = ['POST','GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        datastructure = float(request.form['datastructure']) 
        linearalgebra  = float(request.form['linearalgebra'])
        statistics = float(request.form['statistics'])      
        total_score = (datastructure+linearalgebra+statistics)/3
    # syntax - redirect(url_for(route_name,parameter_which_route_name_is_using = parameter_which_current_route_is_using))
    return redirect(url_for('passed',score = total_score))

if __name__ == '__main__':
    app.run(debug=True)
