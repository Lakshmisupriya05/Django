from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello():
    return "Hello! This is Supriya. My regdno:23B01A12I1"
if __name__=='__main__':
    app.run()