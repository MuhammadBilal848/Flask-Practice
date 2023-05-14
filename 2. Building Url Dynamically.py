from flask import Flask , redirect , url_for

app = Flask(__name__)

@app.route('/')

def home():
    return 'For checking result visit /result url'


# we can define what datatype does parameter 'mark' have.
# Syntax - @app.route('/any_route/<dtype:paramter_name>')
# @app.route('/result/<int:marks>')
# def result(marks):
#     if marks>=50:
#         res = 'pass'
#     else:
#         res = 'fail'
#     return res

@app.route('/passed/<int:score>')
def passed(score):
    return f'Congratulations!!! You have passed with {score}.'
    # we can also put html as the return statement, but it is not a best practice
    # return '<html><body><h1><center>You have passed</center></h1></body></html>.'
    

@app.route('/failed/<int:score>')
def failed(score):
    return f'Dont give up!!! You have failed with {score}.'

# we can redirect the user on other pages as well using 'redirect' and 'url_for' function of flask module
@app.route('/result/<int:marks>')
def result(marks):
    if marks>=50:
        res = 'passed'
    else:
        res = 'failed'
# say i want to redirect passed user to /passed route while failed user to /failed route
# syntax - redirect(url_for(route_name,parameter_which_route_name_is_using = parameter_which_current_route_is_using))
    return redirect(url_for(res,score = marks))

if __name__ == '__main__':
    app.run(debug=True)