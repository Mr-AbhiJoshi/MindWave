# MindWave 🧠

**MindWave** is my inaugural project utilizing the Django framework. This web application serves as a foundational step into full-stack development, integrating Django for backend operations and HTML for frontend presentation. The project showcases essential web development concepts, including template rendering, static file management, and basic routing.

---

## 🚀 Features

- **Django Integration**: Leveraged Django's MTV (Model-Template-View) architecture for structured development.
- **Template Rendering**: Implemented dynamic HTML templates to display content.
- **Static Files Management**: Organized and served static assets like CSS and images.
- **Basic Routing**: Established URL patterns to navigate between different views.

---

## 🛠️ Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML
- **Database**: SQLite
- **Version Control**: Git

---

## 📁 Project Structure

MindWave/
├── home/ # Django app containing views and URLs
├── static/ # Static files (CSS, images)
├── templates/ # HTML templates
├── db.sqlite3 # SQLite database
├── manage.py # Django management script
└── .gitignore # Git ignore file

## 📸 Screenshots

*Include relevant screenshots here to showcase the UI and features.*

---

## 📌 Installation

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

git clone https://github.com/Mr-AbhiJoshi/MindWave.git
cd MindWave

### 2. Create a Virtual Environment

python -m venv env

### 3. Activate the environment

#### a. On macOS/Linux:

source env/bin/activate

#### b. On Windows:

.\env\Scripts\activate

### 4. Install Dependencies

pip install -r requirements.txt

#### Note: 
If requirements.txt is not present, install Django manually:

pip install django

### 5. Apply Migrations

python manage.py migrate

### 6. Run the Development Server

python manage.py runserver

Access the application at: http://127.0.0.1:8000/

## 🧑‍💻 Author

Abhishek Joshi
Aspiring Software Engineer | Full-Stack Developer

📍 Wollongong, New South Wales, Australia

📧 abhijoshi1441@gmail.com