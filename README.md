# Text-to-Speech Converter

## Introduction

This Python script reads a text file, performs text replacement using regular expressions (regex), and then uses the `pyttsx3` library to convert each chapter into separate MP3 files. The program is designed to enhance the accessibility of textual content by converting it into audio files.

## Prerequisites

1. **Python:** Ensure that you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **pyttsx3 Library:** Install the `pyttsx3` library by running the following command:

    ```bash
    pip install pyttsx3
    ```

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd your-repo
    ```

3. **Open the script file, `text_to_speech.py`, in your preferred text editor.**

4. **Customize the input file and replacement dictionary:**

5. **Run the script:**

    ```bash
    python text_to_speech.py
    ```

## Customization

- **Replacement Dictionary (`rep`):** Modify the `rep` dictionary to include the desired text replacements. This dictionary maps original text to the replacement text.

- **Regex Patterns (`regexy`):** Adjust the `regexy` dictionary to add or modify regular expressions for more complex text manipulations.

- **Output File Naming:** Customize the output file naming in the loop where MP3 files are generated. Currently, each file is named as "rozdzialX.mp3."

## Notes

- The script utilizes threading (currently commented out) for potential parallelization of the text-to-speech conversion process. Uncomment the relevant lines in the code if desired.

- The script assumes a specific structure for chapter separation in the input text file. Adjust the regular expression in the `re.split` function based on your file's structure.
