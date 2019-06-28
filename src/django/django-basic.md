## django basic

### Start a Project

```python
django-admin.py startproject tango_my_django
```

### Add a static content folder (Javas­cri­pt/CSS)

**mkdir -p tango_my_django/static/css**

**mkdir -p tango_my_django/static/js**

__tango_my_django/tango_my_django/settings.py__

```python
STATIC_PATH = os.path.join(PROJECT_PATH,'static') 
STATIC_URL = '/static/' 
STATICFILES_DIRS = (
    STATIC_PATH,
)
```

### Add a Templates Folder

**mkdir -p tango_my_django/templates/rango**

__tango_my_django/tango_my_django/settings.py__

```python
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
TEMPLATE_DIRS = (TEMPLATE_PATH,)
```

### Create a Template

__tango_my_django/templates/rango/index.html__

```python
<!DOCTYPE html>
{% load static %}

<html>
     <head>
     ....
```

### Start a App

```python
tango_my_django/manage.py startapp tango_my_django/rango
```

### Add App to Project

__tango_my_django/settings.py__

```python
INSTALLED_APPS = ( ..., ..., 'rango', )
```

### Route from Project to App

__tango_my_django/tango_my_django/urls.py__

```python
# Include tango_my_django/rango/urls.py 
urlpatterns = patterns('', url(r'^mainApp/', include('mainApp.urls')),)
```

### Route from App to View

__tango_my_django/rango/urls.py__

```python
from django.conf.urls import url, patterns
from mainApp import views

urlpatterns = patterns('', url(r'^$', views.index, name='index'),)
```

### Create a view

__tango_my_django/rango/views.py__

```python

from django.conf.http import HttpResponse

def index(request):
    return HttpResponse("hello rango")
```

### Use Template inside a View

__tango_my_django/rango/views.py__

```python

from django.shortcuts import render_to_response 
from django.template import RequestContext

def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage' : 'I come from context_dict'}
    return render_to_response('mainApp/index.html', context_dict, context)
```