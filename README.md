# Library Management System - Project Documentation

## Overview
This project is a **Windows-based Library Management System** developed using **Python** with a relational database backend. It provides a complete solution for managing library operations including member registration, book cataloging, borrowing/returning processes, and staff management.

## Key Features

### 1. Database Design
- Built on **Microsoft SQL Server** with a normalized relational structure
- Core tables: 
  - `Book` (stores book metadata with ISBN as primary key)
  - `Member` (manages library members with national ID as unique identifier) 
  - `Borrow` (tracks lending transactions with foreign key relationships)
  - `Staff` (handles employee records)

### 2. User Interface
- Developed with **Python's Tkinter** for Windows compatibility
- Responsive GUI with modern widget layouts:
  - Treeview components for tabular data display
  - Modal dialog windows for focused interactions
  - Centralized frame-based design

### 3. Functional Modules

#### Staff Portal
- Authentication system with secure login
- Comprehensive management interfaces for:
  - Book inventory (add/edit/remove)
  - Member administration
  - Borrowing oversight
- Real-time status monitoring

#### Member Portal
- Self-service account authentication
- Interactive features:
  - Available book browsing with filters
  - Borrowing request submission
  - Book return processing
- Account management tools

### 4. Technical Implementation
- **Backend**: 
  - SQL Server for data persistence
  - PyODBC for database connectivity
  - Transactional SQL operations

- **Frontend**:
  - Object-oriented Tkinter implementation
  - Multi-window navigation
  - Form validation and error handling

### 5. System Characteristics
- **Platform**: Windows (compatible with SQL Server environments)
- **Development Tools**:
  - VS Code/PyCharm as primary IDEs
  - SQL Server Management Studio for database administration
- **Architecture**: Client-server model with local DB connection

## Project Scope
This system was developed as an academic project fulfilling all standard requirements for library management software while demonstrating:
- Proper database design principles
- Effective Python application development
- User-centric interface design
- Secure data handling practices

The implementation showcases how Python can be effectively used to build functional Windows applications with database integration.
