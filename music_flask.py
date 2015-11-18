import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    return flask.render_template("layout.html", page_to_insert="news.html")


@app.route('/news')
def about():
    return flask.render_template("layout.html", page_to_insert="news.html")


@app.route('/about')
def about():
    return flask.render_template("layout.html", page_to_insert="about.html")


@app.route('/music')
def resume():
    return flask.render_template("layout.html", page_to_insert="music.html")


@app.route('/events')
def resume():
    return flask.render_template("layout.html", page_to_insert="events.html")


@app.route('/contact')
def resume():
    return flask.render_template("layout.html", page_to_insert="contact.html")


if __name__ == '__main__':
    app.run(debug=True)
