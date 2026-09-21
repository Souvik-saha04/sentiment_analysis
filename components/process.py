import joblib
from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent
model=joblib.load(BASE_DIR/"LogisticModel.pkl")
vectorizer=joblib.load(BASE_DIR/"vectorizer.pkl")
def process(text):
    print("vectorizing the text..")
    vectext=vectorizer.transform([text])
    print("predicting the sentiment..")
    result=model.predict(vectext)
    if(result==1):
        return "Positive"
    elif result==0:
        return "Neutral"
    else:
        return "Negetive"

