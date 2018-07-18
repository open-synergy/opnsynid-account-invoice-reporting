# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    product_brand_id = fields.Many2one(
        string="Product Brand",
        comodel_name="product.brand"
    )

    def _select(self):
        _super = super(AccountInvoiceReport, self)
        select_str = _super._select() + """
        , sub.product_brand_id
        """
        return select_str

    def _sub_select(self):
        _super = super(AccountInvoiceReport, self)
        select_str = _super._sub_select() + """
        , pt.product_brand_id
        """
        return select_str

    def _group_by(self):
        _super = super(AccountInvoiceReport, self)
        group_by_str = _super._group_by() + """
        , pt.product_brand_id
        """
        return group_by_str
