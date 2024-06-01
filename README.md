# Job Hunt

Job Hunt is a web application built using Flask that allows users to search for the latest job listings from <a href="https://www.timesjobs.com/">TimesJobs.com</a> based on their skills.

## Features

- Search for job listings based on skills.
- Scrapes the latest job listings from TimesJobs.com.
- Provides job details including company name and job description.
- Provides application link for the job.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/kindo-tk/job_hunter.git
    ```

2. Navigate to the project directory:
   ```sh
   cd .\job_hunter\
   ```
   
3. Activate the virtual environment

    ```bash
    cd .\.venv\Scripts\
    
    .\activate
    ```

4. Install the required dependencies after going back to the `job_hunter` directory (only if the app.py is not running):
   
    ```bash
    pip install -r requirements.txt
    ```

5. Run the Flask application:

    ```bash
    python app.py
    ```

6. Open your web browser and navigate to http://localhost:5000 to access the application.


## Usage

1. Visit the homepage of the application.
2. Enter your skills separated by commas into the provided input field.
3. Click on the "Search Jobs" button to view the latest job listings matching your skills.
4. View the job details including company name and job description.


## Deployment

You can access the deployed application at the following URL: https://weatherapp-hws1.onrender.com

