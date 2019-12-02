from flask import Flask, render_template,request
import os
app = Flask(__name__)
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

@app.route("/", methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        amountDispensed = request.form.get('cups')
        print(amountDispensed)
        os.system('ssh pi@128.194.51.251')
        os.system('shreyasalex')
    return render_template('index.html',amount = p1)

if __name__ == "__main__":
  app.run(host = '0.0.0.0', port = '80', debug = True)