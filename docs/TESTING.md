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
- Logging out with items in the bag correctly empties shopping.
- Adding items to the bag, and logging in after correctly retains the current bag.
- Correct totals are shown.
- Free deleivery threshhold correctly updates, shows correct values.

**Checkout**
- Correct items are carried over from shopping bag to checkout page.
- Form correctly responds to invalid inputs.
- Redirects to the checkout success page correctly.
- Stripe correctly showing 200 status webhooks for orders.
