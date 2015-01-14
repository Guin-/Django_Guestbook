# Django_Guestbook

# README #

This is a Django project I am building out to try to get familiar with the framework. Listed below is the outline of what the finished Guestbook should contain/do. 

The Guestbook is a simple app with the following functionality:

* The app has a single page called "index"
* The "index" page has a single form at the top of the page where any anonymous visitor can submit a GuestbookEntry.
* A "GuestbookEntry" consists of the following:
1. A name (required)
2. An email address (optional)
3. A free-form comment (required)
* Beneath the GuestbookEntry form, the page should also list all other GuestbookEntries made by all previous visitors to the page, in reverse chronological order.

Additional Considerations:

* User input should be sanitized so that users cannot inject arbitrary html or javascript into the page when their entries are displayed on future page loads.
* There should be validation on the email field to ensure that it is actually an email address and not just a random string of characters.
* There should be some general validation on the form to ensure that required fields have been submitted

* Create pagination of Guestbook entries. 
* A Page should consist of up to 10 entries.
* If there are more than 10 entries to show, then there should be "Prev" and "Next" links at the bottom to show the previous (or next) Page of GuestbookEntries
