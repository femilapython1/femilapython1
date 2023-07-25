from flask import Flask

new = Flask(__name__)


@new.route('/profile/<int:id>')
def profile(id):
    return '<h1> This profile is for %d</h1>' % id


new.run()
