# Notifications

## Installation

1. Clone the repository:
    ```shell
    
    git clone git clone https://github.com/y-kondrashova/notifications.git
    cd notifications
    ```
2. Set up virtual environment:
   ```shell
   
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```shell
   
   pip install -r requirements.txt
   ```

4. Create migrations
   ```shell
   
   python manage.py makemigrations
   python manage.py migrate
   ```
   
5. Add test data to db
   ```shell
   python manage.py loaddata data.json
   ```

## API Endpoints

### User Endpoints

 - `POST /api/user/register/` - Register a new user.
 - `GET /api/user/me/` - Retrieve the authenticated user's profile.
 - `POST /api/user/tokens/` - Obtain access and refresh tokens.
 - `POST /api/user/tokens/refresh/` - Refresh access tokens.

### Notifications Endpoints

 - `GET /api/notifications/text/` - Retrieve all user notifications.
 - `POST /api/notifications/text/` - Create a new notification.
 - `GET /api/notifications/settings/` - Retrieve user notification settings.
 - `PUT /api/notifications/settings/<id>/` - Update notification settings.
 - `GET /api/notifications/categories/` - Retrieve all notification categories.
 - `GET /api/notifications/templates/` - Retrieve all notification templates.

### Project Endpoints

 - `GET /api/projects/` - Retrieve all projects.
 - `POST /api/projects/` - Create a new project.
 - `GET /api/projects/<id>/` - Retrieve a specific project by ID.
 - `PUT /api/projects/<id>/` - Update a project.
 - `DELETE /api/projects/<id>/` - Delete a project.

### Translation Endpoints

 - `GET /api/translations/languages/` - Retrieve all supported languages.
 - `POST /api/translations/languages/` - Add a new language.
 - `GET /api/translations/translation_strings/` - Retrieve all translation strings.
 - `POST /api/translations/translation_strings/` - Create a new translation string.

**Credentials for test user**

 - **username**: `tom`
 - **password**: `tom12345`
