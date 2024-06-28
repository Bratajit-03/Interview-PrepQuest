import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def get_interview_questions(domain,interviewer_type):
    prompt= (f"""
    You are an experienced interviewer specializing in conducting '{interviewer_type}' for candidates in the domain of '{domain}'. Your task is to generate a comprehensive list of the most commonly and frequently asked interview questions along with their answers for the '{interviewer_type}' round in the domain of '{domain}'.Please ensure the answers are clear, precise, and to the point, providing not only the correct answer but also the reasoning behind it. Your goal is to create a valuable resource for someone preparing for a '{interviewer_type}' interview in the '{domain}' domain.
    """)

    response = model.generate_content(prompt)
    return response.text

st.markdown(
    """
    <style>
        .navbar {
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #8EE4AF;
            padding: 20px;
            margin-bottom: 20px;
        }
        .navbar-title {
            font-size: 35px; 
            font-weight: bold;
            margin-right: 10px;
        }
        .navbar-logo {
            height: 40px;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 14px;
            color: #666;
        }
    </style>
    
    <div class="navbar">
        <div class="navbar-title">Interview PrepQuest📄</div>
    </div>
    """, unsafe_allow_html=True
)

domain = st.text_input("Enter your preferred Domain (e.g.- Data Science, Web Development):")
interviewer_type = st.selectbox("Select Interviewer Type:", ["Select from dropdown", "HR Interview", "Technical Interview", "Managerial Interview"])



if st.button("Generate"):
    if domain and interviewer_type != "Select from dropdown":
        with st.spinner('Generating Interview Questions & Answers'):
            qa_text = get_interview_questions(domain,interviewer_type)
            st.write(qa_text)
    else:
        st.error("Please enter a domain and select an interviewer type.")

st.markdown(
    """
    <div class="footer">
        Created and Designed by BRATAJIT DAS | &copy 2024 All Rights Reserved
    </div>
    """, unsafe_allow_html=True
)
