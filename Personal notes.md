DON'T FORGET THE TAGS

Odoo addon creation
- I used a virtual env in python named venv
	- To set it, go to /opt/odoo and use "source venv/bin/activate"
Start Odoo with:
	./odoo-bin --addons-path=./addons,./custom_addons
	./odoo-bin --addons-path=./addons,./custom_addons -u tops -d odoo18_tops_0.1.1.1
	./odoo-bin --addons-path=./addons,/media/sf_VMSharedFolders/custom_addons -u tops -d odoo18_tops_0.1.1.1


How to edit the database directly to postgres
- Change the user to 'postgres' user: "sudo su postgres"
- Go to psql: "psql"
- In the postgres interface, you can do whatever you want (don't forget the semicolon)
	- Example, give user permission to create DB: "ALTER ROLE nemael createdb;"


- If I don't see my custom add-on, I can click "update app list" on the top bar

Versioning system:
    - x:y:z
        - x is major version
        - y is the revision (slight changes to the implementation, no effect on me)
        - z is the age. "how many current version are backward supported?"

Odoo URL is nemaodootaler/8069/odoo/apps


What to do when doing a transaction:
    - Make sure I am talking to the right type of service
        - When running the query to get the server config, field "name" should = "taler-merchant"
            - If not, it might be that you are connecting to another service from the taler network.
    - Check that the current wallet version does support the taler merchant version (see video 2 on the versioning system)


More explanations on the settings and how to build them (see at 11min30)
https://www.youtube.com/watch?v=1me-Lto2EPY
