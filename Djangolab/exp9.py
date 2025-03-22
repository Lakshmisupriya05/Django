from bottle import Bottle, run 
app = Bottle() 
@app.route('/') 
def home_page(): 
    return "Hello I'm Supriya! Welcome to Shri Vishnu Engineering College" 
if __name__ == "__main__": 
    run(app, host='localhost',port=8082)