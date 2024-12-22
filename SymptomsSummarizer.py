import streamlit as st
import openai

openai.api_key = 'Enter OpenAI api key'

def get_diagnosis(symptoms):
    try:
        prompt = f"You are a very experienced doctor. The following symptoms have been reported: {', '.join(symptoms)}. Please provide a possible diagnosis. First give the Diagnosis then give pointers on how to relieve the symptoms at home and then when should we go to the doctors."

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a medical assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )

        diagnosis = response['choices'][0]['message']['content']
        return diagnosis.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Function to get a diagnosis in Nepali
def get_diagnosis_in_nepali(symptoms):
    try:
        prompt = f"You are a very experienced doctor. The following symptoms have been reported: {', '.join(symptoms)}. Please provide a possible detailed diagnosis in Nepali. First give the Diagnosis then give pointers on how to relieve the symptoms at home and then when should we go to the doctors."

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a medical assistant fluent in Nepali."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=900
        )

        diagnosis = response['choices'][0]['message']['content']
        return diagnosis.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Main function for the app
def main():
    st.title('Symptom Checker with AI Assistance')
    st.markdown("""
    This app helps you analyze your symptoms and get potential diagnoses. 
    Select your symptoms below and let the AI assist you in understanding what they might mean.
    """)

    # Define available symptoms
    symptoms_list = [
        "Fever", "Headache", "Chills", "Fatigue", "Dizziness", "Nausea", "Body ache",
        "Sore throat", "Chest pain", "Runny nose", "Loss of taste", "Loss of smell", "Rash",
        "Abdominal pain", "Muscle pain"
    ]

    # Let user select multiple symptoms
    selected_symptoms = st.multiselect(
        "Select your symptoms", symptoms_list, default=[]
    )

    if selected_symptoms:
        col1, col2 = st.columns(2)  # Two buttons side by side
        with col1:
            if st.button('Get Diagnosis in English'):
                st.subheader("Diagnosis or Advice (English):")
                diagnosis = get_diagnosis(selected_symptoms)
                st.write(diagnosis)

        with col2:
            if st.button('Get Diagnosis in Nepali'):
                st.subheader("Diagnosis or Advice (Nepali):")
                nepali_diagnosis = get_diagnosis_in_nepali(selected_symptoms)
                st.write(nepali_diagnosis)
    else:
        st.warning("Please select at least one symptom.")

if __name__ == "__main__":
    main()
