import connexion

# this is Flask app from connexion
app = connexion.App(__name__).app

# this is connexion app
app = connexion.App(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
