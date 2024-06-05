# Password Strength Checker GUI Application

This application allows users to check the strength of their passwords using a graphical user interface. Additionally, it features light/dark mode and password visibility toggles.

## Features
- Check password strength
- Toggle password visibility (hide/show)
- Toggle between light and dark modes

## Requirements
- Python 3.x
- `customtkinter`
- `Pillow`

## Installation and Running the Code

### For Developers:

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/aisaac498/PRODIGY_CS_02.git
    ```

2. **Create and Activate a Virtual Environment**:
    ```sh
    python -m venv pwstr
    source pwstr-virtual/bin/activate  # On Windows, use `pwstr-virtual\Scripts\activate`
    ```

3. **Install the Required Packages**:
    ```sh
    pip install customtkinter Pillow
    ```

4. **Run the Application**:
    ```sh
    python password_strength.py
    ```

### For Prodigy Reviewers:

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/aisaac498/PRODIGY_CS_02.git
    ```

2. **Create and Activate a Virtual Environment**:
    ```sh
    python -m venv pwstr
    source pwstr-virtual/bin/activate  # On Windows, use `pwstr-virtual\Scripts\activate`
    ```

3. **Install the Required Packages**:
    ```sh
    pip install customtkinter Pillow
    ```

4. **Run the Application**:
    ```sh
    python password_strength.py
    ```

## Usage
- Enter your password in the text field.
- Click "Check Password Strength" to see the strength of your password.
- Use the eye icon next to the text field to toggle password visibility (hide/show).
- Use the moon/sun icon at the top right to switch between light and dark modes.

## Developer Notes
- This application was developed for cross-platform compatibility but primarily tested on Windows machines.
- Ensure that all required images (`sun.png`, `moon.png`, `show.png`, `hide.png`) are present in the `Images` directory.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
