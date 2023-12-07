# Import necessary libraries
import streamlit as st
from pydantic import BaseModel
from typing import List
from helpers import structured_generator  # Assuming this is a predefined function in the helpers module

# Define the BaseModel class for data validation
class Titles(BaseModel):
    titles: List[str]

# Streamlit code to create the UI
def main():
    # Set up the title and description of the web app
    st.title("Blog Title Generator")
    st.write("Generate blog titles based on a given topic using AI")

    # Input section: User inputs the topic for the blog titles
    user_input = st.text_input("Enter the topic for your blog", "Digital marketing")

    # Button to trigger the title generation
    if st.button("Generate Titles"):
        # Call the structured_generator function with the user input
        prompt = f"generate 5 blog titles for a video about {user_input}"
        openai_model = "gpt-3.5-turbo"
        result = structured_generator(openai_model, prompt, Titles)

        # Display the generated titles
        if result.titles:
            st.subheader("Generated Titles")
            for title in result.titles:
                st.write(title)
        else:
            st.write("No titles were generated. Try a different topic.")

# Protect the script to run only when it's the main module
if __name__ == "__main__":
    main()
