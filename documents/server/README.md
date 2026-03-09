# servers

servers are computers that runs applications and services.
It provides service to the use and another computer.
They are stored in data centers, all of the servers are connected to the internet and running different applications.

Data centers are built based on the service purpose, for instance if it provides more content like images and videos, it will have more hard drive space.
these devices are called ` hardware` and the piece of code that run on them are known as `software`.

## web server

a web server commonly do the following tasks.

- website storage and administration
- data storage
- security
- managing emails
- responding ot web requests from the client

## webpage

a webpage is a document that displays image, videos, text and various content, it is a single page.

## website

a website is collection of webpages that are linked together.

## web application

web applications are more interactive where websites are more informative like `wikipedia`.

## page rendering

when the server sends the page content, the process of reading the code and creating the page on the screen is known page rendering.

## browser

It is a software that allows us to browse on world wide web.

## HTTP

a protocol that is used between the client(user) and the server.
it is used to transfer web resources like images, HTML, videos and so on.

## Library

A library supplies reusable pieces of code that we can use in our application instead of having to re-create the required code.
they are built for a specific purpose.
For instance a library for validating the emails.

## Framework

Frameworks provides the blueprint or structure to work with.
It defines flow and control of our application.
they provide a solid foundation to build upon, just like a house foundation.

#### Advantages

- time saving
- structure
- best practices

in frameworks, we are having more freedom.

## Web Framework

A software framework, in general, is a standard, reusable software platform that facilitates the rapid development of software applications.

The web framework (also called web application framework) provides a generic functionality needed for building web applications, APIs and web services.
For example, you can easily connect your application to databases. Usually, the framework handles tasks such as session management much more efficiently.

## API

application program interfaces that allows us to interact with an application.

## WSGI (Web Server Gateway Interface)

WSGI is designed for synchronous applications. It operates in a blocking, request-response model, which means it handles one request at a time in a linear fashion

Usage: WSGI is widely used in frameworks like Django (before Django 3.0), Flask, and Pyramid. It works well for apps where I/O (like database queries or file reads) is not heavily concurrent.
Limitations: WSGI struggles with real-time applications like WebSockets or long-polling connections because of its blocking nature.

## ASGI (Asynchronous Server Gateway Interface)

Asynchronous: ASGI is designed to handle both synchronous and asynchronous operations. It can manage long-lived connections and high-concurrency tasks, making it ideal for real-time apps like WebSockets, chat applications, or async API servers.

Usage: ASGI is used by frameworks like Django (3.0+ for async support), FastAPI, and Starlette. It provides support for WebSockets, HTTP2, and other modern protocols.
Flexibility: ASGI works well for both simple and complex use cases, enabling features like background tasks, WebSocket connections, and event-driven architectures.

### websocket

A WebSocket is a communication protocol that provides full-duplex (two-way) communication between a client (usually a web browser) and a server over a single, long-lived connection. Unlike traditional HTTP, where the client requests data from the server and the server responds once, WebSocket allows both the client and server to send messages to each other at any time.
