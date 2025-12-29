# Import necessary libraries
import os
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import streamlit as st

# Set up Google Generative AI API key
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model=genai.GenerativeModel('gemini-2.0-flash')


# Streamlit app setup
st.title("YouTube Video Summarizer")
video_url=st.text_input("Enter the video link")

# Function to extract video ID from URL
def vid(video_url):
    video_id="dyeYA7l3t-Y"
    return video_id

# Function to get transcript from YouTube video
def get_transcript(video_url):
    video_id=vid(video_url)
    yt_obj=YouTubeTranscriptApi()
    transcript=yt_obj.fetch(video_id)
    return transcript

# Button to generate summary
if st.button("Get Summary"):
    transcript=get_transcript(video_url)
    prompt= f"let you are a content summarizer.you have to summarize the following content in maximum of 200 words. content: {transcript}"
    response=model.generate_content(prompt)
    st.success("summary generated successfully = {}".format(response.text))
