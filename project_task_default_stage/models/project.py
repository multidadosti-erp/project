# Copyright 2015 Incaser Informatica S.L. - Sergio Teruel
# Copyright 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models, api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    def _get_default_type_common(self):
        ids = self.env['project.task.type'].search([
            ('case_default', '=', True)])
        return ids

    @api.model
    def create(self, values):
        """ Metodo para adicionar os estágios padrão no projeto.

        Arguments:
            values {dict} -- valores para criação do projeto.

        Returns:
            project.project -- retorna criação do projeto
        """
        if 'type_ids' not in values:
            standard_stage_ids = self._get_default_type_common()

            if standard_stage_ids:
                values['type_ids'] = [(6, 0, standard_stage_ids.ids)]

        return super(ProjectProject, self).create(values)
