# Backend Development: From APIs to Deployment

## Purpose of this document

These notes explain the supplied backend-development transcript in
beginner-friendly language. They follow the video's chapters and
timestamps, clarify technical vocabulary, and correct a few
oversimplifications.

This chapter builds on the earlier **Introduction to the Internet**
notes:

-   The Internet connects networks and computers.
-   IP addresses help route data to the right network destination.
-   Clients request services, and servers provide them.
-   Packets carry data across networks.

Now we will look at what happens **inside a web application**: how the
frontend communicates with backend code, how backend code works with
databases, and how applications are hosted.

------------------------------------------------------------------------

# Chapter 1: What Is Backend Development?

**Transcript timestamps: 0:00--0:47**

The video begins by explaining that when you visit a website, some code
is sent to and runs in your browser. This is the **frontend**. The
browser is acting as a **client**.

Other work happens on servers. Examples include processing
recommendations, applying business rules, handling payments, and
accessing user data. This is the **backend**.

A server needs software that can receive and process requests.
Developers build backend applications using frameworks and languages
such as:

-   Java with Spring Boot
-   Python with FastAPI, Django, or Flask
-   JavaScript with Express.js or NestJS
-   Go with its web libraries and frameworks
-   C# with ASP.NET Core

The video then introduces a fictional app as an example.

## Explanation: Frontend vs. Backend

A web application commonly has two major sides.

### Frontend

The frontend is the part users interact with. In a browser, it commonly
uses:

-   **HTML** --- describes the structure and content of a page.
-   **CSS** --- controls the appearance and layout.
-   **JavaScript** --- adds behavior and interactivity.

For example, a profile page might show a person's name, photo, and an
Edit button. The browser displays the page and handles the button
interaction.

### Backend

The backend handles work that should be performed by the server, such
as:

-   Checking whether a user is signed in.
-   Validating information submitted by a user.
-   Applying application rules.
-   Reading and writing database records.
-   Returning data to the frontend.
-   Coordinating services such as email notifications.

For example, clicking **Save profile** may cause the frontend to send
the new profile information to the backend. The backend validates it and
saves it to a database.

### A simple comparison

  -----------------------------------------------------------------------
  Frontend                            Backend
  ----------------------------------- -----------------------------------
  Runs in the user's browser or app   Runs on a server or server
                                      environment

  Displays information                Processes requests and application
                                      rules

  Handles user interactions           Handles data access and server-side
                                      operations

  Sends requests                      Receives and responds to requests
  -----------------------------------------------------------------------

**Important:** Frontend and backend are roles, not necessarily separate
programming languages. JavaScript can run in the browser and on the
server using a runtime such as Node.js.

## What is a backend server?

A backend server is not just a computer sitting online. It is useful to
distinguish:

-   **Server hardware:** the physical or virtual computer.
-   **Server software:** the program that listens for and processes
    requests.
-   **Server role:** the job of providing a service to clients.

A backend application commonly listens for incoming network requests on
a configured port. It then decides what to do with each request.

For example:

`Browser → Internet → Backend application`

The backend application receives the request, performs the required
work, and sends a response.

## What is a backend framework?

A framework provides reusable tools and conventions so developers do not
need to build every feature from scratch.

  Language                  Common backend framework
  ------------------------- --------------------------
  Java                      Spring Boot
  Python                    Django, Flask, FastAPI
  JavaScript / TypeScript   Express.js, NestJS
  C#                        ASP.NET Core

You do not need to learn all of them at once. The fundamental
concepts---requests, responses, routing, validation, databases,
authentication, and error handling---transfer between frameworks.

------------------------------------------------------------------------

# Chapter 2: How Backend APIs Work

**Transcript timestamps: 0:47--1:51**

The video explains that backend applications expose different URL
endpoints for different operations.

It introduces the term **API**, meaning Application Programming
Interface. An API is an interface that allows one software system to
communicate with another.

The video then introduces four common data operations:

-   Create
-   Read
-   Update
-   Delete

These are commonly abbreviated as **CRUD**.

## What is an API?

