# 📚 Book Library API

A modular and lightweight REST API for managing a book library, built using **FastAPI**.

## 🚀 Features

- View a list of available books
- Add new books to the library
- Fetch book details by ID
- Modular code structure for easy scaling
- FastAPI with Uvicorn for high performance

---

## 📁 Project Structure
Book_library/
│
├── app/
│ ├── main.py # Entry point
│ ├── routes/
│ │ └── book_routes.py # API routes
│ ├── data/
│ │ └── book_data.py # In-memory book data
│ └── init.py
│
├── venv/ # Virtual environment
├── requirements.txt
├── .gitignore
└── README.md
