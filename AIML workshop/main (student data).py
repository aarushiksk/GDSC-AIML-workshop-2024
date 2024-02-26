import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('linear_regression_model.pkl')

# Define the DataFrame
df = pd.DataFrame(columns=['age', 'Medu', 'Fedu', 'G1', 'G2', 'sex_F', 'sex_M', 'address_R', 'address_U'])

def main():
    st.title("Student Performance Predictor")
    st.write("Enter student details:")

    # Age input
    age = st.number_input("Age", min_value=15, max_value=22, value=18, step=1)

    # Mother's education input
    medu = st.selectbox("Mother's Education", options=[0, 1, 2, 3, 4], index=2)

    # Father's education input
    fedu = st.selectbox("Father's Education", options=[0, 1, 2, 3, 4], index=2)

    # First period grade input
    g1 = st.number_input("First Period Grade", min_value=0, max_value=20, value=10, step=1)

    # Second period grade input
    g2 = st.number_input("Second Period Grade", min_value=0, max_value=20, value=10, step=1)

    # Gender input
    sex = st.selectbox("Gender", options=["M", "F"])

    # Address input
    address = st.selectbox("Address", options=["Urban", "Rural"])

    # Button to submit inputs
    if st.button("Predict"):
        # Create a dictionary with the input values
        input_dict = {'age': age, 'Medu': medu, 'Fedu': fedu, 'G1': g1, 'G2': g2,
                      'sex_F': 1 if sex == 'F' else 0, 'sex_M': 1 if sex == 'M' else 0,
                      'address_R': 1 if address == 'Rural' else 0, 'address_U': 1 if address == 'Urban' else 0}
        
        # Add the dictionary as a new row to the DataFrame
        df.loc[0] = input_dict
        
        # Perform prediction
        prediction = model.predict(df[['age', 'Medu', 'Fedu', 'G1', 'G2', 'sex_F', 'sex_M', 'address_R', 'address_U']])
        
        # Display the prediction
        st.success(f"Predicted G3: {prediction[0]}")

if __name__ == "__main__":
    main()