An API is a defined way for software components to interact.

For a web application, the frontend might communicate with the backend
through an HTTP API.

For example:

`Frontend → HTTP request → Backend API`

The backend processes the request and returns an HTTP response.

An API is not necessarily a website or a web address. APIs can also
exist between programs on the same computer, between internal services,
or through other communication mechanisms.

## What is an endpoint?

An **endpoint** is a particular address and operation exposed by an API.

Imagine a profile application. It might provide endpoints such as:

  Purpose            Example endpoint
  ------------------ ---------------------------
  Create a profile   `POST /api/profiles`
  Get all profiles   `GET /api/profiles`
  Get one profile    `GET /api/profiles/42`
  Update a profile   `PUT /api/profiles/42`
  Delete a profile   `DELETE /api/profiles/42`

The `/api` prefix is a common naming convention, not a technical
requirement. An API endpoint does not have to start with `/api`.

## What is CRUD?

CRUD describes the four basic operations commonly performed on stored
data.

### 1. Create

Add a new record.

Example: A new user creates a profile.

### 2. Read

Retrieve existing information.

Example: A user requests a list of profiles.

### 3. Update

Change information that already exists.

Example: A user edits their profile description.

### 4. Delete

Remove a record or mark it as deleted.

Example: A user deletes their profile.

## The request-response cycle

HTTP APIs generally work through a request-response model:

1.  The client sends an HTTP request.
2.  The backend receives the request.
3.  The backend performs the required operation.
4.  The backend sends an HTTP response.
5.  The client processes the response and updates the interface.

A response commonly contains:

-   An HTTP status code.
-   Headers containing metadata.
-   A response body, often containing JSON.

For example, a successful request might return status `200 OK` with
profile data.

A request that creates a new resource might return `201 Created`.

------------------------------------------------------------------------

# Chapter 3: HTTP Methods and Coding a Backend

**Transcript timestamps: 1:51--3:15**

The video maps CRUD operations to HTTP methods:

-   POST
-   GET
-   PUT
-   DELETE

It then demonstrates how a backend framework can implement these
operations.

The video also introduces a common three-layer backend architecture:

1.  Controller layer
2.  Business logic or service layer
3.  Data access layer

Finally, it introduces SQL and NoSQL databases.

## HTTP methods

HTTP methods describe the intended action of a request.

  -----------------------------------------------------------------------
  HTTP method             Common purpose          CRUD relationship
  ----------------------- ----------------------- -----------------------
  `POST`                  Create or submit data   Create

  `GET`                   Retrieve data           Read

  `PUT`                   Replace a resource or   Update
                          create it at a known    
                          URI in some cases       

  `PATCH`                 Partially update a      Update
                          resource                

  `DELETE`                Delete a resource       Delete
  -----------------------------------------------------------------------

The video says there are nine HTTP methods. HTTP actually defines a set
of methods beyond these commonly used ones, including `HEAD`, `OPTIONS`,
`CONNECT`, and `TRACE`.

