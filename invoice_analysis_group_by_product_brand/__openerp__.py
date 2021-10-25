# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Invoice Analysis Group By Product Brand",
    "version": "8.0.1.0.0",
    "category": "Accounting & Finance",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "website": "https://simetri-sinergi.id",
    "license": "AGPL-3",
    "installable": True,
    "depends": ["account", "product_brand"],
    "data": [
        "views/invoice_report_views.xml",
    ],
}
