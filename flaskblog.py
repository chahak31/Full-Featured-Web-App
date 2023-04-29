from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'author':'Corey Schafer',
        'title':'Blog Post 1',
        'content':'First Post Content',
        'date_posted':'April 17, 2023'
    },
        {
        'author':'Jane Doe',
        'title':'Blog Post 2',
        'content':'Second Post Content',
        'date_posted':'April 18, 2023'
    }
]


@app.route("/")
def hello():
    return render_template('home.html', posts_var=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = login()
    return render_template('login.html',title='login',form=form)

if __name__ == '__main__':
    app.run(debug=True)