You will most often encounter `GET`, `POST`, `PUT`, `PATCH`, and
\`DELETE when building ordinary web APIs.

## Example: A profile API

Suppose a client wants to create a profile.

It could send:

``` http
POST /api/profiles
Content-Type: application/json
```

Request body:

``` json
{
  "name": "Alex",
  "age": 21
}
```

The backend might:

1.  Receive the request.
2.  Check whether the required fields exist.
3.  Validate the values.
4.  Save the profile in the database.
5.  Return a response.

A successful response might look like:

``` http
HTTP/1.1 201 Created
Content-Type: application/json
```

``` json
{
  "id": 42,
  "name": "Alex",
  "age": 21
}
```

This is an illustrative example, not a complete production
implementation.

## What is JSON?

**JSON** stands for JavaScript Object Notation.

It is a common text format for exchanging structured data between
applications.

Example:

``` json
{
  "username": "alex",
  "active": true,
  "skills": ["HTML", "CSS", "JavaScript"]
}
```

JSON is language-independent. Python, Java, JavaScript, C#, and many
other languages can read and generate it.

## The three-layer backend architecture

The video introduces a common architecture that separates different
responsibilities.

`<escape>`{=html}`text Client (Browser / Frontend)           |           v    Controller Layer           |           v     Service Layer           |           v  Data Access Layer           |           v        Database``</escape>`{=html}

### 1. Controller layer

The controller handles incoming requests and defines API routes.

Its responsibilities commonly include:

-   Receiving HTTP requests.
-   Reading route parameters and request data.
-   Performing or triggering request validation.
-   Calling the appropriate service.
-   Returning an HTTP response.

Think of the controller as the entry point into the backend application.

### 2. Service layer

The service layer contains the application's **business logic**.

Business logic means the rules that define how the application should
behave.

Examples:

-   A matchmaking algorithm.
-   Checking whether a user is eligible for an operation.
-   Calculating an order total.
-   Applying rules before an account can be updated.

The service layer should not need to know every detail of how HTTP
requests are received.

### 3. Data access layer

The data access layer handles communication with the database.

It may contain methods such as:

-   `findProfileById()`
-   `createProfile()`
-   `updateProfile()`
-   `deleteProfile()`

This separation makes the application easier to understand, test, and
maintain.

**Important:** Not every backend project uses exactly three layers. This
is a common design pattern, not a rule that every application must
follow.

## What is a database?

A database is an organized system for storing and retrieving
information.

For example, a profile application might store:

-   User accounts.
-   Profile information.
-   Messages.
-   Preferences.
-   Relationships between users.

The backend communicates with the database to read or change this
information.

## SQL vs. NoSQL

The video introduces two broad database categories.

### SQL databases

SQL databases are commonly relational databases. They organize data into
tables containing rows and columns.

Example:

**Users table**

    id name       age
  ---- -------- -----
     1 Alex        21
     2 Sam         24
     3 Jordan      22

Relational databases commonly use relationships, constraints, and
schemas to maintain data integrity.

Examples:

-   PostgreSQL
-   MySQL
-   SQLite
-   Microsoft SQL Server

**SQL** stands for Structured Query Language. It is used to work with
relational databases.

Example:

``` sql
SELECT * FROM users;
```

This query retrieves rows from the `users` table.

### NoSQL databases

NoSQL is a broad category of databases that do not all use the
traditional relational-table model.

A document database such as MongoDB can store records in JSON-like
documents.

Example:

``` json
{
  "name": "Alex",
  "age": 21,
  "skills": ["HTML", "CSS", "JavaScript"]
}
```

Examples of NoSQL database systems include MongoDB, Redis, and
Cassandra. They have different data models and are designed for
different needs.

### SQL vs. NoSQL comparison

  -----------------------------------------------------------------------
  SQL / Relational                    NoSQL
  ----------------------------------- -----------------------------------
  Often stores data in related tables Uses models such as documents,
                                      key-value pairs, or wide-column
                                      records

  Uses SQL in common relational       Query methods depend on the
  systems                             database

  Often uses schemas and constraints  Schema flexibility varies by
                                      database

  Good for structured relational data Can be useful for particular data
                                      and scaling patterns
  -----------------------------------------------------------------------

### Which should you learn first?

Learning SQL is highly useful for backend development. It teaches you
how to:

-   Store information.
-   Retrieve information.
-   Filter records.
-   Update and delete records.
-   Connect related tables.
-   Use constraints and transactions.

You do not need to master every database technology before building your
first application. Start with one database and learn its fundamentals
properly.

------------------------------------------------------------------------

# Chapter 4: Hosting and Scaling a Backend

**Transcript timestamps: 3:15--4:36**

The video moves from writing backend code to making the application
available on the Internet.

It explains that developers can rent computing resources from cloud
providers. At first, the backend and database might run on the same
machine. As usage increases, the system may need more resources.

The video introduces:

-   Vertical scaling.
-   Horizontal scaling.
-   Load balancing.
-   Automatic scaling.
-   Stateless backend design.
-   Microservices.

## What is hosting?

Writing an application on your laptop does not automatically make it
available to everyone on the Internet.

**Hosting** means running your application on infrastructure where users
or other systems can access it.

A hosted application might run on:

-   A physical server.
-   A virtual machine.
-   A container.
-   A managed application platform.
-   A serverless platform.

A cloud provider supplies computing infrastructure and related services.

## Vertical scaling

Vertical scaling means increasing the resources of one computer.

For example:

-   More CPU capacity.
-   More RAM.
-   Faster storage.

Imagine your application running on a machine with 2 CPU cores and 4 GB
RAM. You move it to a machine with 8 CPU cores and 16 GB RAM.

That is vertical scaling.

**Limitation:** A single machine has practical limits. It can only be
upgraded so far, and it may remain a single point of failure.

## Horizontal scaling

Horizontal scaling means adding more machines or instances to share the
workload.

For example:

Instead of running one backend instance, you run three:

``` text
             Incoming Requests
                     |
                     v
               Load Balancer
                /    |    \
               v     v     v
           Server 1 Server 2 Server 3
