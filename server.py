from cgi import print_environ_usage 
from flask import Flask, render_template  
app = Flask(__name__)    

@app.route('/play')
def index():
    return render_template("index.html")

@app.route('/play/<int:num>')
def numbox(num):
    return render_template("index2.html",num=num)

@app.route('/play/<int:num>/<string:color>')
def colornumbox(num,color):
    return render_template("index2.html",num=num,color=color)

# @app.route('/users/<username>/<id>')
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username + ", id: " + id

if __name__=="__main__":   
    app.run(debug=True)    




