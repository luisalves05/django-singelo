django-singelo/README.rst
=====
Singelo Blog
=====

Singelo is a simple Blog engine developed using Django. 

Quick start
-----------

1. Add "singelo" to your INSTALLED_APPS setting like this::

   INSTALLED_APPS = [
        ...
        'singelo',
   ]

2. Include the Singelo blog URLconf in your project urls.py like::

   url(r'^singelo/', include('singelo.urls')),

3. Run 'python3 manange.py migrate' to create the Singelo models.

4. Start the development server and visit http://127.0.0.1:8000/admin
   to create a post (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/singelo/ to starting blogging. 
