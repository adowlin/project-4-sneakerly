<h1 align="center">Sneakerly</h1>

[<img align="center" src="readme-assets/images/sneakerly-mockups.png" alt="responsive site mockups">](https://ms4-sneakerly.herokuapp.com/)

[View the deployed site here.](https://ms4-sneakerly.herokuapp.com/)

Sneakerly is a sneaker rental website that allows users to rent premium sneakers from a reputable source. This website was created for submission as my Milestone Project 4 as part of the Diploma in Full Stack Software Development course with Code Institute.<br>
 
## User Experience (UX)

The sneaker industry is undergoing a period of huge growth, with popular sneakers selling out instantly from retailers, and being re-sold at after-market values much higher than the original retail value.<br>
This site advances the user's goals by allowing users to rent premium sneakers at affordable prices, allowing them to have the full experience of wearing sought-after styles, without needing to pay huge reseller prices, and without needing to compete against automated purchase bots on retailer websites.<br>
It advances the site owner's goals by providing them with a means to make money from rentals, and they will also be allowed to charge customers late/missing/damaged fees.<br>

The User Experience for this site was planned & developed using the [5 Planes of UX Design](https://medium.com/designcentered/ux-design-5-planes-method-b1b1d6587c05): Strategy, Scope, Structure, Skeleton, Surface.

### Strategy
#### User Stories

- **As a first-time visitor, I want to:**
    - Find out how the rental process works.
    - See a directory of products that are available to rent.
    - Register for an account on the site to allow me to rent a product.
    - Rent a product while authenticated.
    - Find answers to common questions I have about the business & products.
    - Contact the site owners with any questions not answered by the site information.
    - See a blog containing photos from regular site users.

- **As a returning visitor, I want to:**
    - Log in to my user profile.
    - See a list of past rentals.
    - See detailed information about past rentals.
    - Save my default delivery information.
    - Update my default delivery information.
    - See my current default delivery information.
    - Pre-fill the delivery information on the checkout page when booking a new rental.
    - Upload photos to the blog of the products in-use during my rental period.

- **As the site owner, I want to:**
    - Manage users, bookings, products, and blog posts.
    - Have superuser access to blog posts to moderate the content.
    - Receive emails to notify me of questions asked via the contact form.
    - Earn money from rentals by charging users up-front.

### Scope
#### Existing Features

- **Navbar with Site Logo:**
    - The navbar & site logo provide a visual design feature with the diagonal shaping. Upon scrolling down the page, the navbar automatically shrinks back to a regular shape. The navbar links provide a means for users to navigate the site.

- **Homepage with Hero Image & Lead Text:**
    - The hero image provides an immediate visual cue to introduce the type of products available on the site. Just below, the lead text describes the purpose of the site.

- **Homepage Instructions Summary:**
    - On the homepage, the main content section provides a brief description of how the site works, giving instructions on how to use the site to users. Accompanied by images and further informational cards further down the page, the user is concisely presented with all the information they need to get started using the site.

- **Registration:**
    - Provides functionality for users to create an account on the site, in order to rent products and access extra functionality on the site, such as adding blog posts. User input is validated, and upon successful registration, a User object is created in the database.

- **Login/Logout:**
    - Provided users who have registered an account to access their profile, and additional features only available to authenticated users.

- **Profile:**
    - Allows authenticated users to see their booking history, if applicable, and provides functionality to update/add their default delivery information via a form. Successful submission of this form creates a UserProfile object in the database. In the booking history, the user can click on the booking numbers to see full details of the rental.

- **Directory of Products:**
    - The "All Sneakers" directory page provides all users with a list of sneakers that are currently available to rent. Laid out in a grid format using cards to include product images, prices, categories, and a "Rent" button.

- **Product Detail Page:**
    - Provides product image & further details, and allows authenticated users to enter their rental start date, number of rental days, and continue to the next step of the booking process.

- **Rental Confirmation Page (Bag):**
    - Displays a summary of the user's booking before continuing to the checkout process. User's can choose to "Cancel" and return to the Product Detail page, or "Confirm" and continue to the Checkout page.

- **Checkout Page:**
    - Displays a summary of the rental details at the top of the page, providing an option for users to return to the Product Detail page once again via the "Adjust Dates" button. Provides users with a checkout form with validation, prefilled with their default delivery information if present. After clicking the "Complete Checkout" button, a full page overlay is displayed to prevent duplication of the payment if the button is clicked more than once.

- **Checkout Success Page:**
    - If the payment is successful, the user is redirected to a Checkout Success page, providing the user with their booking number, and the details of their booking. A booking confirmation email is sent to the user's email address.

- **Blog:**
    - Displays blog posts to all users, and allows authenticated users to add a blog post. When adding a post, the user can upload a photo of the product they have rented. Provides functionality for the superuser to edit and delete blog posts.

- **FAQs Page:**
    - Provides users with a list of answers to frequently asked questions about the site. Information is arranged in an accordian, to allow users to expand the question to see the answers they wish to see.

- **Contact Page:**
    - Allows users to contact the site owner with any questions not answered by information available on the site via a contact form with validation.

#### Future Planned Features

### Structure
#### Flowchart
- Flowchart created using [Lucidchart](https://www.lucidchart.com):<br>
    [Flowchart PNG](/readme-assets/images/sneakerly-flowchart-2.png)

### Skeleton
#### Wireframes
- Wireframes created using [Balsamiq](https://balsamiq.com/):<br>
    [Wireframes PDF](/readme-assets/sneakerly-wireframes2.pdf)

### Surface

- **Color Scheme:**
    - Chosen using [coolors.co](https://coolors.co/). This color palette was chosen to provide sufficient contrasting color options for accessibility purposes, including multiple shades of similar colors. The colors used were chosen to provide a fun, engaging design throughout the site's UI.<br>
    [<img src="readme-assets/images/sneakerly-palette.png" alt="color palette" width="400"/>](https://coolors.co/52489c-ce84ad-b9508a-2b7878-5ac4c4-a6dddd-a3d8d8-ebebeb-f2404f-f45b69)

- Typography:

- Images:

## Technologies Used

### Tools

### Front-End Technologies

### Back-End Technologies

## Testing

## Deployment
### Local Deployment

### Remote Deployment

## Credits

### Content

### Media

### Acknowledgements