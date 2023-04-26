{
    "name": "IOT",
    "version": "16.0",
    "author": "Protoneer",
    "summary": """IOT""",
    "license": "LGPL-3",
    "depends": ["base_automation"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "data" : [
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/devices.xml',
        'views/base_automation.xml',
    ]
}
