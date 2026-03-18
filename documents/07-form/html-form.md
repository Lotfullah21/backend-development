# Forms

HTML forms are used to collect data from users.

You use forms when you want the user to:

- log in
- sign up
- search
- send a message
- choose options
- upload files

In short, a form is the part of a web page where the user gives information to the browser, and the browser sends that information to a server.

## What A Form Does

A form does three main jobs:

1. It displays input controls such as text fields, radio buttons, checkboxes, and dropdowns.
2. It lets the user enter or choose data.
3. It sends that data when the form is submitted.

## How A Form Works

The flow is simple:

1. The browser reads the `<form>` element and shows the input fields.
2. The user types or selects values.
3. The browser checks basic validation rules such as `required`, `type="email"`, `min`, or `maxlength`.
4. When the user clicks the submit button, the browser collects the values.
5. The browser sends the data to the URL inside `action` using the HTTP method inside `method`.
6. The server processes the data and sends a response back.

## Basic Structure

```html
<form action="/contact" method="post">
	<label for="email">Email</label>
	<input type="email" id="email" name="email" required />

	<label for="message">Message</label>
	<textarea id="message" name="message"></textarea>

	<button type="submit">Send</button>
</form>
```
