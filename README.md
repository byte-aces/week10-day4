# NewCo

A cryptocurrency exchange.

---

# Notes

**Naming convention for tags**

_namespace:predicate=value_

Examples:
- #basename:key=value
- #index.html:priority=high
- #404.html:priority=low

---

# Successes

	_pass_

---

# Obstacles

	_pass_

---

# Next Steps

## 1. Discovery
### a. Buyer Persona
I.   Primary
		- Alice (customer)
II.  Secondary
		- Eve (cracker)
III. Tertiary
		- Jabberwocky (competitor)
### b. User Stories
I.   Customer
    - Alice visits NewCo's frontpage.        #index.html     :priority=high
    - Alice creates an account.              #register.html  :priority=high
    - Alice reviews market conditions.       #dashboard.html :priority=high
    - Alice logs out of her account.         #\*.html        :priority=high
    - Alice logs into her account.           #login.html     :priority=high
    - Alice deposits funds into her account. #account.html   :priority=high
    - Alice buys an asset.                   #dashboard.html :priority=high
    - Alice sells an asset.                  #dashboard.html :priority=high
    - Alice checks her profit-and-loss.      #dashboard.html :priority=high
II.  Cracker
    - Eve mounts an attack on Alice.         #login.html     :priority=low
III. Competitor
		- Jabberwocky visits NewCo's frontpage.  #index.html     :priority=high

## 2. Design
### a. Wireframes
_see `doc/`_
### b. Storyboard (i.e., map Wireframes to User Stories)
_pass_

## 3. Development
### a. FIXMES (e.g., short term)
`registration.html`
--> Introduce registration functionality
--> Define a schema for the database
--> Create a PostgreSQL database
--> Create user table in the database
--> Seed user table in the database
--> Connect the user table to the registration model
`login.html`
--> Introduce log-in functionality
--> Connect the user table to the login model
`dashboard.html`
--> Download source code from Bootstrap
--> Re-factor source code
--> --> Swap out links to local directories with links to Bootstrap
--> Integrate source code with structure.html
--> Animate charts and tables with our data
`account.html`
--> Download source code from Bootstrap
--> Re-factor source code
--> --> Swap out links to local directories with links to Bootstrap
--> Integrate source code with structure.html
### b. TODOS (e.g., long term)
`404.html`
--> Come up with something funny to serve
--> Integrate source code with structure.html
`register.html`
--> Use JavaScript to confirm that the passwords match.

## 4. Deployment
### a. Monolithic (i.e., reference implementation)
### b. Microservice Reference Architecture

## 5. Documentation
### a. supra
`README.md`
### b. infra
`404.html`
