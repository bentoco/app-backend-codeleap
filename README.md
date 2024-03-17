# CodeLeap coding test!

## 1. Environment Setup

To run the application locally, follow these steps:

### 1.1 Prerequisites
- Docker installed on your local machine

### 1.2 Setup Docker Environment
- Navigate to the `locals` folder in your project directory.
- Use the following `docker-compose.yml` configuration:

```yaml
services:
  postgres:
    image: 'postgres:14.2-alpine'
    environment:
      POSTGRES_USER: 'root'
      POSTGRES_PASSWORD: 'root'
      POSTGRES_DB: 'codeleap'
    ports:
      - '5432:5432'
    networks:
      - codeleap-network

networks:
  codeleap-network:
    driver: bridge
    ipam:
      config:
        - subnet: 10.10.1.0/24
```

- Run the following command to start the PostgreSQL container:

    ```bash
    docker-compose up -d
    ```

### 1.3 Database settings

Update your Django settings (settings.py) to use the PostgreSQL database:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'codeleap',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 1.4 Migrate Database

Run Django migrations to create necessary database tables:

```bash
python manage.py migrate
```

## 2. Overview of API View
The CareerListCreateAPIView and CareerRetrieveUpdateDestroyAPIView provide endpoints to manage career posts.

### 2.1 CareerListCreateAPIView
- URL: /careers/
- Methods: GET (list all career posts), POST (create a new career post)
- Pagination: 10 posts per page, with a maximum of 100 posts per page
- Example Usage:
  - GET: Retrieve all career posts with pagination.
  - POST: Create a new career post by sending username, title, and content data in the request body.

### 2.2 CareerRetrieveUpdateDestroyAPIView
- URL: /careers/<post_id>/
- Methods: PATCH (update a specific career post), DELETE (delete a specific career post)
- Example Usage:
  - PATCH: Update a specific career post by its ID with new title and content data.
  - DELETE: Delete a specific career post by its ID.

### 3. Running Unit Tests

To run unit tests for the Django application, execute the following command:

```bash
python manage.py test careers
```