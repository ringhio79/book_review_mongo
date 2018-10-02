# For the Love of books

This web application is born out of the desire to share book recommendations with friends and family overseas. It allows a user to scroll through the current book titles and authors, add reviews and add additional books and authors if necessary. 

## UX
 
The navigation of this app is designed with simplicity in mind. It should be easy enough for an inexperienced user to navigate through without any issues.

- Browsing Books: Users may browse through the book list cards.  Each book card title links to the full details of the book which  turn allows the user to add a review for that book. A back button allows the user to return to the book details.  Alternatively the navbar item can be used to return to the main booklist.

- Browsing Authors: Similar to the books, users can navigate through the author thumbnails. When clicking on an author's name the user will be taken to a new page with the author details and a list of books by that author.  The book titles in turn link to the book details. The user can then return to the author's page by clicking on the authors name or navigate to any other page through the navbar links.

- Adding Books & Authors: There are dedicated pages to add books or authors.  The user may fill in the online form with the relevant information. The image field is not required as it may difficult for a user to locate an online image.  If no image is added then a default image will be added to the display when necessary.


## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.

## Technologies Used

### Frameworks
- [Flask Web Framework](http://flask.pocoo.org/)
    - to creating the base web framework, template
- [Materialize](http://flask.pocoo.org/)
    - to create additional layout and styling features as well as responsiveness

### Languages
- [Python3](https://www.python.org/)
    - to create functionality, render templates write to database
- HTML & CSS
    - to create layout and styling of front end

### Databases
- [MongoDB](https://www.mongodb.com/)
    - to store data in the cloud and use the same database in prod and dev environments.

## Testing

This app has been manually tested for functionality and layout on different screens sizes.

**Display**
    The application views have been tested on mobile as well as desktop devices
    Due to the narrow viewing area on mobile devices, the image in the book cards is hidden
    
**Forms**
    Form input fields have been tested for required fields
    Errors are show for missing information on required fields
    Reset button reloads the page with empty form
    
    
## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X