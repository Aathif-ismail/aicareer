from google import genai
import streamlit as st

advisor = genai.Client(api_key="AIzaSyAQNUSjLk4pUKXwui4WXALeqD0gcSqpraM")

st.title("AI Career Advisor")

age = st.text_input("Enter your age: ")
qualification = st.text_input("Enter your qualification: ")
designation = st.text_input("Enter your current designation: ")
salary = st.text_input("Enter your current salary: ")
skills = st.text_input("Enter your skills: ")
experience =st.text_input("Enter your years of experience: ")
interest =st.text_input("Enter your area of interest: ")
goal = st.text_input("Enter your career goal: ")
location =st.text_input("Enter your preferred job location: ")
language =st.text_input("Enter your known languages: ")
nationality =st.text_input("Enter your nationality: ")

prompt = f"""
You are an expert career advisor. Based on the following inputs from the user, give your career advice in detail.

Age: {age}
Qualification: {qualification}
Designation: {designation}
Salary: {salary}
Skills: {skills}
Experience: {experience}
Area of Interest: {interest}
Career Goal: {goal}
Preferred Job Location: {location}
Known Languages: {language}
Nationality: {nationality}

keep it simple,precise and to the point,add bullet points for easy refernce

suggest me resourse materials for upskilling
list me certification i should acquire

"""

if st.button("submit"):
    response = advisor.models.generate_content(model="gemini-1.5-flash",
                                               contents=prompt)
    st.write(response.text)
