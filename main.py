from flask import Flask,redirect,url_for,render_template,request,make_response,session
from flask_wtf.csrf import CSRFProtect

import forms

app=Flask(__name__)
app.secret_key = '\x9ff\xfc\xeb\xbb\xb7\xe1\x9f\x91^\x97\xa3\xe6Mn\xd6\xa4\x00K\x92\x15X\xa8\xf6'
csrf = CSRFProtect(app)

@app.route('/',methods = ['GET','POST'])
def home():
    if 'usuario' in session:
        usuario = session['usuario']
        print(usuario)
    return usuario
    # custom_cookie = request.cookies.get('custom_cookie','Undefined')
    # print(custom_cookie)
    # comment_form = forms.CommentForm(request.form)
    # if request.method == 'POST' and comment_form.validate():
    #     print(comment_form.username.data)
    #     print(comment_form.email.data)
    #     print(comment_form.comment.data)
    # else:
    #     print("Error en el formulario")
    
    # nombre = 'Angel'
    # return render_template('user.html',nombre=nombre,form = comment_form)

@app.route('/cookie')
def cookie():
    response = make_response(render_template('cookie.html'))
    response.set_cookie('custom_cookie','Angel Colman')
    return response;

@app.route('/login',methods=[ 'GET','POST' ])
def login():
    login_form = forms.LoginForm(request.form)
    if request.method=='POST' and login_form.validate():
       session['usuario'] = login_form.usuario.data
       
    return render_template('login.html',form = login_form,titulo='Login')

@app.route('/cerrar_sesion')
def cerrarSesion():
    if 'usuario' in session:
        pass
    return redirect(url_for('login'))
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
    
