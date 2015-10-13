# Introduction #
This guide will show you have to get Data Wrap up and running using the example configuration that is included in the download.

## Dependencies ##

Data Wrap has some dependencies that you will need to make sure you have installed.

  1. [Python](http://python.org/)
  1. [Django](http://www.djangoproject.com/)
  1. [libRETS](http://code.crt.realtors.org/projects/librets/) - This needs to include the Python bindings.
  1. [PyYaml](http://pyyaml.org/) - A YAML library for python.

## Running ##

Once the dependencies have been install, download Data Wrap and unzip it.  Go into the data\_wrap directory and type

`python manage.py runserver`

If everything has been installed correctly Django should start up.

Now to check that Django is running Data Wrap, go to the URL: http://127.0.0.1:8000/Translator/Properties/-/res/?ListPrice=250000.

## Installing Into Existing Django Project ##
If you already have a Django project you wish to run Data Wrap in do the following.

  1. Copy the directories _Atom2RETS_ and _templates_ to your Django project
  1. Copy rets.yaml to your Django project
  1. Edit your projects url.py file and add the following
```
from Atom2RETS.views import LatestEntries
...
feeds = {
...
    'Translator': LatestEntries,
}

urlpatterns = patterns('',
    (r'^(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)

```
  1. Edit settings.py and add the following.
```
TEMPLATE_DIRS = (
...
    'templates',
)

INSTALLED_APPS = (
...
    'Atom2RETS',
)
```

## Customize Configuration ##
Once you have Data Wrap installed and running, customize your Django project as you like and also edit the rets.yaml file to pull from the RETS servers you will to make feeds from.  See [Configuration#Configuring](Configuration#Configuring.md) for more details.