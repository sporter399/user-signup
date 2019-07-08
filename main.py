from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 


@app.route("/add", methods=['POST'])
def add_user_info():
    user_name = request.form['user-name']
    password = request.form['password']
    rep_password = request.form['rep_password']
    e_mail = request.form['e_mail']
    

    if (len(user_name) <= 3) or (user_name.strip() == ""):
        user_error = "User names must contain at least 4 characters. Please try again."
        return redirect("/?user_error=" + user_error)

    user_name_escaped = cgi.escape(user_name, quote=True)

    

    if (len(password) <= 3) or (password.strip() == ""):
        pass_error = "Passwords must contain at least 4 characters. Please try again."
        return redirect("/?pass_error=" + pass_error)

    password_escaped = cgi.escape(password, quote=True)

    if (rep_password != password):
        rep_pass_error = "Your passwords do not match. Please try again."
        return redirect("/?pass_error=" + rep_pass_error)

    password_escaped = cgi.escape(rep_password, quote=True)

    if (len(e_mail) <= 3) or (len(e_mail) >= 20) or (e_mail.strip() == "") or ('@' not in e_mail) or ('.' not in e_mail):
        mail_error = "Email addresses must contain '@' and '.' and be between 3 and 20 characters long. Please try again."
        return redirect("/?mail_error=" + mail_error)

    e_mail_escaped = cgi.escape(e_mail, quote=True)




    return render_template('add-confirmation.html', name=user_name, password=password, rep_password=rep_password, e_mail=e_mail)




@app.route("/")
def index():
    user_encoded_error = request.args.get("user_error")
    pass_encoded_error = request.args.get("pass_error")
    rep_pass_encoded_error = request.args.get("rep_pass_error")
    e_mail_encoded_error = request.args.get("mail_error")
    
    return render_template('edit.html', user_error=user_encoded_error and cgi.escape(user_encoded_error, quote=True), 
        pass_error=pass_encoded_error and cgi.escape(pass_encoded_error, quote=True), rep_pass_error=rep_pass_encoded_error and
        cgi.escape(rep_pass_encoded_error, quote=True), mail_error=e_mail_encoded_error and cgi.escape(e_mail_encoded_error, quote=True))


app.run()