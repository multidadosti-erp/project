# Copyright 2014 Daniel Reis
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models


class ProjectTask(models.Model):
    """Added state in the Project Task."""

    _inherit = 'project.task'

    stage_state = fields.Selection(
        related='stage_id.state',
        oldname='state',
        store=True
    )

    closed = fields.Boolean(
        related='stage_id.closed',
        store=True
    )
