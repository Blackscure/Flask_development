from flask import Flask,render_template

app = Flask(__name__)
blog = {
    'name': 'My awesome blog',
    'posts':{
        1:{
            'post_id': 1,
            'title': 'First post',
            'contact': 'Hello, world'
       
        }
    }
}
 


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = blog['posts'][post_id]
    return post['title']

if __name__ == '__main__': 
    app.run(debug=True) 