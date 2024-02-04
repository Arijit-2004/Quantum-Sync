from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__, static_folder='./static')

# Load your machine learning model
model = pickle.load(open('final_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/devs')
# def devs():
#     return render_template('.html')

@app.route('/faqs')
def faqs():
    return render_template('faq.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/predict', methods=['GET'])
def predict_get():
    return render_template('prediction.html')   

@app.route('/predict', methods=['POST'])
def predict():
    request_data = request.get_json()
    # Retrieve data from the form
    transactionType = request_data['transactionType']   
    step = float(request_data['step'])
    amount = float(request_data['actualAmount'])
    amount_received = float(request_data['amountReceived'])
    amount_paid= float(request_data['amountPaid'])
   #  sender_details = request_data['sender']
   #  receiver_details = request_data['receiver']
    
    # Make the prediction using your model
    mapped=0
    if(transactionType.lower() == "cash-out"):
       mapped=1
        #transfer->4 
    #payment->3
    #cash out->1 
    elif(transactionType.lower() =="payment"):
       mapped=3
    elif(transactionType.lower() =="cash-in"):
       mapped=0
    elif(transactionType.lower() =="transfer"):
       mapped=4
    elif(transactionType.lower()== "debit"):
       mapped=2
    prediction = model.predict([[step, mapped, amount, amount_paid, amount_received]])

    # Display the result
    result = "Fraudulent" if prediction == 1 else "Not Fraudulent"
    print(result)
    return {'result': result}

if __name__ == '__main__':
    try:
     app.config['TEMPLATES_AUTO_RELOAD'] = True
     app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
     app.run(debug=False)
    except:
      print("occured error")
