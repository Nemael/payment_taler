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

Odoo URL is nemaodootaler:S8069/odoo/apps

Sandbox URL is:
- https://backend.demo.taler.net/instances/sandbox

For now: steps to add Taler to point of sale
- Create TalerOnline as a new payment method in pos
- Go in pos settings and add TalerOnline in the "payment method" section for one of the shops
- Setting "Allowed Providers" should be set to "Taler" only

- DB ./odoo-bin --addons-path=./addons,/media/sf_VMSharedFolders/custom_addons -i tops -u tops --init tops -d odoo18_tops_0.3.1.5 is the reliable one

- The list of countries is stored in odoo/addons/base/data/res_country_data.xml

- How to run odoo with debug logs:
  - Add "--log-level=debug" at the end of the command
  - ./odoo-bin --addons-path=./addons,/media/sf_VMSharedFolders/custom_addons -i tops -u tops --init tops -d odoo18_tops_0.3.1.19 --log-level=debug

- Delete a database (to free up space)
  - sudo -u postgres psql
  - \l to display list of db
  - DROP DATABASE database_name; to drop what I want
