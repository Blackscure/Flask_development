from flask import Flask,render_template, request

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
    post = blog['posts'].get(post_id)
    if not post:
        return render_template('404.html', message=f'A post with id {post_id} was not found.')
    return render_template('post.html',  post=post)



@app.route('/post/create', methods=['GET', 'POST'])
def create():
    if request.method == 'post':
        pass
    return render_template('create.html')


if __name__ == '__main__': 
    app.run(debug=True) 