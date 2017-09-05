# Singelo
Singelo is a lightweight blog developed using Django framework.

## Requirements
This project was developed using Django 1.11.4 and Python 3.62.

## Installation

**1. Add "singelo" to your INSTALLED_APPS setting like this:**

``` code
    INSTALLED_APPS = [
        ...
        'singelo',
    ]
```

**2. Include the Singelo blog URLconf in your project urls.py like:**

``` code
    url(r'^singelo/', include('singelo.urls')),
```
**3. Run 'python3 manange.py migrate' to create the Singelo models.**

**4. Start the development server and visit http://127.0.0.1:8000/admin to create a post (you'll need the Admin app enabled).**

**5. Visit http://127.0.0.1:8000/singelo/ and starting blogging :)**

## Preview
![Main Page](http://i.imgur.com/bmp74AH.png)


## Do you want to improve it?

**Clone or fork and send me a pull request, thanks!**
 
## License
MIT