```

This allows the system to handle more requests by distributing work
across multiple instances.

## What is a load balancer?

A load balancer distributes incoming requests across available backend
instances.

Its goals can include:

-   Distributing traffic.
-   Avoiding overload on one instance.
-   Checking whether instances are healthy.
-   Improving availability.

For example, if three backend instances are available, the load balancer
can send requests to different instances according to its configured
algorithm and health information.

A load balancer is software or infrastructure; it does not have to be a
separate tiny physical computer.

## Auto-scaling

Auto-scaling means automatically increasing or decreasing the number of
running instances based on configured conditions.

For example:

-   Traffic increases → add instances.
-   Traffic decreases → remove unnecessary instances.

Auto-scaling can help control costs while maintaining enough capacity to
serve users.

It requires suitable monitoring, configuration, and capacity limits.

## Stateless backend architecture

The video introduces an important concept: **statelessness**.

A stateless backend instance does not rely on its own local memory to
remember the previous request from a particular user.

Imagine a user sends one request to Server 1 and the next request to
Server 3.

If the application needs information from the previous request, that
information must be available through an appropriate shared or external
mechanism.

Common examples include:

-   A database.
-   A shared cache such as Redis.
-   A session store.
-   A signed authentication token.

### Why is statelessness useful?

It makes it easier to distribute requests across multiple backend
instances.

However, stateless does not mean that the application stores no data.

A stateless backend can still use databases and shared storage. It
simply avoids depending on one particular instance's private local state
for continuity between requests.

## Microservices architecture

The video then introduces microservices.

A microservices architecture divides an application into smaller,
independently deployable services.

For example:

``` text
             Frontend
                 |
           API Gateway
           /     |      \
          v      v       v
      User     Payment  Messaging
     Service   Service   Service
          \      |       /
           \     |      /
             Databases
