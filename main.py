from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 


@app.route("/add", methods=['POST'])
def add_user_info():
    user_name = request.form['user-name']
    password = request.form['password']
    

    if (len(user_name) <= 3) or (user_name.strip() == ""):
        user_error = "User names must contain at least 4 characters. Please try again."
        return redirect("/?user_error=" + user_error)

        user_name_escaped = cgi.escape(user_name, quote=True)

    

    if (len(password) <= 3) or (password.strip() == ""):
        pass_error = "Passwords must contain at least 4 characters. Please try again."
        return redirect("/?pass_error=" + pass_error)

    password_escaped = cgi.escape(password, quote=True)


    return render_template('add-confirmation.html', name=user_name, password=password)




@app.route("/")
def index():
    user_encoded_error = request.args.get("user_error")
    pass_encoded_error = request.args.get("pass_error")
    return render_template('edit.html', user_error=user_encoded_error and cgi.escape(user_encoded_error, quote=True), 
        pass_error=pass_encoded_error and cgi.escape(pass_encoded_error, quote=True))


app.run()