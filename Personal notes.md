<!--
SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>

SPDX-License-Identifier: CC0
-->

DON'T FORGET THE RELEASE TAGS ON THE REPOSITORY

Odoo addon creation
- I used a virtual env in python named venv
	- To set it, go to /opt/odoo and use `source venv/bin/activate`
Start Odoo with:
	`./odoo-bin --addons-path=./addons,./custom_addons`
	`./odoo-bin --addons-path=./addons,./custom_addons -u tops -d odoo18_tops_0.1.1.1`
	`./odoo-bin --addons-path=./addons,/media/sf_VMSharedFolders/custom_addons -u tops -d odoo18_tops_0.1.1.1`


How to edit the database directly to postgres
- Change the user to 'postgres' user: `sudo su postgres`
- Run psql with psql`
- In the postgres interface, you can do whatever you want (don't forget the semicolon)
	- Example, give user permission to create DB: `ALTER ROLE nemael createdb;`

- If I don't see my custom add-on, I can click "update app list" on the top bar

Versioning system:
    - x:y:z
        - x is major version
        - y is the revision (slight changes to the implementation, no effect on me)
        - z is the age. "how many current version are backward supported?"

Odoo URL is `nemaodootaler:S8069/odoo/apps`

Sandbox URL is:
- https://backend.demo.taler.net/instances/sandbox

For now: steps to add Taler to point of sale
- Create TalerOnline as a new payment method in pos
- Go in pos settings and add TalerOnline in the "payment method" section for one of the shops
- Setting "Allowed Providers" should be set to "Taler" only

- DB `./odoo-bin --addons-path=./addons,/media/sf_VMSharedFolders/custom_addons -i tops -u tops --init tops -d odoo18_tops_0.3.1.5` is the reliable one

- The list of countries is stored in `odoo/addons/base/data/res_country_data.xml`

- How to run odoo with debug logs:
  - Add `--log-level=debug` at the end of the command
  - `./odoo-bin --addons-path=./addons,/media/sf_VMSharedFolders/custom_addons -i tops -u tops --init tops -d odoo18_tops_0.3.1.19 --log-level=debug`

- Delete a database (to free up space)
  - `sudo -u postgres psql`
  - `\l` to display list of db
  - `DROP DATABASE database_name;` to drop what I want

- SSH troubles
  - On opening a new terminal for git, that has the wrong ssh authentication (can't connect to Codeberg)
  - Run `eval "$(ssh-agent -s)"`
  - Run `ssh-add ~/.ssh/id_ed25519`
    - For authentication, use the ssh passphrase that I saved. An empty passphrase is not valid
    - This command has to return something such as "Identity added", otherwise it means the key wasn't added
  - Run `ssh-add -l` to confirm that the ssh key was added
  - I can now clone and push using ssh to this repository

- How to change the currency of my Odoo instance
  - Change the main or secondary currencies in the settings of your instance

- How to attach a tag to a commit
  - After a commit is made and pushed to the repository
  - Run `git tag "tag_string"` to make the tag
  - Run `git push origin tag "tag_string"` to push the tag to the repository. `tag_string` must match with the previous command