```

A real design may use separate databases, shared infrastructure, queues,
or other communication mechanisms.

Each service focuses on a particular responsibility.

Examples:

-   User service: manages accounts and profiles.
-   Payment service: handles payment-related operations.
-   Messaging service: manages messages and notifications.

### Why use microservices?

Potential advantages:

-   Services can be scaled independently.
-   Teams can work on different services.
-   Different technologies can be used where justified.
-   One service can be deployed without redeploying the entire
    application.

### What are the disadvantages?

Microservices also introduce complexity:

-   Services must communicate over networks.
-   Debugging becomes more difficult.
-   Monitoring and deployment require more infrastructure.
-   Data consistency across services can be challenging.
-   Network failures and timeouts must be handled.

**Important:** Microservices are not automatically better than a single
application. A well-designed monolith is often a better starting point
for a small project.

## Monolith vs. Microservices

  -----------------------------------------------------------------------
  Monolithic application              Microservices
  ----------------------------------- -----------------------------------
  Main application is developed and   Application is divided into
  deployed as one unit                independently deployable services

  Usually simpler to start            Requires more infrastructure and
                                      coordination

  Internal function calls are common  Network communication between
                                      services is common

  Can be scaled as a whole            Services can be scaled
                                      independently
  -----------------------------------------------------------------------

For a beginner project, start with a simple backend application. Learn
how it works before introducing distributed architecture.

------------------------------------------------------------------------

# Chapter 5: The Boot.dev Sponsor Segment

**Transcript timestamps: 4:36--5:26**

This section is a sponsored promotion for a programming-learning
platform.

The speaker discusses gamified learning features such as:

-   XP and levels.
-   Quests.
-   Coding challenges.
-   Practical exercises.
-   Infrastructure automation.

The speaker also argues that understanding code remains important even
when AI tools can generate code.

## Technical lesson from this section

The useful learning principle is that programming requires more than
producing code.

A capable developer needs to understand:

1.  What the code does.
2.  Why the code is structured in a particular way.
3.  How to debug it.
4.  How to test it.
5.  How different components communicate.
6.  How to design systems that remain maintainable.

AI tools can assist with coding, but understanding the underlying
concepts helps you evaluate their output and identify mistakes.

The platform promotion and discount are advertising, not core backend
concepts.

------------------------------------------------------------------------

# The Complete Backend Request Journey

Let's connect all the chapters into one practical example.

Imagine a user clicks **Create Profile** in a browser.

## Step-by-step process

1.  **Frontend:** JavaScript collects the information entered by the
    user.
2.  **HTTP request:** The browser sends a `POST` request to
    `/api/profiles`.
3.  **Backend server:** The backend application receives the request.
4.  **Controller:** The controller matches the request to the correct
    endpoint.
5.  **Validation:** The application checks whether the supplied data is
    valid.
6.  **Service:** The service layer applies the application's business
    rules.
7.  **Data access:** The data access layer sends the required database
    operation.
8.  **Database:** The database stores the new profile.
9.  **Response:** The backend returns an HTTP response, commonly with a
    status code and JSON data.
10. **Frontend:** JavaScript processes the response and updates the
    page.

The complete flow:

`<escape>`{=html}`text User clicks "Create Profile"             |             v        Frontend             |             v       HTTP POST Request             |             v      Backend Controller             |             v       Service Layer             |             v      Data Access Layer             |             v          Database             |             v        HTTP Response             |             v        Frontend Update``</escape>`{=html}

------------------------------------------------------------------------

# Important Backend Vocabulary

  -----------------------------------------------------------------------
  Term                                Meaning
  ----------------------------------- -----------------------------------
  Frontend                            The user-facing part of an
                                      application

  Backend                             The server-side part that processes
                                      requests and application logic

  Server                              A system that provides a service to
                                      clients

  Framework                           A reusable structure and set of
                                      tools for building software

  API                                 An interface through which software
                                      components communicate

  Endpoint                            A particular API address and
                                      operation

  HTTP                                A protocol used for web
                                      communication

  HTTP method                         Describes the intended action of an
                                      HTTP request

  CRUD                                Create, Read, Update, Delete

  JSON                                A text format for exchanging
                                      structured data

  Controller                          Handles incoming requests and
                                      routes them to application logic

  Service layer                       Contains business rules and
                                      application logic

  Data access layer                   Handles interaction with stored
                                      data

  Database                            A system for storing and retrieving
                                      information

  SQL                                 A language commonly used with
                                      relational databases

  NoSQL                               A broad category of non-relational
                                      database models

  Hosting                             Running an application on
                                      infrastructure where it can be
                                      accessed

  Vertical scaling                    Increasing the resources of one
                                      machine

  Horizontal scaling                  Adding more machines or instances

  Load balancer                       Distributes incoming traffic across
                                      available instances

  Stateless                           Does not depend on one instance's
                                      local memory to maintain request
                                      continuity

  Microservices                       An architecture made of smaller,
                                      independently deployable services
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# How This Connects to Your JavaScript Learning

You can understand backend development as an extension of the JavaScript
you already use in the browser.

JavaScript has two important environments:

## 1. Browser JavaScript

This is JavaScript running in the browser.

It can:

-   Respond to button clicks.
-   Read form inputs.
-   Change HTML content.
-   Send HTTP requests using `fetch()`.
-   Display data received from a backend.

Example:

``` javascript
async function getProfiles() {
  const response = await fetch("/api/profiles");

  if (!response.ok) {
    throw new Error("Could not fetch profiles");
  }

  const profiles = await response.json();

  console.log(profiles);
}
```

## 2. Server-side JavaScript

Using Node.js, JavaScript can also run outside the browser.

It can:

-   Receive HTTP requests.
-   Process data.
-   Apply business rules.
-   Communicate with databases.
-   Return responses.

A backend framework such as Express.js makes it easier to build HTTP
APIs.

Example:

``` javascript
const express = require("express");

