# Heart Failure Mortality Prediction App

**A web application to predict the risk of heart failure mortality using a trained Artificial Neural Network (ANN) model. Built with Python, TensorFlow, and Streamlit.**

---

## **Features**

* Predicts the risk of heart failure mortality based on patient clinical features.
* User-friendly web interface built with **Streamlit**.
* Displays risk probability clearly with success or warning messages.
* Fully deployable on **Streamlit Cloud**.

---

## **Model Details**

* Model Type: Artificial Neural Network (ANN)
* Framework: TensorFlow 2.15, Keras 2.15
* Input Features: 12 clinical parameters (e.g., Age, CPK, Ejection Fraction, Serum Creatinine, Serum Sodium, etc.)
* Output: Probability of heart failure mortality (0 = low risk, 1 = high risk)

---

## **Installation**

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/heart-failure-mortality-prediction.git
cd heart-failure-mortality-prediction
```

2. Create and activate a virtual environment (Python 3.10 recommended):

```bash
# Windows (PowerShell)
python -m venv tf_215_env
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\tf_215_env\Scripts\Activate.ps1

# Mac/Linux
python3.10 -m venv tf_215_env
source tf_215_env/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app locally:

```bash
streamlit run app.py
```

---

## **Usage**

1. Enter patient clinical parameters in the sidebar.
2. Click **Predict**.
3. View the predicted risk of heart failure mortality.

---



## **Requirements**

* Python 3.10
* streamlit==1.27.0
* tensorflow-cpu==2.15.0
* keras==2.15.0
* numpy, pandas, scikit-learn, protobuf, ml-dtypes, tensorboard

*(See `requirements.txt` for full details)*


## **Author**

Shazia Afraz
