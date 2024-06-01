from flask import Flask,render_template,request, jsonify
import joblib

# Load the saved model
loaded_model = joblib.load("model.pkl")
totalmark1=0
totalmark2=0
temp = 0

app = Flask(__name__)

def testmodel(totalmark1, totalmark2):
    return loaded_model.predict([[0,totalmark1,totalmark2]])

    
@app.route('/')
def index():
    if temp==0:
     return render_template('index.html',result=0)
    elif temp==1:
        return render_template('index.html',result=1)
    else:
        return render_template('index.html',result=testmodel(totalmark1,totalmark2))


@app.route('/question')
def question():
     return render_template('question.html')
@app.route('/question2')
def question2():
     
     return render_template('question2.html')
 
@app.route('/submit_mark1', methods=['POST'])
def submit_mark1():
    global temp
    global totalmark1
    data = request.get_json()
    temp=0
    totalmark1= data['marks']
    # Do something with total_marks, like storing it in a database
    print("test1:-")
    print(totalmark1)
    temp=temp+1
    print(temp)
    return jsonify({'success': True, 'marks': totalmark1,'redirect': '/'})

@app.route('/submit_mark2', methods=['POST'])
def submit_mark2():
    global temp
    global totalmark2
    data = request.get_json()
    totalmark2= data['marks']
    # Do something with total_marks, like storing it in a database
    print("test2:-")
    print(totalmark2)
    temp=temp+1
    print(temp)
    return jsonify({'success': True, 'marks': totalmark2})

if __name__ == '__main__':
    app.run(debug=True)