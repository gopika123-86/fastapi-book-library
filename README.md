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
└── README.md

Description of Endpoints used
GET /books
This endpoint retrieves a list of all books in the library.
Description: Fetches all available books.
Method: GET
Response: A JSON array of book objects.
Example Response:

JSON

[
  {
    "id": 1,
    "title": "The Hitchhiker's Guide to the Galaxy",
    "author": "Douglas Adams"
  },
  {
    "id": 2,
    "title": "1984",
    "author": "George Orwell"
  }
]
GET /books/{book_id}
This endpoint fetches a single book by its ID.
Description: Retrieves a specific book using its unique ID.
Method: GET
URL Parameters:
book_id (integer): The ID of the book to retrieve.
Response: A JSON object of the requested book.

Error Responses:
404 Not Found: Returned if no book with the specified book_id exists.

POST /books
This endpoint adds a new book to the library.
Description: Creates a new book entry.
Method: POST
Request Body: A JSON object representing the new book.
Response: The JSON object of the newly created book.
Error Responses:

400 Bad Request: Returned if a book with the same ID already exists.

PUT /books/{book_id}
This endpoint updates an existing book.
Description: Replaces a book with new data based on its ID.
Method: PUT
URL Parameters:
book_id (integer): The ID of the book to update.
Request Body: A JSON object with the new book data.
Response: The JSON object of the updated book.
Error Responses:

404 Not Found: Returned if the book to be updated does not exist.

DELETE /books/{book_id}
This endpoint deletes a book from the library.
Description: Removes a book entry using its ID.
Method: DELETE
URL Parameters:
book_id (integer): The ID of the book to delete.
Response: A JSON message confirming the deletion.
Error Responses:

404 Not Found: Returned if the book to be deleted does not exist.
