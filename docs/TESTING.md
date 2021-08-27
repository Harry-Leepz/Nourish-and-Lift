[Back to README](https://github.com/Harry-Leepz/Nourish-and-Lift#nourish-and-lift)

---

### **User Stories Testing**

- [Regular Site User Stories Testing](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/regular-site-user-stories.pdf)

- [Customer Shopper Stories Testing](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/customer-shopper-stories.pdf)

- [Customers (Logged in) Stories Testing](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/logged-in-stories.pdf)

---

### **Manual Testing**

**Navigation Bar** 
- Navigation bar is fully responsive on large/medium/small resolutions.
- At 320px, all navigation links are inline and not wrapping on another line.
- All links are correctly redireting to the correct pages. 
- Signing out, correctly shows the correct dropdown options, Log in and Register.
- Signing in, correctly shows the correct dropdown options, My profile and Logout.
- Admins, have additional option in dropdown menu to Product Management page.

**Footer**
- Hover Css is correctly working, changing the color on the icon on hover.
- Links redirect to the correct social media page.
- Links open in a new browser tab. 

**Products**
- On loading products correct appear in Sku order.
- Sorting functionality works, correctly sorting products by price descending or ascending.
- Confirm product name and price against their fields in the database.
- Products have the correct tag.
- Tags are correctly redirecting and filtering products by category name.

**Products Details**
- Correct redirect to the correct product on the clicking the product image.
- Products details are correct and match the details in the database.
- Product quantity buttons are correctly disabled when at 1 or 99.
- Add to wishlist button correctly only shows up for logged in users.
- Links correctly work, redirecting back to the products page and adding the product to the shopping bag.


**Reviews**
- Product reviews show for the correct product, matching the database.
- Product review form correctly not showing for users not logged in, shows for logged in users. 
- Confirm only the user who created the review or superusers have the option edit a review.
- Editing a review correctly edits the review, redirects to the correct sections of the page.


**WishList**
- Confirm users who are not logged in do not have the option to add a product to the wishlist.
- Confirm users who are logged in do have the option to add an item to their WishList.
- Confirm users who are not logged in are rredirected to the Log In page when clicking the WishList link.
- Products details links correctly redirects to the correct page when clicking the link on the WishList Page.
- Removing an item from the WishList working correctly, correctly reflected within the database.

**Admin**
- Only admins have access to the Product Management page on the account dropdown.
- Only admins are able to see the Edit/Delete buttons on the product details page.
- Product Management links correctly redirect to the add product page.
- Adding a product working correctly, product has the correct information from the form. Correctly shows within the database.
- Editing the product, working fully, reviews are maintained for the products after editing. Details correctly reflected.
- Delete button correctly shows modal to confirm delete.
- Deleting a products correctly removed the product from the database, and any reviews for the products are also deleted.

**Shopping Bag**
- Shopping bag link in navbar shows correct value of the current bag session.
- Quantity buttons are working correctly preventing the user from exceeding 99 and going below 1.
- Correct products are shown in the shopping bag.
- Adding items to the bag, and logging in after correctly retains the current bag.
- Correct totals are shown.
- Free deleivery threshhold correctly updates, shows correct values.

**Checkout**
- Correct items are carried over from shopping bag to checkout page.
- Form correctly responds to invalid inputs.
- Redirects to the checkout success page correctly.
- Stripe correctly showing 200 status webhooks for orders.

**Search Bar**
- Showing correct search for words searched.
- Adding a new product and search by it's name correctly shows the product.
- User feedback is accurate.


**Chrome Dev Tools**

Chrome dev tools was used throughout the development of the project to test responsiveness.
Responsiveness was tested using Dev Tools to emulate the following devices,
- Iphone 5
- Iphone 6/7/8
- Iphone 6/7/8 Plus
- Iphone X
- Ipad
- Ipad Pro

**Browser Testing**

During development, the testing was mainly done solely using Google Chrome.

In production the site has been tested on the following browsers,
- Google Chrome
- Mozilla Firefox
- Opera
- Microsoft Edge

---

### **Automated Testing**


[W3C HTML Validator](https://validator.w3.org/)
- 0 Errors
- 0 Warnings

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- 0 Errors
- 28 Warnings
    - These warnings are in relation to a unknown vendor extentions that are added by CSS Autoprefixer for cross browser support.

[JSHint JavaScript Validator](https://jshint.com/)
- 0 Errors
- 1 Undefined variable `stripe`.
    - This variable is being used.

The python extention was used to test Python for Pep8 compliance withit's built in linting too.
- Alot of the Python errors were fixed during development.
- Any errors that related to files that were auto generated by Django were left untouched.
    - Migration files.
    - Project setting.py
    - ./manage.py
    - checkout/__init__.py
- The errors relating to the variable 'e' not being used,
    - 'e' as a variable here is used to capture any errors from the Stripe webhook handler.
- There are 2 errors relating to lines being too long in the checkout app,
    - models.py has 1 line that cannot be shortened without breaking the code
    - webhooks.py has 1 line that cannot be shortened wihout breaking the code.
- ./checkout/app.py - 'checkout.signals' imported but unused
    - The import is used to let Django know there a signals module, listening for changes to automatically updating the totals

![Flake 8 Python code errors](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/images/pep8.png "Python code errors")


### **Bugs and Fixes**


- Reviews not being centered.
    - Credit to Benjamin Kavanagh for finding this issue.
    - Added `text-center mt-5` to the div, to have all the text centered and add margin to the top.

![Empty reviews message not centered image](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/images/review-fix.png "Empty reviews message not centered image")

- Button to edit the review was overlapping the container.
    - Credit to Benjamin Kavanagh for finding this issue and fixing it Chrome Dev Tools.
    - Fix was impletemented in base.css with the solution Banjamin used in Chrome Dev Tools.

![An image of the review button fix](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/images/review-button-fix.png "Review button fix")

- Missing 404 and 500 error pages.
    - Credit to Benjamin Kavanagh for finding this issue and offering a solution.
    - 404.html and 500.html templates were created with a heading and button to redirect the user to the products page.

- Adding a product to the wishlist created an infinite loop, if the user was not signed it. The user would correctly be redirected to the login page, but the backend would carry on attempting to add the product to the wishlist.
    - I removed the wishlist button for users not logged in, and set it to show only if the user is logged in. This avoid the loop from taking place.

- Wishlist app template rendering. I had significant issues writing the view to render the wishlist template correctly.
    - Chris Zielinski rewrote the view for the wishlist view, wish was far clearner and functioned correctly.

Original Wishlist view by me,
```
@login_required
def wishlist(request):
    """
    A view to render the users wishlist
    """
    wishlist_count = WishList.objects.filter(user=request.user).count()
    if wishlist_count > 0:
        wishlist = WishList.objects.get(user=request.user)
        items = WishListItem.objects.filter(wishlist=wishlist.user.id)

        context = {
            'items': items,
        }
    else:
        context = {}
    return render(request, 'wishlist/wishlist.html', context=context)
```

Chris Zielinski Wishlist view solution,
```
@login_required
def wishlist(request):
    """
    A view to render the users wishlist
    """
    wishlist = None
    try:
        wishlist = WishList.objects.get(user=request.user)
    except WishList.DoesNotExist:
        pass

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist/wishlist.html', context=context)
```

- Footer appearing higher up on pages with less content.
    - Credit to Jane Rinn for pointing this issue out.
    - A `large-container` class was created with a `min-height` to push the content down. This was applied to the shopping bag template,
    wishlist template and allauth templates.

- Unused variable in wishlist app.
    - Credit to Aaron Sinnot for providing a solution.
    - My original code for my add_to_wishlist view,
    ` wishlist, created = WishList.objects.get_or_create(user=request.user)` this was causing a Pep8 error with the `created` variable being unused.
    - `wishlist, _ = WishList.objects.get_or_create(user=request.user)` Aaron suggested to use an underscore.

### **Un-resolved Bugs**

- Users logged in who have items in their shopping bag, lose the contents of their shopping bag upon logging out.

- Users are able to delete the current number in the quantity input, and can add to bag on the product detail page or update in the shopping bag page.
    - Users are redirected to a 404 error page when they do this, but the core issue remains unresolved.

- Clicking a drop down option is using the default blue acchor tag color for a split second.

- Successful messages can be difficult to see and understand if item are in the shopping bag. On any success notitifcation, the bag contents are always displayed.

- Filename not showing when adding or editing products. 
    - I had a duplicate id error in the html validator orignally, and although the id's were different, I had to remove one if to pass validations. Doing so though has caused the above error.

