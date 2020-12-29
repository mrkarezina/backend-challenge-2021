# Django Photo API
Simple REST API for managing photos.



## Installation

Please update `docker-compose.yml` with AWS credentias for S3 file uploads.

Run locally with Docker Compose:
```
docker-compose up
```

## Endpoints

### Jwt token endpoint
Method | Endpoint | Functionanlity
--- | --- | ---
POST | `/api-token-auth` | Request jwt token

### User Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/user` | List users
GET | `/api/user/create` | Creates a user
GET | `/api/user/profile/{pk}` | Retrieve a user
POST | `/api/user/upload/{pk}` | Upload image to user 



## Helpful Commands

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
    - **PostgreSQL** database
- Amazon Web Services
    - S3 for images
    - Elastic Beanstalk for hosting
- Docker


## Resources

This was my first time using Django. The following resources where helpful in making this api:

- [Simple boilerplate for django rest framework](https://github.com/p8ul/django-rest-framework-boilerplate)
- [How to Implement Token Authentication using Django REST Framework](https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html)
- [Storing Django Static and Media Files on Amazon S3](https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/)

