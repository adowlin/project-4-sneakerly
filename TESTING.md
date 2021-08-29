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
    - On the Profile page, a form that is pre-filled with the current default information, is available to update default delivery information to the currently logged-in user profile.
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
    - Upon successful submission of the "Contact" page form, an email is sent to the site owner's email address containing details of the submission.
- Earn money from rentals by charging users up-front;
    - The Checkout page collects user's card details at the time of booking, and will not allow users to make bookings without a successful payment.

### Manual Testing
#### All Pages
Manual testing was performed on the following elements that appear across all pages on the site, to ensure that all are working as expected;

- Navbar:
    - Clicking the site logo in the navbar correctly directs back to the site's home page.
    - All navigation links direct the user to the correct site page for each link.
    - Collapsible sidebar button opens the modal navigation element on mobile devices.
    - All navigation links within the mobile modal navigation correctly direct the user to the corresponding site page.
    - Hovering over the navigation links triggers the expected hover effect color & underline.
    - Hovering over the site logo triggers the expected hover effect color.
    - Login & Register navigation links only appear when the user is unauthenticated, and correctly direct to their respective pages.
    - Profile and Logout navigation links correctly appear only when a user is already logged in, and correctly direct to the Profile page, and log the user out, respectively.
    - Navbar diagonal shape correctly shrinks back to a regular rectangle navbar shape when the appropriate scroll position is reached.
- Footer:
    - External links open the correct external site in a new tab.
    - Contact & FAQs links direct to the internal site pages correctly.
    - Hovering over the footer links triggers the expected hover effect color & underline.
- Page Headers:
    - Header images appropriately resize responsively across all device sizes.
    - Where page headers are present over the header images, an opaque overlay correctly covers the image, and header text appropriately re-sized across all device sizes.

#### Home Page
Manual testing was performed on the following elements that appear on the Home page;

- Buttons:
    - The "Create an Account" buttons only appear when the user is unauthenticated, and correctly direct to the registration page.
    - The "Go to Profile" buttons correctly replace the "Create an Account" buttons only when the user is authenticated, and correctly direct to the profile page.
    - The "See All Sneakers" button correctly directs to the products page.
    - The bottom "Create an Account"/"Go to Profile" and "See All Sneakers" buttons correctly re-position from a full-width row each to two columns in a single row on larger screens.
- Info Cards:
    - The information cards correctly re-position from a full-width row each to two columns in a single row on larger screens.

#### Register Page
Manual testing was performed on the following elements that appear on the Register page;

- Form:
    - Input fields validate the input data as expected.
    - The form submission button correctly creates a User in the database, and directs the user to the email confirmation page as expected.
    - The "sign in" link correctly redirects to the "Log In" page.

- Defensive programming works as expected - an authenticated user who tries to brute-force access the Register page is redirected back to the home page.

#### Log In Page
Manual testing was performed on the following elements that appear on the Log In page;

- Form:
    - Input fields validate the input data as expected.
    - The form submission button correctly logs the user in and redirects to the home page.
    - The "sign up" link correctly redirects to the "Register" page.

- Defensive programming works as expected - an authenticated user who tries to brute-force access the Log In page is redirected back to the home page.

#### Log Out Page
Manual testing was performed on the following elements that appear on the Log Out page;

- Button:
    - The "Sign Out" correctly signs the user out of the session, and redirects back to the home page.

- Defensive programming works as expected - an unauthenticated user who tries to brute-force access the Log Out page is redirected back to the login page.

#### Profile Page
Manual testing was performed on the following elements that appear on the Profile page;

- Booking History:
    - The table correctly appears only when the user has bookings attached to their user profile, and displays informative text if no bookings are attached.
    - The table data displays the appropriate booking object information.
    - Clicking the booking number directs to the booking details page as expected.
    - The booking history details page displays the correct information for the specified booking.
    - The booking history page displays a toast message notification stating the information relates to a past booking, as expected.

