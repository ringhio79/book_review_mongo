# For the Love of books

This web application is born out of the desire to share book recommendations with friends and family overseas. It allows a user to scroll through the current book titles and authors, add reviews and add additional books and authors if necessary. 

## Live Link 
The web app has been deployed on Heroku and may be accessed at [For the Love of Books](https://fortheloveofbooks.herokuapp.com/)

## UX
 
The navigation of this app is designed with simplicity in mind. It should be easy enough for an inexperienced user to navigate through without any issues.

- Browsing Books: Users may browse through the book list cards.  Each book card title links to the full details of the book which  turn allows the user to add a review for that book. A back button allows the user to return to the book details.  Alternatively the navbar item can be used to return to the main booklist.

- Browsing Authors: Similar to the books, users can navigate through the author thumbnails. When clicking on an author's name the user will be taken to a new page with the author details and a list of books by that author.  The book titles in turn link to the book details. The user can then return to the author's page by clicking on the authors name or navigate to any other page through the navbar links.

## Featurs
- Adding Books & Authors: There are dedicated pages to add books or authors.  The user may fill in the online form with the relevant information. The image field is not required as it may difficult for a user to locate an online image.  If no image is added then a default image will be used to the display when necessary.

- Adding a review: Users can add reviews to any book.  Given the restrictions imposed by not having any login feature there are no options to edit reviews but only to add.

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

### Database
- [MongoDB](https://www.mongodb.com/)
    - storing data in the cloud and use the same database in prod and dev environments.

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

This project is deployed and hosted on Heroku which is linked to cloud-based MongoDB database. The process followed is detailed below:

1. Create procfile in the root directory 

2. Install gunicorn by running $ sudo pip3 install gunicorn

3. Create requirements.txt Run command $ pip3 freeze --local > requirements.txt

4. Create a new app on Heroku.

5. Add the config settings for Heroku to connect to the MongoDB

6. Connect Heroku to GitHub repository and hit deploy


## Credits

## Author
This web app was created by Giselle Baldacchino as the final project for the Code Institute Fullstack Developer bootcamp.

### Content
- Information on the books and the authors was taken from https://www.goodreads.com/

### Media
- Other images are taken from https://www.pexels.com/


### Acknowledgements
- Thanks to the teachers and mentors at Code Institute for their constant support and patience throughout this course.
- Thanks to my sister for inspiring me to create this app so we can share our reading experiences even when we are apart.