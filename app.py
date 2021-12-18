from flask import Flask,render_template,request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

host = "smtp.gmail.com"
port = "587"
login = ""
senha = "" #para funcionar basta colocar email e senha 

@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato',methods = ['GET','POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        message = request.form.get('mensagem')
        server = smtplib.SMTP(host, port)
        server.ehlo()
        server.starttls()
        server.login(login, senha)

        msg=(f'Churrascaria Grill! Você recebeu uma mensagem de: \n {nome} \n com o email:  {email} com a mensagem: \n\n {message}')

        email_msg = MIMEMultipart()
        email_msg['From'] = login
        email_msg['To'] = login
        email_msg['Subject'] = "Email da Churrascaria"
        email_msg.attach(MIMEText(msg,'Plain'))
        server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
        server.quit()

        return render_template('contato.html', message=message)
    return render_template('contato.html')


from app import app

if __name__ == "__main__":
    app.run(debug=True)