- Default Delivery Info Form:
    - Input fields validate the input data as expected.
    - The form is blank where the user does not yet have delivery information saved, and pre-fills the form fields with their default delivery information if the information is present.
    - The form submission button correctly adds or updates the user profile's default delivery information.

- Defensive programming works as expected - an unauthenticated user who tries to brute-force access the Profile page is redirected back to the login page.

#### All Sneakers (Products) Page
Manual testing was performed on the following elements that appear on the Products page;

- Product Cards:
    - Product data is correctly iterated over to create a card for each product.
    - Cards correctly re-position themselves from full-width on smaller screens to a grid layout on larger screens.
    - The "Rent" buttons on each card direct to the appropriate product detail page for each product.

#### Product Detail Pages
Manual testing was performed on the following elements that appear on the Product Detail pages;

- Product Info:
    - The correct product information & image is displayed for the specified product.

- Rental Date Selection Form:
    - The date input field correctly allows the user to select a start date for their rental.
    - The field does not, however, save the selected start date to attach it to the booking later on. See [Known Issues](#known-issues) for more detail.
    - The Rental Days input field allows the user to enter their desired number of rental days, with validation, as expected.
    - The "Rent" button correctly passes the rental days to the Bag view, and redirects to the "Confirm Booking" (Bag) page.
    - The form fields are disabled when an unauthenticated user visits the page, as expected.
    - The "Rent" button is replaced by information text when an unauthenticated user visits the page, as expected.

#### Confirm Booking (Bag) Page
Manual testing was performed on the following elements that appear on the Confirm Booking page;

- Buttons:
    - The "Cancel" button correctly directs the user back to the Product Detail page.
    - The "Confirm" button correctly directs the user to the Checkout page.

- Defensive programming works as expected - an unauthenticated user who tries to brute-force access the Bag page is redirected back to the login page.

#### Checkout Page
Manual testing was performed on the following elements that appear on the Checkout page;

- On loading the page, a Stripe PaymentIntent for the total price is correctly created.

- Booking Summary:
    - The information displayed is correct for the specified product.
    - The total price displayed is correctly calculated & displayed from the product price and rental days.
    - The "Adjust Dates" button correctly re-directs the user back to the Product Detail page.

- Checkout Form:
    - Input fields validate the input data as expected.
    - The form is blank where the user does not yet have delivery information saved, and pre-fills the form fields with their default delivery information if the information is present.
    - The form submission button correctly adds or updates the user profile's default delivery information.
    - On successfully submitting the form, a payment is created in Stripe as expected.
    - If a card requiring authentication is used, the Stripe authentication modal is displayed as expected.
    - The full-screen loading overlay correctly displays when the form is submitted.
    - The form provides dynamic feedback for card errors where the payment is not successful.

- Defensive programming works as expected - an unauthenticated user who tries to brute-force access the Checkout page is redirected back to the products page, with a toast message populated to let the user know that they cannot checkout.

#### Checkout Success Page
Manual testing was performed on the following elements that appear on the Checkout Success page;

- Summary:
    - The page displays the correct booking information for the specified booking number.

- Email:
    - The checkout success page's view correctly sends a confirmation email to the user's email address.

- Defensive programming works as expected - an unauthenticated user who tries to brute-force access the Checkout Success page is redirected back to the login page.

#### Blog Page
Manual testing was performed on the following elements that appear on the Blog page;

- Cards:
    - Blog Post data is correctly iterated through to create a card for each blog post.
    - The card for each post correctly displays the uploaded image, product name, and username of the user who created the post.

- Buttons:
    - The "Add Post" button only appears for authenticated users, as expected.
    - The Edit & Delete icon buttons only appear for the authenticated superuser, and correctly direct to the Edit Post page, and action the Delete Post functionality respectively.

- Defensive programming works as expected - an unauthenticated user who tries to brute-force access the Add/Edit/Delete Blog Post URL is redirected back to the login page. A non-superuser who tries to brute-force access to the Edit or Delete Blog Post URL is redirected back to the Blog page, with a toast message populated indicating that only admins can access those pages.

#### FAQs & Contact Pages
Manual testing was performed on the following elements that appear on the FAQs & Contact pages;

- FAQs:
    - Accordion correctly collapses each question when clicked to display the answer.

- Contact Form:
    - Form inputs are validated as expected.
    - On submission, an email is sent to the account owner as expected.
    - After submission, the page reloads with a toast message confirming that the message has been sent, as expected.

### Compatibility & Responsiveness
The final site was tested across multiple browsers and device types, with no cross-browser compatibility issues to note.

- Browsers tested:
    - Chrome (Windows, macOS, iOS, Android)
    - Safari (macOS, iOS)
    - Microsoft Edge (Windows, macOS)
    - Firefox (Windows, macOS)
    - Samsung Browser (Android)
- Devices tested:
    - iPhone XS
    - Samsung Galaxy Edge
    - Desktop PC
    - Laptop
    - Tablet

The site was found to be fully responsive on device sizes ranging from 320px X 480px to 1920px X 1080px.

### Bugs Found & Fixed
During compatibility testing on iOS devices, the background images that had the `background-attachment:fixed` property set were not correctly centered - instead only the top-left corner of the images were visible.
    - This was due to the `fixed` value for `background-attachment` not being supported by iOS.
    - A similar bug was found in a previous project, so the same fix of using `background-attachment:scroll` was used. Ref: https://github.com/adowlin/project-1-dungeons-dragons#bugs-found--fixed

### Known Issues
During development & testing, I was unable to get functionality working that would record the rental start dates from the date picker form inputs on either the Product Detail page, or the Checkout page.
    - In the interest of demonstrating the future functionality of the data-pickers, they were kept in the final product, but their inputs are not posted to any of the app views.

### Validation
#### HTML
- [W3C HTML Validator](https://validator.w3.org/nu/) was used to validate the HTML code on all 29 HTML templates in the app. This validator does not recognise Django templating, so returns quite a few expected, all related to Django Template scripting & variables. No errors are present in the HTML code otherwise.

#### CSS
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS code in the 5 CSS files present in the app. A couple of expected errors & warnings are returned when validating the `base.css` file.

- Error:
    - Property `backdrop-filter` doesn't exist : `blur(16px) saturate(180%)`
        - `backdrop-filter` is not yet recognized by the CSS validator, despite not being a very new property. It is not yet supported by Firefox, but the default background blur on the modal where this property is used is sufficient. For design purposes, the property was kept in the code to provide the desired glass-morphism effect on the modal in other browsers.
        - Ref: https://github.com/w3c/css-validator/issues/289

- Warnings:
    - `-webkit-text-stroke` is an unknown vendor extension
    - `-webkit-backdrop-filter` is an unknown vendor extension

- All other CSS code is valid.

#### JavaScript
- [JSHint](https://jshint.com/) was used to validate the JavaScript code in the script.js and stripe_elements.js files. No errors are present.
- [Esprima](https://esprima.org/demo/validate.html) was also used to validate the JavaScript syntax. Returned result: "Code is syntactically valid".

#### Python
- [PEP8 Online](http://pep8online.com/) was used to validate the Python code in the 37 .py files.
- Expected errors were returned for the `settings.py` file:
    - `line too long (>79 characters)` in the `AUTH_PASSWORD_VALIDATORS = [{}]` settings x4
    - This is a known issue with the built-in Django settings, and it would not be acceptable to force a line break in the dictionary value strings.
- Another expected error is returned for the Blog app's `widgets.py` file:
    - `line too long (>79 characters)` on line 9.
    - It would not be acceptable to force a line break in the filepath string as doing so breaks the "Add Blog Post" and "Edit Blog Post" pages.

- All other Python code is fully PEP8 compliant.

