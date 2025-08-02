from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_text = request.form['news']
    vec_text = vectorizer.transform([input_text])
    prediction = model.predict(vec_text)[0]
    result = "✅ Real News" if prediction == 1 else "🚨 Fake News"
    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
