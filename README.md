# StanleyHub

StanleyHub is a learning platform designed to provide courses, articles, and resources for individuals interested in cybersecurity, software engineering, and data science. The platform includes features such as user authentication, course enrollment, and a dynamic learning page.

## Features

- **User Authentication**: Secure login and signup functionality with password hashing.
- **Course Management**: Browse, enroll, and track progress in various courses.
- **Dynamic Learning Page**: Step-by-step learning materials including videos, documents, and text content.
- **GitHub-Inspired Theme**: A clean and modern design with a theme toggle for light and dark modes.
- **Article Library**: Access articles on topics like Zero Trust Security, OWASP Top 10, and more.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/stanlley-locke/stanlleyhub.git
   ```

2. Navigate to the project directory:
   ```bash
   cd stanlleyhub
   ```

3. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Initialize the database:
   ```bash
   python app.py
   ```

## Usage

- Start the Flask development server:
  ```bash
  python app.py
  ```
- Access the application at `http://127.0.0.1:8080`.

## File Structure

- `app.py`: Main application file containing routes and logic.
- `models.py`: Database models for users, courses, and learning materials.
- `templates/`: HTML templates for the frontend.
- `static/`: Static files including CSS, JavaScript, and images.

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.