# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from openerp import models, api
from openerp.exceptions import Warning as UserError
from openerp.tools.translate import _

logger = logging.getLogger(__name__)


class ProxyBackend(models.Model):
    _inherit = "proxy.backend"

    @api.model
    def get_aeroo_report(self, report_name, object_id, params=None, copies=1):
        if not params:
            params = {}
        logger.info(
            'Values Report %s ID %s',
            report_name, object_id)
        if len(object_id) > 1:
            data_id = object_id
        else:
            data_id = [object_id[0]]
        report = self.env['ir.actions.report.xml']._lookup_report(report_name)
        report_xml = self.env['report']._get_report_from_name(report_name)
        data = {
            'model': report_xml.model,
            'id': data_id,
            'report_type': 'aeroo',
        }
        logger.info(
            'Request printing aeroo report %s model %s ID %s Context %s in %d copies ',
            str(report), data['model'], data['id'], self.env.context, copies)
        
        aeroo_report_content, aeroo_report_format = report.create(
            self.env.cr, self.env.uid, data_id,
            data, context=dict(params))

        return {
            "content": aeroo_report_content,
            "format": aeroo_report_format
        }
