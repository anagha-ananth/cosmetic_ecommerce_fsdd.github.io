# AA Shops - E-commerce Web Application

  AA Shops is a simple e-commerce web application built using Django. It allows users to browse products, add items to a shopping cart, create wishlists, and proceed to checkout. After placing an order, users receive an order confirmation with a summary of their purchase.

## Features

- **Home Page**: Displays a list of available products with their details.
- **Product Details Page**: Shows a detailed view of each product, including name, description, price, and stock.
- **Add to Cart**: Allows users to add products to their cart.
- **Wishlist**: Users can save products to their wishlist for future reference.
- **Cart Management**: View, update, or remove items from the shopping cart.
- **Checkout**: View order details and confirm the purchase (payment excluded in this version).
- **Order Confirmation**: Displays a summary of the order and the total price.
- **User Authentication**: Includes user registration, login, and logout functionality.

## Technologies Used

- **Frontend**: HTML, CSS, Bootstrap (for styling).
- **Backend**: Django (Python-based web framework).
- **Database**: SQLite (default database for Django).

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)
  
## Usage

1. **Homepage**: Browse available products.
2. **Authentication**: Sign up or log in to access features like adding items to the cart or wishlist.
3. **Cart and Wishlist**: Add products, view items, and manage your cart or wishlist.
4. **Checkout**: Confirm your order and view the order summary on the confirmation page.

## Project Structure

- **cos_app**: Main application folder.
  - `models.py`: Database models for products, cart, wishlist, and orders.
  - `views.py`: Handles the logic for each route.
  - `urls.py`: Defines the URL patterns for the application.
  - `templates/`: Contains all HTML templates for rendering pages.
- **static/**: Contains static assets like CSS and images.
- **db.sqlite3**: SQLite database file.

## Future Enhancements

- Add payment gateway integration for processing payments.
- Implement search and filtering functionality for products.
- Add order history for users.
- Improve UI/UX with more styling and animations.
