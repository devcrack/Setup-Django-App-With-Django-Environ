Based on the above, we see that environment variables are the perfect place to store settings.

Writing code using os.environ could be tricky sometimes and require additional effort to handle errors. It’s better to use django-environ instead.

Notes: For this example the .env file is placed in the root path of the project, remember that! :v:
A similar approach is used in [Two Scoops of Django book](https://www.feldroy.com/) and explained in [12factor-django article](https://wellfire.co/learn/easier-12-factor-django/)

More about django-environ:
[django-environ Documentation](https://django-environ.readthedocs.io/en/latest/#)



