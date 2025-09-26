# 1. Create project directory and navigate into it
mkdir myproject
cd myproject

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Upgrade pip and install Django
python -m pip install --upgrade pip
pip install django

# 5. Create Django project
django-admin startproject myproject .

# 6. Run the development server
python manage.py runserver
