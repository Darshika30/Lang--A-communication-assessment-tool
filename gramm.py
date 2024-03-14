import tkinter as tk
from tkinter import messagebox
import language_tool_python
from PIL import Image, ImageTk

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
        messagebox.showinfo("Grammar Check Result", f"Corrected Text:\n{corrected_text}\nGrammar Score: {score}/100")
    else:
        messagebox.showinfo("Grammar Check Result", "No grammar errors found.\nGrammar Score: 100/100")

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

def on_submit():
    user_input = text_input.get("1.0", "end-1c")
    if user_input.isdigit():
        messagebox.showerror("Error", "Please enter text, not a number.")
    elif user_input:
        check_grammar(user_input)
    else:
        messagebox.showwarning("Warning", "Please enter something.")

def main():
    # Create GUI window
    window = tk.Tk()
    window.title("Grammar Checker")
    window.geometry("600x550")
    window.config(bg="#f0f0f0")

    # Heading
    heading_label = tk.Label(window, text="Describe this Scene", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
    heading_label.pack(pady=10)

    import random

# List of image filenames
    image_filenames = ["img.jpg", "img2.jpg", "img3.jpg", "img4.jpg"]

    # Load and display a random image
    selected_image = random.choice(image_filenames)
    image = Image.open(selected_image)
    image = image.resize((400, 300))
    photo = ImageTk.PhotoImage(image)
    img_label = tk.Label(window, image=photo)
    img_label.image = photo
    img_label.pack(pady=10)

    # Text input area
    global text_input
    text_input = tk.Text(window, height=5, wrap="word", font=("Helvetica", 12))
    text_input.pack(pady=10, padx=10, fill="both", expand=True)

    # Submit button
    submit_button = tk.Button(window, text="Check Grammar", command=on_submit, bg="#4caf50", fg="white", font=("Helvetica", 12, "bold"))
    submit_button.pack(pady=5)

    # Run the GUI application
    window.mainloop()

if __name__ == "__main__":
    main()
