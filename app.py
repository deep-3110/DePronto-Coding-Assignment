
from flask import Flask, render_template, request,redirect,url_for
app = Flask(__name__)
  
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/projects', methods=['GET', 'POST'])
def projects():
    return render_template('projects.html')


@app.route('/blogs', methods=['GET', 'POST'])
def blogs():
    return render_template('blogs.html')

@app.route('/contactus', methods=['GET', 'POST'])
def contactus():

    return render_template('contactus.html')

@app.route('/ThankYou', methods=['GET', 'POST'])
def ThankYou():
    if request.method == "GET":
        name=request.form.get("username")
        date=request.form.get("date")
        title=request.form.get("title")
        message=request.form.get("message")
        promomail=request.form.get("cb1")
        prodcmail=request.form.get("cb2")
        gender=request.form.get("gender")
        print('\nName:' + str(name))
        print('\nDate:' + str(date))
        print('\nTitle:' + str(title))
        print('\nmessage:' + str(message))
        print('\nPromotional mail:' + str(promomail))
        print('\nProduct Mail:' + str(prodcmail))
        print('\nGender:' + str(gender))
    return render_template('ThankYou.html')
if __name__ == '__main__':


    app.run(host = "localhost", debug = True)
    app.config["CACHE_TYPE"] = "null"