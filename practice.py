import streamlit as st
import language_tool_python
from PIL import Image
import random

def check_grammar(text):
    # Initialize LanguageTool
    tool = language_tool_python.LanguageTool('en-US')

    # Check grammar
    matches = tool.check(text)

    # Parse matches
    if matches:
        # Apply corrections
        corrected_text = apply_corrections(text, matches)

        # Calculate grammar score
        score = calculate_score(text, matches)

        # Show result
        st.success(f"Corrected Text:\n{corrected_text}\nGrammar Score: {score}/100")
    else:
        st.success("No grammar errors found.\nGrammar Score: 100/100")

def apply_corrections(text, matches):
    # Apply corrections to the text based on the matches
    index_offset = 0

    for match in matches:
        offset = match.offset
        length = match.errorLength
        replacements = match.replacements

        # Apply the first replacement option
        replacement = replacements[0]

        # Calculate new index after applying replacement
        corrected_offset = offset + index_offset
        corrected_length = length + len(replacement) - len(text[offset:offset+length])

        # Apply replacement to the text
        text = text[:corrected_offset] + replacement + text[corrected_offset+length:]

        # Update index offset for next replacement
        index_offset += corrected_length - length

    return text

def calculate_score(text, matches):
    # Calculate grammar score based on number of errors
    num_errors = len(matches)
    score = max(0, 100 - num_errors * 10)  # Deduct 10 points for each error, maximum score is 100
    return score

def main():
    st.title("Grammar Checker")

    # Heading
    st.header("Describe this Scene")

    # Load and display a random image
    image_filenames = ["img.jpg", "img2.jpg", "img3.jpg", "img4.jpg"]
    selected_image = random.choice(image_filenames)
    image = Image.open(selected_image)
    st.image(image, caption='Random Image', use_column_width=True)

    # Text input area
    user_input = st.text_area("Enter your text here")

    # Submit button
    if st.button("Check Grammar"):
        if user_input:
            check_grammar(user_input)
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
