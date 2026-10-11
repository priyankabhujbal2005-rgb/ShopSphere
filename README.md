# ShopSphere –
# ShopSphere – Django E-Commerce Website

## About the Project

ShopSphere is a web-based e-commerce application developed using Python and Django. It allows users to browse products, view product details, add items to a shopping cart, and create an account or log in.

## Features

* Home page with product listings
* Product detail page
* Add products to the shopping cart
* Cart management
* User registration and login
* Django admin panel for managing products
* Database integration using SQLite

## Technologies Used

* **Frontend:** HTML, CSS
* **Backend:** Python, Django
* **Database:** SQLite
* **Tools:** Visual Studio Code or any text editor, web browser

## Project Structure

```text
ShopSphere/
├── accounts/
├── config/
├── shop/
├── templates/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/ShopSphere.git
cd ShopSphere
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment (Windows)

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install django pillow
```

If a `requirements.txt` file is provided, use:

```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Start the Development Server

```bash
python manage.py runserver
```

Open the following URL in your browser:

http://127.0.0.1:8000/

## Admin Panel

To create an administrator account, run:

```bash
python manage.py createsuperuser
```

Then open:

http://127.0.0.1:8000/admin/

## Important Notes

* The local SQLite database (`db.sqlite3`) is not included in the repository. Run migrations to create a new database.
* Create a new administrator account on your computer if required.
* Keep secret keys and passwords private.
* `DEBUG = True` should only be used for local development, not production deployment.

## Future Improvements

* Product search and filtering
* Online payment integration
* Order history and tracking
* Product reviews and ratings
* Responsive design improvements

## Author

Developed as a learning project to practice Django web development and e-commerce functionality.
