# Vacation Homes and Rentals Application

## Overview
This project is an end-to-end application designed to manage vacation home rentals and sales. The application provides the following features:

1. **User Authentication**: Login, registration, and logout.
2. **Property Management**: Viewing, listing, and recommendations for properties.
3. **AI-Driven Recommendations**: Personalized property suggestions based on user preferences.
4. **Checkout and Profile Management**: Buying/renting properties and managing user profiles.
5. **Responsive Design**: Optimized for both desktop and mobile devices.

## Technology Stack
- **Frontend**: HTML, CSS, Bootstrap, JavaScript.
- **Backend**:
  - Java (Spring Boot): User and property management APIs.
  - Python (Flask with TensorFlow): AI recommendation system.
- **Database**: PostgreSQL.

## Features
### 1. Login/Register Page
- Users can register an account or log in using their credentials.
- Authentication data is stored securely in the database.

### 2. Property Listings and Recommendations
- Users can view properties available for rent or purchase.
- AI-driven recommendations suggest properties based on preferences.

### 3. Profile and Checkout Page
- Users can view and manage their profiles.
- Checkout allows users to finalize property rentals or purchases.

## Installation and Usage

### Prerequisites
- PostgreSQL database installed and running.
- Java 17+ installed.
- Python 3.8+ installed.
- Node.js and npm for managing frontend dependencies (optional for advanced customization).

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repository/vacation-homes.git
   cd vacation-homes
   ```

2. **Database Setup**:
   - Execute the SQL scripts in `database_tables.sql` to create and populate the database.

3. **Backend Setup**:
   - **Java**:
     - Navigate to the `backend/java` directory.
     - Build the Spring Boot application:
       ```bash
       ./mvnw spring-boot:run

       ./gradlew bootRun
       ```
     - Access APIs at `http://localhost:8080/api`.
   - **Python**:
     - Navigate to the `backend/python` directory.
     - Install dependencies:
       ```bash
       pip install -r requirements.txt
       ```
     - Run the Flask application:
       ```bash
       python app.py
       ```
     - Access recommendations at `http://localhost:5000/recommend`.

4. **Frontend Setup**:
   - Open the HTML files in the `frontend` directory in a browser.

### Usage
- Visit the login page to create an account or log in.
- Browse the property listing page to view available properties.
- Check out personalized recommendations based on preferences.
- Finalize rentals or purchases on the checkout page.

## Project Structure
```
vacation-homes/
├── backend/
│   ├── java/          # Spring Boot backend
│   └── python/        # Flask AI model
├── database/          # SQL scripts
├── frontend/          # HTML, CSS, JavaScript files
└── README.md          # Documentation
```

## Screenshots
1. **Login/Register Page**:  
   ![Login Page]![image](https://github.com/user-attachments/assets/cd4d5555-1d6e-4e00-bd4a-d336c9a83bcf)
   ![Register Page]![image](https://github.com/user-attachments/assets/28cdb161-68dc-4628-8fe4-22e4b632d924)

2. **Resgistered_user Database**:  
   ![image](https://github.com/user-attachments/assets/83cc3567-1b37-4835-a79f-3037c0f1578b)

3. **Property Listings**:  
   ![Listings]![image](https://github.com/user-attachments/assets/cf424fc1-a0b6-4d07-b8c6-edd5fad8877e)

4. **Recommendations**:  
   ![Recommendations]![image](https://github.com/user-attachments/assets/65aa3d70-274e-4f97-8897-407fd32ff410)


## Deployment
- Host the frontend on GitHub Pages or a similar service.

## Future Enhancements
- Add admin panel for managing properties.
- Include advanced filters for property search.
- Integrate payment gateway for seamless transactions.



