django-dignity-parallax
=======================

Dignity: http://themeforest.net/item/dignity-simple-portfolio-responsive-retina-html5/6021446

Dignity is a simple & easily reusable web template with a clean design and neat arrangement of contents.
A perfect onepage portfolio for all creatives.

I took The Dignity Parallax template and placed it into this Django skeleton, but altered it to make it as dynamic as possible.

I used WPAdmin (Wordpress Admin) as the admin backend - along with TinyMCE at specific points.
https://github.com/barszczmm/django-wpadmin

This project is great for bootstrapping your startup- it's very awesome for those of you who want the Dignity template
as dynamic as possible (Django is also a massive benefit).

```
Features:
1. Choose between the four template colors: Blue, Yellow, Red, Green
2. The backgrounds are dynamic so you can load in as many images as you want.
3. All text is dynamic - so you don't have to jump into any HTML.
4. The admin looks awesome and can be skinned to any of WPAdmin's themes (inside settings)

Installation:
1. Download this Repo with git.
2. Create your project's virtualenv - if you don't work with Django and virtualenv's this project isn't for you.
   However, if you are starting out, This may help (it is directed at deploying the project live - you can use DigitalOcean): 
   http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/
3. $ pip install -r requirements
4. Configure your database/debug settings in settings_local.py
5. $python manage.py syncdb --migrate
6. $python manage.py runserver
```

Please note, this project does use easy-thumbnails==1.3 to crop images on the Dignity template - in order to have the jpeg's
supported and cropping correctly, you will need PIL (or pillow - whatever works for you). PIL always gives me issues
- so Inside the requirements.txt file, I've placed as many instructions in there to help install PIL and get it up and
running correctly.

If you have any issues email me at paulvonhoesslin@gmail.com
