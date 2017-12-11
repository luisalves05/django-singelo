# Singelo
Singelo is a lightweight blog under construction using Django framework.

## Requirements
This project was developed using Django 1.11.4 and Python 3.62.

## Installation

1. Add "singelo" to your INSTALLED_APPS setting like this:**

``` code
    INSTALLED_APPS = [
        ...
        'singelo',
    ]
```

2. Include the Singelo blog URLconf in your project urls.py like:

``` code
    url(r'^singelo/', include('singelo.urls')),
```
3. Inside the django-singelo folder run the following commands:
``` code
    python setup sdist
    pip install dist/django-singelo-0.1.tar.gz
```
4. Run 'python3 manange.py makemigrations singelo' to make the migration files

5. Run 'python3 manange.py migrate singelo' to apply the migration files.

5. Start the development server and visit http://127.0.0.1:8000/admin to create a post (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/singelo/ and starting blogging :)

## Do you want to improve it?
Clone or fork and send me a pull request, thanks!
 
## License
MIT
