# honors_ui: Enhancing Web UI/UX through Design and Psychology

## Project Summary

The `honors_ui` project, spearheaded by Ethan Rohman as part of his Honors Thesis, aims to bridge the gap between technology, art, and psychology to enhance the user experience on the web. By leveraging advanced design principles and psychological insights, this project develops experimental websites to study and improve user engagement and satisfaction. The project utilizes a combination of Postgres, Django, and Next.js to track user interactions and analyze the effectiveness of various design interventions.

## Technologies Used

- **Database:** Postgres
- **Backend:** Django Web Framework
- **Frontend:** Next.js
- **Server:** Nginx 

## Features

- Experimental web interfaces with unique design elements
- Application of design principles such as the rule of thirds, Fibonacci sequence, and golden ratio
- Psychological studies on the impact of design choices on user behavior
- Tracking of user interactions for data analysis
- Static Site Generation (SSG) with Next.js for enhanced UI/UX elements

## Getting Started

### Prerequisites

- Docker (optional for containerized environments)
- Python 3.10 or newer
- Node.js 12.x or newer
- PostgreSQL 14 or newer

### Installation

1. Clone the repository: Use the command git clone followed by the repository URL and then navigate into the honors_ui directory.
2. Set up a virtual environment (optional): Use python -m venv venv to create a virtual environment and then activate it.
3. Install Django dependencies: Run pip install -r requirements.txt to install the required packages.
4. Install Next.js dependencies: Navigate to the frontend directory (assuming your Next.js project is in a directory named frontend) and run npm install.
5. Configure Postgres: Ensure Postgres is running and create a database for the project. Update the Django settings.py file with your database credentials.
6. Run migrations: Use python manage.py migrate to apply database migrations.
7. Start the Django server: Run python manage.py runserver to start the local development server.
8. Build and run the Next.js frontend: Within the frontend directory, use npm run build to build your project and npm start to run it.
9. Configure Nginx as a proxy for Django (optional): Refer to the Nginx documentation for setting up a reverse proxy to your Django application.

## Usage

Navigate to the URLs served by Django and Next.js to interact with the experimental web interfaces. The application tracks user interactions for analysis.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Special thanks to the fields of technology, art, and psychology for inspiring this project.
- Gratitude to the Django and Next.js communities for their invaluable resources.
