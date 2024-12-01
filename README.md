# Job Application Tracker

A web application built using [NiceGUI](https://nicegui.io/) to track job applications. Users can log in, add new applications, view an overview of applications, and manage additional information via tabs.

## Features

- **Authentication**: Secure login and logout functionality.
- **Add Application**: A form to add job applications with fields for the date, job title, company, and description.
- **Overview**: A tab to display and manage all job applications.
- **Extras**: Placeholder for additional features.

## Project Structure

```plaintext
src/
├── pages/
│   ├── __init__.py
│   ├── login_page.py          # Login / register page
│   ├── main_page.py          # Main application page with header and tabs
│   ├── tabs/
│   │   ├── __init__.py
│   │   ├── add_application.py  # Add Application tab logic
│   │   ├── applications_overview.py  # Applications Overview tab logic
│   │   ├── extras.py          # Extras tab logic
├── app.py                   # Application entry point
├── requirements.txt         # Python dependencies
Dockerfile                   # Docker configuration
docker-compose.yml           # Docker Compose configuration
```
## Requirements

- Python 3.10
- Docker and Docker Compose

## Installation

### 1. Clone the repository
```bash
git clone <repository_url>
cd job-application-tracker
```

### 2. Install dependencies
```bash
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r src/requirements.txt
```

### 3. Run the application locally
```bash
python src/app.py
```
The application will be available at http://localhost:8080.

Or run the app using docker compose:
```bash
docker-compose -f docker/docker-compose.yml up -d
```

## Environment Variables

Ensure the following environment variables are set for production:

- `USERDB_DATABASE=${USERDB_DATABASE}`
- `USERDB_HOST=${USERDB_HOST}`
- `USERDB_PORT=${USERDB_PORT}`
- `APP_SECRET=${APP_SECRET}`

These can be defined in a `.env` file or passed as arguments to `docker run` or `docker-compose`.
