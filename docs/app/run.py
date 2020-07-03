import flask


app = flask.Flask(__name__)

# Comment out to cache pages
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/', defaults={'filename': 'index.html'})
@app.route('/<path:filename>')
def documentation(filename):
    return flask.send_from_directory(
        "../build/html", filename
    )


if __name__ == "__main__":
    app.run(port=8888)
