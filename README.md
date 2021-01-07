# Django Photo API
Simple REST API for a photo gallery app. Users can create an account and manage their photo collection.


## Installation

Please update `docker-compose.yml` with AWS credentias for S3 file uploads.

Run locally with Docker Compose:
```
docker-compose up
```

## Endpoints

[Postman collection](https://www.getpostman.com/collections/015d3c2d5c26e1708bc4)

### JSON Web Token endpoint
Method | Endpoint | Functionanlity
--- | --- | ---
POST | `/api-token-auth` | Request jwt token

### User Endpoints

Method | Endpoint | Functionality
--- | --- | ---
GET | `/api/user` | List users
GET | `/api/user/create` | Creates a user
GET | `/api/user/profile/{pk}` | Retrieve a user
PUT | `/api/user/update/{pk}` | Edit a user
DELETE | `/api/user/destroy/{pk}` | Delete a user

### Image Endpoints
Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/user/images/upload` | Upload an image, image_type private or public.
GET | `/api/user/images/public` | List of public image URLs

## Utility Commands

After updating the data model, make migrations and migrate.
```
python manage.py makemigrations && python manage.py migrate
```

Create super user
```
python manage.py createsuperuser
```

Run tests
```
python manage.py test
```


## Technologies
- Django
    - [Django REST framework](https://www.django-rest-framework.org/)
    - [Django Storages](https://github.com/jschneier/django-storages) for uploading to AWS S3
    - SQLite database
- Amazon Web Services
    - S3 for images
    - Elastic Beanstalk for hosting
- Docker


## Resources

The following resources where helpful in making this API:

- [Simple boilerplate for django rest framework](https://github.com/p8ul/django-rest-framework-boilerplate)
- [How to Implement Token Authentication using Django REST Framework](https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html)
- [Storing Django Static and Media Files on Amazon S3](https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/)

