<h1 align="center">Sneakerly Testing</h1>

[View the deployed site.](https://ms4-sneakerly.herokuapp.com/)

Main [README.md](README.md) file<br>
[Project Repository](https://github.com/adowlin/project-4-sneakerly)

## Testing
### Testing User Stories from User Experience (UX) Section

**As a first-time visitor, I want to;**
- Find out how the rental process works;
    - On the site's home page, a summary of how the process of renting works is immediately visible.
    - Scrolling down the homepage, further information about cleaning and returns are shown.
    - In the site's navbar and footer, a link to the FAQs page is visible.
    - On the FAQs page, answers to frequently asked questions about the site can be found easily.
- See a directory of products that are available to rent;
    - On the site's home page, an "All Sneakers" button is found underneath the rental process information.
    - In the site's navbar, a link to the "All Sneakers" page is immediately visible.
    - On the "All Sneakers" page, cards containing images and information about the available products are found.
- Register for an account on the site to allow me to rent a product;
    - On the home page, multiple "Create an Account" buttons are visible, and in the navbar a "Register" link is immediately visible.
    - From the "Registration" page, a form is presented in order to create an account on the site, by providing an email address, username, and password. 
    - After creating an account, a confirmation email is sent, and after confirming the email address, the site redirects to the sign in page.
- Rent a product while authenticated;
    - After signing in, the form fields on the "Product Detail" page are enabled, and the "Rent" button becomes visible.
    - Clicking through the rental confirmation page, the Checkout page is enabled to allow delivery and payment details to be provided.
    - After successful payment, the "Checkout Success" page shows the booking confirmation number, and details of the booking.
- Find answers to common questions I have about the business & products;
    - In the site's navbar and footer, a link to the FAQs page is visible.
    - On the FAQs page, answers to frequently asked questions about the site can be found easily.
- Contact the site owners with any questions not answered by the site information;
    - In the site's navbar and footer, a link to the contact page is easily visible.
    - On the "Contact" page, a form is available, and when submitted, presents a confirmation message that the message has been sent.
- See a blog containing photos from regular site users;
    - In the site's navbar, a link to the site's "Blog" page is immediately visible.
    - On the "Blog" page, when unauthenticated, posts from other site users can be found.

**As a returning visitor, I want to:**
- Log in to my user profile;
    - In the site's navbar, a link to the "Log In" page is immediately visible.
    - On the site's product detail page, a prompt to sign in is shown in order to continue with the booking process.
    - From the "Log In" page, a form is available to sign in using an existing username and password.
- See a list of past rentals;
    - When authenticated, the "Profile" link is visible in the site's navbar.
    - On the "Profile" page, a table containing past rentals is visible, if any past rentals exist on the user profile.
- See detailed information about past rentals;
    - From the "Rental History" section of the Profile page, clicking on a booking number will load the full booking details for that rental.
- Save my default delivery information;
    - On the Profile page, a form is available to save default delivery information to the currently logged-in user profile.
    - On the Checkout page, the delivery information entered is automatically saved to the current user's profile.
- Update my default delivery information;
    - On the Profile page, a form, that is pre-filled with the current default information, is available to update default delivery information to the currently logged-in user profile.
- See my current default delivery information;
    - On the Profile page, the form is pre-filled with the current default delivery information.
- Pre-fill the delivery information on the checkout page when booking a new rental;
    - On the Checkout page, the form is pre-filled with the current profile's default delivery information. If new delivery information is entered, it is automatically saved to the current user's profile.
- Upload photos to the blog of the products in-use during my rental period;
    - A link to the "Blog" page is visible to all site users in the site's navbar.
    - When authenticated, on the "Blog" page, the "Add Post" button is visible.
    - Clicking the "Add Post" button directs to the "Add Blog Post" page. This page presents a form to collect the product, title, and an image for the blog post. On submission of the form, the post appears on the main "Blog" page.

**As the site owner, I want to:**
- Manage users, bookings, products, and blog posts;
    - Navigating to the site's URL with "/admin/" appended, a login form is available. Logging in with superuser credentials allows access to the site's admin interface, where users, bookings, products, blog_posts, and all site objects can be modified or deleted.
- Have superuser access to blog posts to moderate the content;
    - When authenticated as a superuser, on the "Blog" page, edit and delete icons are visible on all blog posts'
    - The "edit blog post" button directs to the "Edit Blog Post" page, where the post's details can be edited and saved.
    - The "delete blog post" icon button deletes the blog post.
- Receive emails to notify me of questions asked via the contact form;
    - Upon successful submission of the "Contact" page form, and email is sent to the site owner's email address containing details of the submission.
- Earn money from rentals by charging users up-front;
    - The Checkout page collects user's card details at the time of booking, and will not allow user's to make bookings without a successful payment.

### Manual Testing


### Compatibility & Responsiveness


### Validation
