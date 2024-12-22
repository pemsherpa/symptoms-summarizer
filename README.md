**Symptom Checker with AI Assistance 🌡️🩺**

This project is a Symptom Checker application powered by OpenAI’s GPT-4 model. It helps users analyze their symptoms and provides potential diagnoses, including home remedies and guidance on when to consult a doctor. The app supports English and Nepali for diagnosis.

Features 🚀

	•	AI-Powered Diagnoses: Provides detailed medical advice based on selected symptoms.
	•	Dual Language Support:
	•	English
	•	Nepali
	•	User-Friendly Interface: Simple and intuitive interface built with Streamlit.
	•	Multiple Symptom Selection: Allows users to select multiple symptoms simultaneously.
	•	Actionable Advice: Offers home remedies and guidance on seeking professional medical help.

Installation 🛠️

Prerequisites

	•	Python 3.7+
	•	An OpenAI API key
	•	Streamlit installed

Steps

	1.	Clone the repository:

git clone https://github.com/your-username/symptom-checker-ai.git
cd symptom-checker-ai


	2.	Set up a virtual environment:

python -m venv venv
source venv/bin/activate   # For Mac/Linux
venv\Scripts\activate      # For Windows


	3.	Install dependencies:

pip install -r requirements.txt


	4.	Add your OpenAI API key:
Replace Enter OpenAI api key in the code with your actual OpenAI API key.
	5.	Run the app:

streamlit run app.py


	6.	Open your browser and go to http://localhost:8501.

How to Use 🖥️

	1.	Select your symptoms from the available list.
	2.	Choose one of the following:
	•	Get Diagnosis in English
	•	Get Diagnosis in Nepali
	3.	View detailed diagnoses with actionable advice.

Project Structure 📂

symptom-checker-ai/
│
├── app.py                     # Main application file
├── requirements.txt           # List of Python dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore file

Example Output 🎯

English Diagnosis:

	Diagnosis: You may have a mild viral infection.
Home Remedies: Drink plenty of fluids, rest, and take over-the-counter medications if needed.
When to See a Doctor: Consult a doctor if symptoms worsen or persist for more than three days.

Nepali Diagnosis:

	निदान: तपाईँलाई साधारण भाइरल संक्रमण हुनसक्छ।
घरमै गर्न सकिने उपायहरू: धेरै पानी पिउनुहोस्, आराम गर्नुहोस्, र आवश्यक भएमा औषधि लिनुहोस्।
डाक्टरलाई कहिले देखाउनु पर्ने: यदि लक्षणहरू तीन दिनभन्दा बढी रहन्छ वा गम्भीर हुन्छ भने डाक्टरलाई भेट्नुहोस्।

Technologies Used 🧰

	•	Python: Programming language
	•	Streamlit: Framework for the web interface
	•	OpenAI GPT-4: Backend AI for generating diagnoses

Contributing 🤝

Contributions are welcome! Please follow these steps:
	1.	Fork the repository.
	2.	Create a feature branch:

git checkout -b feature-name


	3.	Commit your changes:

git commit -m "Add your message"


	4.	Push to the branch:

git push origin feature-name


	5.	Open a pull request.

License 📄

This project is licensed under the MIT License. See the LICENSE file for details.

Contact 📧

If you have any questions or feedback, feel free to reach out at your-email@example.com.

Acknowledgments 🙏

	•	OpenAI for the amazing GPT-4 API.
	•	Streamlit for the user-friendly framework.
	•	Everyone who supports open-source projects.

Enjoy using the Symptom Checker! 😊
