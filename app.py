from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/static_files')

def static_files():
    return render_template('static_files.html')

@FAI.route('/new')
def new():
    return render_template('new.html')


FAI.run(debug=True)