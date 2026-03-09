## template

templates are text based document or python strings marked up using django template language(DTL).

templates contains mainly two kinds of content.

- `static content`: the html that does not change on the webpage.
- `template language`: it is a syntax that allows us to insert dynamic data.

The contents presented `{{}}` are dynamic content and the rest are static content.

```html
<li>take the following course: {{course}}</li>
```

template handles the user interface of the page.

To pass the data from view to templates, we use from context property and pass the data in the form of a dictionary and access the context data using its key in the template.

## dynamic content

data that changes according to context, user behavior, and preferences.

## django template language

`DTL` is the language to add dynamic content inside a template.

## template engine

template engine process django template engine like variables, expressions, and statements.

## tag

`{% %}` this tag is used to build loops, conditional statements.

## variable

`{{}}` is used for having variables inside a template.

## How it works

- view function retrieve data from a database
- we use template and django template language to display the retrieved data.

Django template language uses curly braces ({{ }}) for rendering variables and expressions, and percentage signs ({% %}) for executing template tags and filters.

## render

render is a function used inside view and it takes three parameters,`render(request, path, context)`.
render returns a string for a http request.

- request, represents the initial request
- path is address to the template
- context contains a dictionary that template can use to display dynamic data.

#### using for loop in template

the data is particular to the templates we are inside that particular function.

To write a loop inside our template we should follow the following syntax.

`./home/views.py`

```py
def index(request):
    courses = ["ai","js","dl","css","html"]
    num = random.randint(10, 1000)
    return render(request,"index.html", context={"random_number":num, "courses":courses})
```

`./home/index.html`

```py
{%for course in courses%}
	<li>{{course}}</li>
{%endfor%}
```

`{%endfor%}` is crucial here, as it shows the end of for loop.

#### using if-else block in template

`./home/views.py`

```py
def index(request):
    courses = ["ai","js","dl","css","html"]
    age = 21
    num = random.randint(10, 1000)
    return render(request,"index.html", context={"random_number":num, "courses":courses, "age":age})
```

`./home/index.html`

```html
{% if age > 20 %}
<h1>You can vote</h1>
{% endif %}
```

Take care of the spacing, `	{% if age>20 %}` will raise an error.

#### adding else

```html
{% if age > 20 %}
<h1>You can vote</h1>
{% else %}
<h2 style="color: red">you cannot vote</h2>
{% endif %}
<h1>Welcome to Hooshmandlab</h1>
```

## Inheritance

Using inheritance, we can use a common block of code inside our templates.

## extends

It creates a parent child relationship where parent's functionality can be overwritten.

Base Template: Defines the overall layout structure, including header, footer, navigation, and other common elements.

Child Templates: Extend the base template and provide content specific to individual pages.

Blocks: Designated sections in the base template that child templates can override or fill with custom content.

Context: Data passed from views to templates, accessible within both base and child templates.

We can write a reusable piece of code in one template and use it in other template using inheritance property.
`./home/base.html`

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>django</title>
	</head>
	<body>
		<div style="padding: 4rem 2rem">{%block start%} {% endblock %}</div>
	</body>
</html>
```

`./home/contact.html`

```html
{% extends "base.html" %} {%block start%}

		<nav style="padding: 4rem">
			<a href="{%url 'index'%}">home</a>
			<a href="{%url 'about'%}">about</a>
		</nav>

		<h1>Hello from contact page</h1>
		<p>name: Hooshmandlab</p>
		<p>address: server</p>
		<p>field: educational technology</p>
	</body>
</html>

{%endblock%}

```

inside `{%block start%} {% endblock %}`, we will place our dynamic content.

## include

Using include, it renders a template in the current context.

In Django templates, the include tag allows you to insert the contents of one template into another, promoting code reuse and modularity.

It's different from inheritance, as it doesn't create a parent-child relationship between templates. Instead, it simply incorporates a specific portion of one template into another.

`./home/image.html`

```html
<img
	style="width: 220px; height: 230px"
	src="https://images.pexels.com/photos/28766046/pexels-photo-28766046/free-photo-of-healthy-breakfast-bowl-with-oats-and-fruits.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" />
```

`./home/contact.html`

```html
{% extends "base.html" %} {%block start%}

<nav style="padding: 4rem">
	<a href="{%url 'index'%}">home</a>
	<a href="{%url 'about'%}">about</a>
</nav>
{% include "image.html" %}
<h1>Hello from contact page</h1>
<p>name: Hooshmandlab</p>
<p>address: server</p>
<p>field: educational technology</p>

{%endblock%}
```
