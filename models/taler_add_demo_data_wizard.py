# SPDX-FileCopyrightText: 2025 Mael Panouillot <panouillot.mael@gmail.com>
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from odoo import models

class TalerAddDemoDataWizard(models.TransientModel):
    _name = "tops.add.demo.data.wizard"
    _description = "Confirmation popup to add demo data"

    def action_proceed(self):
        active_id = self.env.context.get("active_id")
        if not active_id:
            return {"type": "ir.actions.act_window_close"}

        record = self.env[self.env.context["active_model"]].browse(active_id)

        record.write({
            "taler_merchant_url": "https://backend.demo.taler.net/instances/sandbox", # this value is the url to the Taler merchant sandbox environment
            "taler_merchant_password": "sandbox" # sandbox is the password to the Taler merchant sandbox environment
        })

        return {
            "type": "ir.actions.client",
            "tag": "reload",
        }

    def action_cancel(self):
        return {"type": "ir.actions.act_window_close"}
