## What is CSRF?

**Cross-Site Request Forgery (CSRF)** is an attack where a malicious website tricks your browser into sending a request to a site you’re already logged into — without you knowing.

### How the attack works

Imagine this scenario:

1. You log in to your bank (`bank.com`). Your browser stores a session cookie.
2. You open a new tab and visit `evil-site.com`.
3. That site has a hidden form like this:

```html
<!-- on evil-site.com -->
<form action="https://bank.com/transfer" method="POST">
	<input type="hidden" name="to" value="attacker" />
	<input type="hidden" name="amount" value="5000" />
</form>
<script>
	document.forms[0].submit();
</script>
```

4. Your browser sends the POST request to `bank.com` **with your session cookie attached** — because that’s how cookies work.
5. The bank sees a valid session and processes the transfer. You never clicked anything.

- The key problem: the bank has no way to tell if the request came from its own form or from a malicious site.

### Why it happens

Two things make CSRF possible:

- **Cookies are sent automatically.** Your browser attaches cookies to every request to a domain, regardless of which site initiated the request.
- **The server can’t tell the origin.** Without extra protection, a POST from `evil-site.com` looks identical to a POST from the real site.

### How Django prevents it — the full token lifecycle

Django uses a **CSRF token** — a random, secret value delivered through two different channels.

**Step 1: You visit a page with a form (GET request)**

Django generates a random token (e.g. `abc123`) and does two things:

1. Sets a **cookie**: `csrftoken=abc123`
2. Embeds the same token as a **hidden field** in the form HTML:

```html
<form method="POST">
	{% csrf_token %}
	<input type="text" name="message" required />
	<button type="submit">Send</button>
</form>
```

This renders as:

```html
<input type="hidden" name="csrfmiddlewaretoken" value="abc123" />
```

- The token cookie is **only set** when Django renders a template containing `{% csrf_token %}`. No form on the page = no cookie.

**Step 2: You submit the form (POST request)**

Your browser sends **both**:

- The `csrftoken` cookie (automatically, like all cookies)
- The `csrfmiddlewaretoken` value in the POST body (from the hidden field)

**Step 3: Django compares them**

```
token from POST body  ==  token from cookie  ->  200 OK
token from POST body  !=  token from cookie  ->  403 Forbidden
token from POST body is missing               ->  403 Forbidden
```

### Why the attacker can’t beat this

The attacker’s site can trigger a POST to `bank.com`, and yes, the browser **will** send the `csrftoken` cookie automatically. But the attacker **cannot**:

1. **Read the cookie** — browsers enforce the Same-Origin Policy, so `evil-site.com` cannot read cookies belonging to `bank.com`
2. **Put the token in the POST body** — since they can’t read it, they can’t include the matching hidden field

So Django gets: cookie = `abc123`, POST body = empty. Mismatch -> 403.

- The cookie and the hidden field are the **same token delivered through two different channels**. Only the real site can deliver both. That’s the entire trick.

### When does Django check the token?

Django only validates the CSRF token on **unsafe** HTTP methods:

| Method | Cookie sent?           | Token checked? |
| ------ | ---------------------- | -------------- |
| GET    | Yes (if cookie exists) | No             |
| POST   | Yes                    | Yes            |
| PUT    | Yes                    | Yes            |
| DELETE | Yes                    | Yes            |

- This is why the rule exists: **never use GET requests to modify data.** Django assumes GET is safe and skips CSRF checks entirely.

### Quick rules

| Rule                          | Details                                                        |
| ----------------------------- | -------------------------------------------------------------- |
| Always add `{% csrf_token %}` | Inside every `<form method="POST">` in your templates          |
| Only needed for POST          | GET requests don’t need it (they shouldn’t modify data anyway) |
| Django enforces it by default | Via `CsrfViewMiddleware` in `settings.py`                      |
| Never disable it              | Unless you know exactly what you’re doing                      |

### What about reading the cookie with JavaScript?

An attacker might think: "I'll use JavaScript to read the `csrftoken` cookie and inject it into my forged form." But this doesn't work because of the **Same-Origin Policy**:

```js
// on evil-site.com
document.cookie; // only shows evil-site.com's cookies, NOT bank.com's
```

The browser completely walls off cookie access between different domains.

### The one exception: XSS

If an attacker injects JavaScript **into your own site** (an XSS attack), that script runs on your domain and _can_ read the cookie:

```js
// malicious script injected INTO bank.com via XSS
document.cookie; // can now read csrftoken — game over
```

This is why **XSS and CSRF are related** — XSS bypasses CSRF protection entirely. It's also why Django auto-escapes template variables by default (`{{ variable }}` escapes HTML) to prevent XSS in the first place.

> CSRF protection assumes the attacker is on a **different site**. If they're already running code on your site (XSS), you have a bigger problem.

See [django-forms.md](django-forms.md) for Django Form and ModelForm usage, HTML forms, messages, and validation.