const app = express();

app.use(express.json());

app.get("/api/profiles", (req, res) => {
  res.json([
    { id: 1, name: "Alex" },
    { id: 2, name: "Sam" }
  ]);
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
```

This is a small demonstration. It returns hard-coded data rather than
reading from a database.

------------------------------------------------------------------------

# Suggested Learning Order

Do not try to learn every backend technology mentioned in the video
simultaneously.

A sensible learning sequence is:

1.  **JavaScript fundamentals:** variables, functions, arrays, objects,
    loops, modules, promises, and `async/await`.
2.  **HTTP fundamentals:** requests, responses, methods, headers, status
    codes, and JSON.
3.  **Node.js:** understand how JavaScript runs outside the browser.
4.  **Express.js:** build routes and HTTP endpoints.
5.  **REST API fundamentals:** organize endpoints around resources.
6.  **SQL:** learn tables, queries, relationships, joins, and
    constraints.
7.  **Database integration:** connect your backend to a database.
8.  **Authentication and authorization:** understand how applications
    identify users and control access.
9.  **Deployment:** learn how to host your application.
10. **Advanced architecture:** explore caching, load balancing, and
    microservices when you have a reason to use them.

------------------------------------------------------------------------

# Check Your Understanding

Try answering these questions without looking at the explanations.

1.  What is the difference between frontend and backend?
2.  What is an API?
3.  What is an endpoint?
4.  What does CRUD stand for?
5.  What is the difference between `GET` and `POST`?
6.  What is JSON used for?
7.  What are the responsibilities of a controller?
8.  What is the purpose of the service layer?
9.  What does the data access layer do?
10. What is the difference between SQL and NoSQL?
11. What is vertical scaling?
12. What is horizontal scaling?
13. What does a load balancer do?
14. What does stateless backend architecture mean?
15. What is a microservices architecture?
16. Why might a monolithic application be a better starting point for a
    beginner?

## Short Answers

1.  Frontend handles the user-facing interface; backend handles
    server-side processing and application logic.
2.  An interface that allows software components to communicate.
3.  A particular address and operation exposed by an API.
4.  Create, Read, Update, Delete.
5.  `GET` retrieves data; `POST` commonly submits data or creates a
    resource.
6.  To exchange structured data between systems.
7.  Receive requests, match routes, and coordinate responses.
8.  To implement application and business rules.
9.  To interact with the database or other data stores.
10. SQL commonly works with relational tables; NoSQL covers several
    other data models.
11. Increasing the resources of one machine.
12. Adding more machines or instances.
13. Distributing requests across available backend instances.
14. Backend instances do not rely on their own local memory to remember
    previous requests.
15. An architecture made of smaller, independently deployable services.
16. It is generally simpler to build, test, deploy, and understand.

------------------------------------------------------------------------

# Final Summary

Backend development is about building the server-side systems that power
applications.

The frontend sends requests to backend API endpoints. The backend
processes those requests, applies business logic, communicates with
databases, and returns responses.

A common backend structure separates responsibilities into controllers,
services, and data access layers. Databases store application data.
Hosting makes the application accessible over the Internet, while
scaling techniques help it handle increasing traffic.

**The central idea to remember:**

The frontend is how users interact with an application. The backend is
where the application processes requests, applies rules, and manages
data.

Start with a small backend, understand the request-response cycle,
connect a database, and build from there. You do not need microservices
or a complex cloud architecture to build your first full-stack
application.
