from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    greeting="world"
    return f'hello{greeting}!'
if __name__ == "__main__":
    app.run()
