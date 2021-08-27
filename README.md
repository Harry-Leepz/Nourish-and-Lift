# **Nourish and Lift**

[Live Site](https://nourish-and-lift.herokuapp.com/)

![Responsive view of Nourish and Lift on all devices](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/images/project-image.png "Nourish and Lift")


## **Introduction**
Welcome to Nourish and Lift.

Nourish and Lift is my fourth and final project, part of the Code Institute, Full Stack Web Developer Course.

The purpose of this project was a build a full-stack site based around a business logic used to control a centrally-owned dataset. The technologies used for this project are HTML, CSS, JavaScript, Python, and Django. Stripe handles online test payments and Heroku Postgres as a relational database.

Nourish and Lift is a fictional brand, purchases on this project are accepted via Stripes test card details. For further information on which card number you should use, please refer to Stripe's official documentation.

[Stripe Test Integration](https://stripe.com/docs/testing)

This project is for educational purposes only, No commercial revenue is generated from this project.

---

## **UXD - User Experience Design**

A large part of inspiration behind the planning for this project came from Jason James Garretts’s, “The Elements of User-Experience”. By keeping the user in mind throughout the design and development of the project, it would be easier to make the user experience a positive one. For the user to have a positive emotional response throughout the project.

The planning of the project is broken into 5 planes,

- The Strategy Plane
- The Scope Plane
- The Structure Plane
- The Skeleton Plane
- The Surface Plane
---

## **The Strategy Plane**

### **Creator Goals**
- As a creator, I wasnt the site to be easy to navigate.
- As a creator, I want user to be able to filter through products, either by name, price.
- As a creator, I want to provide users with updates to any actions.
- As a creator, I want to allows admins to Add/Edit/Delete products to/from the store.

### **User Stories**

#### **Regular Site User Stories**
- As a site user, I want the main purpose of the site to be clear, so that I can determine if this the correct 
site for me.
- As a site user, I want to be able to navigate across the site, so that I can view different pages on the site. 
- As a site user, I want to be able to sign up, so that I can have a personal account on the site.
- As a site user, I want to be able to receive an email confirmation after registering, so that I can verify 
that my account registration was successful.

#### **Customer Shopper Stories**
- As a shopper, I want to be to view all products, so that I can decide what I want to buy.
- As a shopper, I want to be able to view products in more detail.
- As a shopper, I want to be able to view reviews left by other customers for products, so that I can understand whether the product is worth purchasing. 
- As a shopper, I want to be able to see a confirmation when a product is added to my shopping bag, so that I can avoid accidentally adding multiple quantities of the same item. 
- As a shopper, I want to be able to view my bag, so that I can see what is in my bag and adjust quantities

#### **Customers (Logged in) Stories**
- As a logged in user, I want to be able to save my details, so that I can avoid retyping my details again.
- As a logged in user, I want to have my past orders viewable, so that I can verify what my past order was and view the order number.
- As a logged in user, I want to be able to leave reviews on product, so that other users may be able to benefit from my opinions on my purchase. 
- As a logged in user, I want to be able to edit my reviews, so that I am able to amend any errors or incase I change my opinion.
- As a logged in user, I want to be able to add products to my wishlist, so that I can view those products later.
- As a logged in user, I was to be able to remove products from my wishlist, so that my wishlist is only full of products I want saved.

My user stories were obtained by doing research into other stores and seeing how their sites ran. Argos in particular helped me to guage what I would need to implement and what potentially could be left out or moved into a phase for later deployment.

---

## **The Scope Plane**

The features that I had thought about before designing the project and my deadline was not achievable. I opted for a phased release approach. 

I was able to ascertain which features were more important and should be working on my initial deployment, and which features I could add later.

My plan for a phased deployment, 

**Phase 1**
- A project that would satisfy my user stories.
    - Home Page with a introduction 
    - Navbar allowing user to navigate to different pages
    - Products page allowing users to view all products. 
    - A product detail page.
    - E-commerce functionality allowing user to make purchases.
**Phase 2**
- Building upon the Phase 1 project with additional features.
    - A funtional blog app that allows admins to to post blogs.
    - Allow users the filter blog types.
    - Allow users to post comments on the blogs.
**Phase 3**
- My final planned phase would focus on user feedback
    - Project feedback, to see if things could be improved.

---

## **The Structure Plane**

#### **Colors**
![Color pallete used through the project](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/images/color-pallete.png "Color Pallete")

#212121
- I used a dark grey for the body color, I have always preferred darkmode and thought it helped the lighter colors stand out, creating a better contrast.

#17A2B8
- The Bootstrap info class colors was used most on horizontal rules, buttons and anchortag elements. 

#FAFAFA
- Offwhite color was used for the text throughout the project. I felt it's softer of the eyes over default white, and compliments the blue and dark grey really well.

#484848
- A slightly lighter shade of grey was mainly used on the Bootstrap toasts as a background. I choose this, so it's easier for the user to view the toasts and descern the difference between elements overlapping.

#### **Fonts**

Google Fonts - Quicksand
- I chose Quicksand as my font throughout the project. The font is easily readible and simple. I opted to have a single font in this project simply because the project as whole isn't text heavy, and chose to instead to use a heavier font weight for headings.

#### **Images**

My images over the course of the project did manage to evolve and develop thanks to Sonia Akhtar Hussain.
My defualy images for the product had white background, and Sonia used her skills to really base the products stand out with a custom background.
Please visit the credits section for a link to Sonia's profile.

#### **Database Design**

SQLite was used during development and then Heroku Postgres in production.

[Database Diagram](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/schema/database.pdf)

#### **Key Models**

**UserProfile**
- The user profile is connected to the User model created by Allauth on registration.
- The default fields are saved fields by the user to speed up the checkout process by pre-populating shipping details.

**Order**
- The order model is connected to the User Profile, allows the user to view their previous orders.
- The order model acts as a container for the orderlineitems. Although is item is stored within the OrderLineItem model, having them connected allows to retrieve the item purchased.

**Product**
- The product model hold key information for each product. Each product has a unique ID.
- The product model is connected to the category model, this allows the user to filter products by category.

**ProductReview**
- Reviews for products can be left for products with this model, having it connect to the Product model via the ID.
- The review model also is connected to the User model to obtain the user's username. This allows user to see the name of the user on each review. 

**WishList**
- The wishlist model allows user to save items for quicker access. These items can be removed.
- This model also acts as a container for the WishListItem model. Just like the Order model, each wishlist is unique to each user but connecting to the user ID.

---

## **The Skeleton Plane**

I made some significant changes from my original wireframes. Some changes were more based on removing features I had planned to implement, and other changes were made after receiving feedback.

[Navbar Wireframes](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/wireframes/navbar-wireframes.pdf)

- I decided to change my navbar signifcantly due to originally planning to have more pages than I finished with.
- The search input field stayed in the middle, but on mobile and tablet resolutions the search bar is instead held within a font awesome magnifying icon. User can still acess the search bar on mobile by clicking the icon to reveal the bar.
- The left sid has had to most changes due to not having additional pages that were planned. Instead only a Home link is there to give users a way toget back to the home page. 

[Shopping Bag Wireframes](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/wireframes/checkout-page-wireframes.pdf)

- The shopping bag page has it's layout changed mainly on mobile, whereas on desktop everything is more condensed so not to take up the full width of the browser.
- On smaller resolutions fitting everything within a 320px resolution became incredibly problematic. Everything felt squashed and condensed.
- To remedy the smaller resolutions, items within the bag now show u vertically, with the image first, name, price, quantity input and total for the product in that order. This change was well recieved from the feedback I got, and all in all provides a better user experience.

[All Products Wireframes](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/wireframes/shop-page-wireframes.pdf)

- I changed the amount of products being shown horizontally from 4 to 3. This change was the leverage how good I felt the product images were.
- I removed the deatils and add to bag buttons, the image now acts as a link to the products detials page.

[Product Details Wireframes](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/wireframes/products-detail-wireframes.pdf)

- Small change on this page was to move the product description to below the product. I felt as though the amount of information on the right side of the page was causing a bad user experience. Moving the description below also allowed me to increase the font size to make it easier to read.

[Account Page Wireframes](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/wireframes/account-page-wireframes.pdf)

[Checkout Success Wireframes](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/wireframes/checkout-success-wireframes.pdf)

[Register Wireframes](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/wireframes/register-page-wireframes.pdf)

[Log In Wireframes](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/wireframes/login-page-wireframes.pdf)

---

## **The Surface Plane**

### **Features**

*Features present across the project,*

**Navigation Bar**
- Navbar is implemented on every page and is fully responsive across all resolutions.
- Users are able to freely navigate across the site freely.
- Users shopping have the cost of the current shopping basket display on large screen sizes.

![Project Navigation Bar](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/images/navbar.png "Image of the navigation bar")

**Introduction**
- Home page features an introductions to notify users to welcome them and explain the purpose of the site.

![Project Introduction](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/images/introduction.png "Image of the Introduction")

**Store Page**
- Store page offer products on large resolutions in a row of three. Image are lare to attract users attention, and clicking the image will redirect the user to the product detail page.

![Products](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/images/shop.png "Image of the products in the store")

**Search Functionality**
- Users can take advantage of the the search function within the navigation bar to search for products or descriptions.
- Search results are show in a simple format with a link to redirect to the general store page.

![Search Results](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/images/search.png "Image of the search results")

**Reviews**
- Users can choose to view the reviews left by users for a specific product.
- Logged in users are able to post a review, whereas users not logged in are show a small message to log in to leave a product review.
- User choosing the leave a review can choose to pick a title, give a start rating out of five, and write a review.

![Reviews](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/images/reviews.png "Image of the reviews section")

**Toasts**
- Almost all actions provide feedback to the user via the bootstrap toasts writted to provide used feedback.
- Users shopping can view the current items within the bag and total cost. How much they need to spend to get free delivery.
- At the bottom of the toast is a link to the checkout page.

![Toasts](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/images/toasts.png "Image of the toasts.")

**Shopping Bag**
- The shopping bag page is fully responsive, showing users a picture of the item, name, price per unit, and total price.
- Users can also chohose to increase/decrease the quantity of items in their bag, click the update button to have the prices update.
- user can click the remove link and have all the item within the bag removed, regardless of quantity.
- At the bottom of the page user can find the cost of the bag, cost of delivery, the grand total and how much they must spend to be eligible for free delivery.

![Shopping Bag Page](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/images/shopping-bag.png "Image of the the shopping bag page with 2 items")

**Checkout Overlay**
- Users who checkout will see a simple overlay with a spinning icon while the payment is processed.

![Loading Overlay](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/images/overlay.png "Image of the the loading overlay")

**Social Media Links**
- Every page throughout the project has a footer with social media links. 
- Clicking the social media like redirect the user to the social media page in a new tab, so not to cause disruption to the user experience.

![Social Media Icons](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/images/social.png "Image of the the social media icons in the footer")

---

## **Technologies Used**

- [Python](https://www.python.org/) 
    - The following Python modules were used on this project, 
        - asgiref==3.4.1
        - boto3==1.18.26
        - botocore==1.21.26
        - dj-database-url==0.5.0
        - Django==3.2.5
        - django-allauth==0.41.0
        - django-countries==7.2.1
        - django-crispy-forms==1.12.0
        - django-storages==1.11.1
        - gunicorn==20.1.0
        - jmespath==0.10.0
        - oauthlib==3.1.1
        - Pillow==8.3.1
        - psycopg2-binary==2.9.1
        - pylint-django==2.4.4
        - pylint-plugin-utils==0.6
        - python3-openid==3.2.0
        - pytz==2021.1
        - requests-oauthlib==1.3.0
        - s3transfer==0.5.0
        - sqlparse==0.4.1
        - stripe==2.60.0

- [Heroku Postgres](https://www.heroku.com/postgres)

- [AWS S3](https://aws.amazon.com/)
 
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)

- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)

- [Bootstrap](https://getbootstrap.com/)

- [jQuery](https://jquery.com/)

- [JavaScript](https://www.javascript.com/)

- [Google Fonts](https://fonts.google.com/)

- [Font Awesome](https://fontawesome.com/)

- [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)

- [Github](https://github.com/)

- [Git](https://git-scm.com/)

- [Gitpod](https://www.gitpod.io/)

- [Balsamiq](https://balsamiq.com/)

- [AutoPrefixer](https://autoprefixer.github.io/)

- [Grammarly](https://www.grammarly.com/)

---

## **Testing**

Link to the Testing Document
- [TESTING.md](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/TESTING.md)
---

## **Deployment**

The master branch of this repository is the most current version and has been used for the deployed version of the site.

The Code Institiue student template was used to create this project.

[Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)

- Click the *Use This Template* button.
- Give your repository a name, and description if you wish.
- Click the *Create Repository from Template* to create your repository. 
- Click the *Gitpod* button to create a gitpod workspace, this can take a few minutes.
- When working on project using Gitpod, please open the workspace from Gitpod, this will open your previous workspace rather than creating a new one.
Use the following commands to commit your work, 
- `git add . ` - adds all modified files to a staging area.
- `git commit -m "A short message exlaining your commit"` - commits all changes to a local repository.
- `git push` - pushes all your commited changes to your Github repository.

**Requirements**

- [Python 3](https://www.python.org/downloads/)
- [Pip](https://pypi.org/project/pip/)
- [Git](https://git-scm.com/)
- [AWS S3](https://aws.amazon.com/)

**Creating a Clone**

1. From the repository, click *Code*
2. In the *Clone >> HTTPS* section, copy the clone URL for the repository
3. In your local IDE open Git Bash
4. Change the current working directory to the location where you want the cloned directory to be made
5. Type `git clone`, and then paste the URL you copied in Step 2 - ``git clone https://github.com/Harry-Leepz/Nourish-and-Lift.git``
6. Set the following values in a `env.py` file.
```
import os

os.environ.setdefault("SECRET_KEY", "<app secret key of your choice>")
os.environ.setdefault("DEVELOPMENT", "True")
os.environ.setdefault('STRIPE_PUBLIC_KEY', '<key generated by Stripe>')
os.environ.setdefault('STRIPE_SECRET_KEY', '<key generated by Stripe>')
os.environ.setdefault('STRIPE_WH_SECRET', '<key generated by Stripe>')
```

- Stripe keys are generated by Stripe, each individual have their own unique key values.
- *PLEASE MAKE SURE NEVER TO PUBLISH THESE KEYS, ADD THE `env.py` TO A `.gitignore` TO AVOID PUSHING KEYS TO GITHUB.*
7. Install the project requirements - `pip3 install requirements.txt`
8. Apply database migrations - `python manage.py migrate`
9. Create a superuser - `python manage.py createsuperuser`
10. The project can be run with the following - `python manage.py runserver`

**Heroku Deployment**

1. Log into Heroku
2. Create a new app, choose a location closest to you
3. Search for Heroku Postgres from the resources tab and add to your project
4. Make sure to have `dj_database_url` and `psycopg2` installed.
```
pip3 install dj_database_url
pip3 install psycopg2
```
5. Login to the Heroku CLI - `heroku login -i`
6. Run migrations on Heroku Postgres - `heroku run python manage.py migrate`
7. Create a superuser - `python manage.py createsuperuser`
8. Install `gunicorn` - `pip3 install gunicorn`
9. Create a requirements.txt file - `pip3 freeze > requirements.txt`
10. Create a `Procfile` (note the capital P), and add the following,
```
web: gunicorn moose_juice.wsgi:application
```
11. Disable Heroku from collecting static files - `heroku config:set DISABLE_COLLECTSTATIC=1 --app <your-app-name>`
12. Add the hostname to project settings.py file
```
ALLOWED_HOSTS = ['<you-app-name>.herokuapp.com', 'localhost']

```
13. Connect Heroku to you Github, by selecting Github as the deployment method and search for the github repository and pressing `connect`
14. In Heroku, within settings, under config vars select `Reveal config vars`
15. Add the following, 
```
AWS_ACCESS_KEY_ID =	<your variable here>
AWS_SECRET_ACCESS_KEY =	<your variable here>
DATABASE_URL =	<added by Heroku when Postgres installed>
DISABLE_COLLECTSTATIC =	1 
EMAIL_HOST_PASS = <your variable here>
EMAIL_HOST_USER = <your variable here>
SECRET_KEY = <your variable here>
STRIPE_PUBLIC_KEY = <your variable here>
STRIPE_SECRET_KEY = <your variable here>
STRIPE_WH_SECRET = <different from env.py>
USE_AWS = True
```
16. Go back to the Deploy tab and under Automatic deploys choose `Enable Automatic Deploys`
17. Back in your CLI add, commit and push your changes and Heroku will automatically deploy your app
```
git add .
git commit -m "Initial commit"
git push
```
18. Your deployed site can be launched by clicking `Open App` from its page within Heroku.

**AWS S3 Bucket setup**
1. Create an Amazon AWS account
2. Search for S3 and create a new bucket
    - Allow public access
3. Under Properties > Static website hosting
    - Enable
    - index.html as index.html
    - save
4. Under Permissions > CORS use the following:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
5. Under Permissions > Bucket Policy:
    - Generate Bucket Policy and take note of Bucket ARN
    - Chose S3 Bucket Policy as Type of Policy
    - For Principal, enter *
    - Enter ARN noted above
    - Add Statement
    - Generate Policy
    - Copy Policy JSON Document
    - Paste policy into Edit Bucket policy on the previous tab
    - Save changes
6. Under Access Control List (ACL):
    - For Everyone (public access), tick List
    - Accept that everyone in the world may access the Bucket
    - Save changes

**AWS IAM (Identity and Access Management) setup**
1. From the IAM dashboard within AWS, select User Groups:
    - Create a new group
    - Click through and Create Group
2. Select Policies:
    - Create policy
    - Under JSON tab, click Import managed policy
    - Choose AmazongS3FullAccess
    - Edit the resource to include the Bucket ARN noted earlier when creating the Bucket Policy
    - Click next step and go to Review policy
    - Give the policy a name and description of your choice
    - Create policy
3. Go back to User Groups and choose the group created earlier
    - Under Permissions > Add permissions, choose Attach Policies and select the one just created
    - Add permissions
4. Under Users:
    - Choose a user name 
    - Select Programmatic access as the Access type
    - Click Next
    - Add the user to the Group just created
    - Click Next and Create User
5. Download the `.csv` containing the access key and secret access key.
    - **THE `.csv` FILE IS ONLY AVAILABLE ONCE AND CANNOT BE DOWNLOADED AGAIN.**

**Connecting Heroku to AWS S3**
1. Install boto3 and django-storages
```
pip3 install boto3
pip3 install django-storages
pip3 freeze > requirements.txt
```
2. Add the values from the `.csv` you downloaded to your Heroku Config Vars under Settings:
3. Delete the `DISABLE_COLLECTSTATIC` variable from your Cvars and deploy your Heroku app
4. With your S3 bucket now set up, you can create a new folder called media (at the same level as the newly added static folder) and upload any required media files to it.
    - **PLEASE MAKE SURE `media` AND `static` FILES ARE PUBLICLY ACCESSIBLE UNDER PERMISSIONS**


---

## **Credits**

**Product Images / Names / Descriptions**
- All the content relating to the products all came from the Argos website. Although the images were altered the original images were screen shots taken from items from there.
- [Argos](https://www.argos.co.uk/list/shop-all-opti-weights?tag=ar:shop:opti:weights-dumbbells-lb)
    - This project is made solely for educational purposes. There is no financial gain from the project. 

**Code**
- A large amount of code came from the Code Institute, Boutique Ado Project.
- [Code Institute, Boutique Ado](https://harry-boutique-ado.herokuapp.com/)
    - Boutique Ado is a walkthrough project by Code Institute, this project gave students an introduction to Django/AWS S3/Stripe/Heroku Postgres
    - The core functionality of Nourish and Lift is all taken from the Boutique Ado project.

**Bootstrap**
- The Bootstrap Library was used through the project. The project used version 4.6.
- [Bootstrap](https://getbootstrap.com/docs/4.6/components/alerts/)
    - Toasts/Navigation Bar/Forms/Dropdown Menu/Buttons, the core elements mentioned are all found in the Bootstrap components section and built upon.

**Django Documentation**
- Django have amazing documentation with a tutorial project and in depth explanations on core components.
- [Django Documentation ](https://docs.djangoproject.com/en/3.2/)

## **Aknowledgements**

Chris Zielinski
- [LinkedIn Profile](https://www.linkedin.com/in/ckz8780/)
    - The creator of the Boutique Ado project. Also Help create the models and views for the wishlist app.
    - He has been a huge help and support throughotu this project, not only to me but countless other students. Takes time out of his day to help and respond to messages and has always been extremely courteous and respectful.

