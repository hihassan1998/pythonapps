## Maths by Python API Project Documentation
##  Introduction
I create a basic application of mathematical functions and deploy it over a web interface using Flask. The purpose is to connect all the pieces of knowledge gained in the course till now, and see the application development and deployment steps in action.


# Objectives
In this assignment i will:

Task 1: Create the mathematical functions.
Task 2: Package the functions and test the package.
Task 3: Web Deployment of the application package using Flask.




## Step 1: Clone Dependency Repository

To get started with this basic Maths project, you need to clone the dependency repository:

```bash
git clone https://github.com/ibm-developer-skills-network/hjbsk-build_deploy_app_flask
Step 2: Set Up the Maths Project
Follow these steps to set up the Maths project:

Create a folder named "Maths" and change to that directory:

bash
Copy code
mkdir Maths
cd Maths
In the "Maths" directory, create a new file called mathematics.py. Add the following functions:

summation(a, b)
subtraction(a, b)
multiplication(a, b)
Step 3: Package the Functions
Perform the following steps:

Create an __init__.py file in the "Maths" directory.

Import the file mathematics.py into the __init__.py file:

python
Copy code
from . import mathematics
Import the package "Maths" in server.py:

python
Copy code
from Maths.mathematics import summation, subtraction, multiplication
Implement methods in server.py for the following endpoints:

/: Renders the index.html page.
python
Copy code
@app.route("/")
def render_index_page():
    return render_template('index.html')
/sum: Uses the summation function, taking num1 and num2 as float inputs through the request parameter, and returns a string output.

/sub: Uses the subtraction function, taking num1 and num2 as float inputs through the request parameter, and returns a string output.

/mul: Uses the multiplication function, taking num1 and num2 as float inputs through the request parameter, and returns a string output.

Step 4: Web Deployment
To deploy the application package using Flask, change the current directory in the terminal to the hjbsk-build_deploy_app_flask directory and run the server:
s
bash
Copy code
cd /path/to/hjbsk-build_deploy_app_flask
python3.11 server.py
This will launch the server, and you can access the application through the specified endpoints.