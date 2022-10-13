# Release Notes

### Modules

The project was developed on top of 5 modules:

#### Core

The core module contains all the models, so any other module can access them. It also contains the custom model manager used on User model, so to adapt it on the changes made on top of the default user model.


#### News Details

This module is responsible for rendering the individual page for each news.


#### News Listing

This module is responsible for rendering the home page, which shows all the published news and a preview of their content. Also it paginates the list of news if it has more than 10 items.


#### Post Creation

This module is resposible for rendering the form to make new posts, or redirect unauthorized users to the login form.


#### Authentication

This module is resposible for rendering the page for users to log in and for logging out.


### User model

The username was changed to an e-mail field, since the username wouldn't be necessary, the e-mail is easier to remember and I already would use it to notify the staff members when a new post was made.


### Generic Views

I've enjoyed the build-in generic views from Django, so that I could deliver maximum value inside the 6 hours limit.


### Conditional Views

So that I could cache only when a new post was made, I've used the conditional views feature from Django, which allowed me to change the "Last-Modified" header and then combining it with the vary_on_header decorator.


### Layering

Since the application didn't demand many business logic, most of the modules had only presentational features. The ones it did had business logic, a service layer was created to save the presentational layer on processing business logic.


## Features not implemented

* Creation form for new categories
* Automated tests
* CI/CD