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

Sandbox URL is:
- https://backend.demo.taler.net/instances/sandbox



--dev <feature,feature,...,feature>
    comma-separated list of features. For development purposes only. Do not use it in production. Possible features are:
        all: all the features below are activated
        xml: read QWeb template from xml file directly instead of database. Once a template has been modified in database, it will be not be read from the xml file until the next update/init. Particularly, templates are not translated on using this option.
        reload: restart server when python file are updated (may not be detected depending on the text editor used)
        qweb: break in the evaluation of QWeb template when a node contains t-debug='debugger'
        (i)p(u)db: start the chosen python debugger in the code when an unexpected error is raised before logging and returning the error.
        werkzeug: display the full traceback on the frontend page in case of exception

Run tests with `/odoo-bin --test-file=/media/sf_VMSharedFolders/custom_addons/tops/tests/welcome_tests.py`
