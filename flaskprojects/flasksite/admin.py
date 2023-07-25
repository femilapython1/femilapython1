from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html',username=username,isActive=True)

@app.route('/names')
def names():
    names=['Muhammad','Femila','Muad','Imad','Miqdaad']
    return render_template('name.html',names=names)

@app.route('/books')
def books():
    books=[{'name':'book1','auth':'fem','cover':'https://img.freepik.com/free-vector/abstract-elegant-winter-book-cover_23-2148798745.jpg?w=740&t=st=1686553910~exp=1686554510~hmac=a82d8c12493241a9c98ccad1a6bae9dc6a039eb4ae4b30bf48bb565be1a11f5e.png'},{'name':'book2','auth':'sam','cover':'https://img.freepik.com/free-vector/abstract-elegant-winter-book-cover_23-2148798745.jpg?w=740&t=st=1686553910~exp=1686554510~hmac=a82d8c12493241a9c98ccad1a6bae9dc6a039eb4ae4b30bf48bb565be1a11f5e.png' },{'name':'book3','auth':'pam','cover':'https://img.freepik.com/free-vector/abstract-elegant-winter-book-cover_23-2148798745.jpg?w=740&t=st=1686553910~exp=1686554510~hmac=a82d8c12493241a9c98ccad1a6bae9dc6a039eb4ae4b30bf48bb565be1a11f5e.png'}]
    return render_template('book.html',books=books)
app.run(debug=True)
