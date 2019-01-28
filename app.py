from flask import Flask,render_template

app = Flask(__name__)
blog = {
    'name': 'My awesome blog',
    'post':{
        1:{
            'post': 1,
            'title': 'First post',
            'contact': 'Hello, world'
       
        }
    }
}
 


@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__': 
    app.run(debug=True) 