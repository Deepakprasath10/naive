#  Fake News Detection Web App

A machine learning-based Flask web application that classifies news articles as **Real** or **Fake** using a Naive Bayes Classifier. Users can input custom news text and receive instant predictions.

---


##  Project Structure
```
FakeNewsDetectionApp/
│
├── static/
│ └── style.css # Custom frontend styling
│
├── templates/
│ ├── index.html # Input form page
│ └── result.html # Result output page
│
├── fake_news_model.pkl # Trained Naive Bayes model
├── vectorizer.pkl # TF-IDF vectorizer
├── fake_news.csv # Training dataset (Kaggle)
├── app.py # Main Flask application
├── requirements.txt # Required Python packages
└── README.md # Project documentation
```

## Technologies Used
```
| Layer        | Technology                  |
|--------------|-----------------------------|
| Language     | Python 3                    |
| Backend      | Flask                       |
| ML Algorithm | Multinomial Naive Bayes     |
| NLP          | scikit-learn, NLTK          |
| Frontend     | HTML, CSS                   |
```
---

##  Installation & Setup
 1. Clone this repository
```
git clone https://github.com/your-username/FakeNewsDetectionApp.git
cd FakeNewsDetectionApp
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Run the Flask application
```
python app.py
```
Visit: http://localhost:5000

## How It Works
The user submits a news article through the form.

The app processes the input using a TF-IDF vectorizer.

The trained Naive Bayes model classifies the news as Real or Fake.

The result is shown on a separate page.

## Sample Input & Output
Input: "Government confirms breakthrough in renewable energy."

Output:  Real

Input: "Aliens invade Earth and take over the stock market."

Output:  Fake

## Screenshots
![alt text](<Screenshot 2025-08-02 152906.png>)
![alt text](<Screenshot 2025-08-02 152937.png>)
![alt text](<Screenshot 2025-08-02 152946.png>)