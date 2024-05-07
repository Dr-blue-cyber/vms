# Django Application Documentation

## Cloning and Setting Up the Django Application

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
