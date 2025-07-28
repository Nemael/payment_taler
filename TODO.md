odoo differences community edition and enterprise edition
how to install odoo enterprise edition on my own server


First do a first draft of the logic used to make a payment to Taler
	Reach out to the guy who is making the Python implementation for Frog logo ERP
Then buy a subscription to Odoo Enterprise edition to implement this logic into existing modules that use payments, accounting is the priority


Remove the __pycache__ folder from the repository



Taler ideas:
    - For password
        - Maybe I should only store the Taler token, or a hash of the user's Taler password
            - (have to learn how to manage a password like this, best practices)
        - When I enter a merchant url, add a button "is my url valid?" that sends a request with the configuration payload to the other side of the url, and if the configuration is valid, confirm that this is a valid merchant url
            - Add a circling waiting animation + 3 seconds of forced delay, to make this button feel better.


Check this warning in Odoo console logs
    - WARNING odoo18_tops_0.1.1.1 odoo.modules.module: Missing `license` key in manifest for 'tops', defaulting to LGPL-3

Make the settings company-specific, so you can switch company and use a different Taler endpoint and password and such
    See https://www.youtube.com/watch?v=1me-Lto2EPY


I can access the settings from the top bar in the add-on, but I cannot see the settings on the left bar when I am opening the settings pages. Make it so that the settings appear on the left bar as well.


Make a longer line for the setting of the Merchant URL, in the settings page, so that the whole URL can be displayed at once instead of having to scroll it.


Check if "Taler Merchant URL" is the proper name for the URL my add-on will connect to make a payment with Taler

Find a better way to store the password+secret token, and make ui to ask user for password
Add popups when an error from a request occurs
Add the "app" tag to the module at the end of the project, to make it findable in the app install menu.
Add the icon from Taler in the settings page (and plenty of other spots)
