# Copyright 2014 Daniel Reis
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import fields, models, api


_TASK_STATE = [
    ('draft', 'New'),
    ('open', 'In Progress'),
    ('pending', 'Pending'),
    ('done', 'Done'),
    ('cancelled', 'Cancelled')]


class ProjectTaskType(models.Model):
    """Added state in the Project Task Type."""

    _inherit = 'project.task.type'

    state = fields.Selection(
        _TASK_STATE,
        'State'
    )

    closed = fields.Boolean(
        help="Tasks in this stage are considered closed.",
        compute='_compute_closed',
        store=True,
    )

    @api.multi
    @api.depends('state')
    def _compute_closed(self):
        for stage in self:
            stage.closed = stage.state in ('done', 'cancelled')
