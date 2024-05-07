# Vendor Management System API Documentation
[(Postman Collection)](https://www.postman.com/galactic-water-179159/workspace/public-workspace/collection/23389473-ef942ca9-461b-4150-856e-1647296cb171?action=share&creator=23389473)
## Cloning and Setting Up the Django Application

## Getting Started
To get started with the VMS API, follow the instructions below:
1. Clone the repository.
2. Install the required dependencies.
3. Set up your environment variables.
4. Run the server.


### 1. Clone the Repository
To get started, clone the repository to your local machine. Open your terminal and execute the following command:

```bash
git clone https://github.com/Dr-blue-cyber/vms.git
```

### 2. Set Up a Virtual Environment
Navigate into the project directory and create a virtual environment. Use the following commands:

```bash
cd vms
python -m venv myenv  # Create a virtual environment named 'myenv'
```
### Activate the Virtual Environment
* Windows:
```bash
.\myenv\Scripts\activate
```
* Unix/MacOS:
```bash
source myenv/bin/activate
```
### 3. Install Dependencies
While inside the activated virtual environment, install all the required modules using pip:

```bash
pip install <module_name>  # pip install django
```

## Running the Django Application

### 1. Activate the Virtual Environment (if not already activated)
 If you've closed your terminal or deactivated the virtual environment, reactivate it using the appropriate command based on your operating system.
### 2. Start the Django Server
 In the project directory, run the following command to start the Django development server:
```bash
python manage.py runserver
```

If successful, you'll see output indicating that the server is running, usually on http://127.0.0.1:8000/.


### 3. Accessing the APIs
With the server running, you can now access the APIs provided by your Django application. Open your web browser and go to http://127.0.0.1:8000/ or http://localhost:8000/.

## Deactivating the Virtual Environment
### 1. Deactivate the Virtual Environment
Once you're done working with the application, you can deactivate the virtual environment using the following command:
```bash
deactivate
```

## Additional Notes
### Troubleshooting ModuleNotFoundError
If you encounter a ModuleNotFoundError when running the Django server, make sure to install all the required modules using ```pip install <module_name>``` as mentioned in the documentation.

### Changing Execution Policy (Windows)
If you encounter an execution policy error on Windows, run the following command to change the execution policy for the current session:
```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
Then, reactivate the virtual environment as mentioned earlier.


## Core Features

### 1. Vendor Profile Management (to used the APIs you must pass the x-api-key in headers)

#### Model Design
The model stores vendor information including name, contact details, address, and a unique vendor code.

#### API Endpoints [(Postman Collection)](https://www.postman.com/galactic-water-179159/workspace/public-workspace/collection/23389473-ef942ca9-461b-4150-856e-1647296cb171?action=share&creator=23389473)
- **POST /api/vendors/**: Create a new vendor.
- **GET /api/vendors/**: List all vendors.
- **GET /api/vendors/{vendor_id}/**: Retrieve a specific vendor's details.
- **PUT /api/vendors/{vendor_id}/**: Update a vendor's details.
- **DELETE /api/vendors/{vendor_id}/**: Delete a vendor.

### 2. Purchase Order Tracking

#### Model Design
The model tracks purchase orders with fields like PO number, vendor reference, order date, items, quantity, and status.

#### API Endpoints
- **POST /api/purchase_orders/**: Create a purchase order.
- **GET /api/purchase_orders/**: List all purchase orders with an option to filter by vendor.
- **GET /api/purchase_orders/{po_id}/**: Retrieve details of a specific purchase order.
- **PUT /api/purchase_orders/{po_id}/**: Update a purchase order.
- **DELETE /api/purchase_orders/{po_id}/**: Delete a purchase order.

### 3. Vendor Performance Evaluation

#### Metrics
- **On-Time Delivery Rate**: Percentage of orders delivered by the promised date.
- **Quality Rating**: Average of quality ratings given to a vendor’s purchase orders.
- **Response Time**: Average time taken by a vendor to acknowledge or respond to purchase orders.
- **Fulfilment Rate**: Percentage of purchase orders fulfilled without issues.

#### Model Design
Fields are added to the vendor model to store these performance metrics.

#### API Endpoints
- **GET /api/vendors/{vendor_id}/performance**: Retrieve a vendor's performance metrics.


## Usage
To use the API, send HTTP requests to the provided endpoints with the required parameters.
