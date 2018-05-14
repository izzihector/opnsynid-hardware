# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Backend Direct Printing Using Hardware Proxy + "
            "Aeroo Report + Cups",
    "version": "8.0.1.0.0",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "report_aeroo",
        "proxy_backend",
        "base_other_report_engines"
    ],
    "data": [
        "views/proxy_backend_cups_aeroo.xml"
    ],
}
