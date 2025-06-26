# Online Bookstore Management System

A Flask-based web application for bookstore inventory, customer, and order management, developed as a database course project at Beijing University of Technology.

## Key Features
- 📚 Book management (CRUD operations)
- 👥 Customer management with purchase history
- 💳 Order processing with payment/shipping tracking
- 📊 Sales statistics and reporting
- 📈 Dashboard with key performance metrics

Tech Stack
- Backend: Python/Flask
- Database: MySQL (Cloud-hosted)
- Frontend: HTML/CSS/JavaScript
- ORM: SQLAlchemy
- Templates: Jinja2

Database Schema
```mermaid
erDiagram
    book_info ||--o{ purchase_method : "1-N"
    buyer_info ||--o{ purchase_method : "1-N"
    book_info {
        INT book_id PK
        VARCHAR(50) book_category
        VARCHAR(100) book_name
        DECIMAL(10,2) price
        TEXT introduction
    }
    buyer_info {
        INT purchase_id PK
        VARCHAR(50) name
        ENUM('Male','Female','Other') gender
        INT age
        VARCHAR(100) contact
    }
    purchase_method {
        INT method_id PK
        INT purchase_id FK
        INT book_id FK
        VARCHAR(50) payment_method
        VARCHAR(50) delivery_method
    }
