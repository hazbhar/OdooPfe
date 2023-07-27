# See LICENSE file for full copyright and licensing details.

{
    "name": "IDAFormation",
    "version": "15.0.1.0.0",
    "author": "Hazem Bhar",
    "category": "IDAF Management",
    "license": "AGPL-3",
    "complexity": "easy",
    "Summary": "A Module For IDAFormation Management",
    "images": ["static/description/EMS.jpg"],
    "depends": ["hr", "crm", "account"],
    "data": [
        "security/IDAFormation_security.xml",
        "security/ir.model.access.csv",
        "data/student_sequence.xml",
        "data/mail_template.xml",
        "wizard/terminate_reason_view.xml",
        "views/student_view.xml",
        "views/IDAFormation_view.xml",
        "views/teacher_view.xml",
        "wizard/assign_roll_no_wizard.xml",
        "wizard/move_standards_view.xml",
        "report/report_view.xml",
        "report/identity_card.xml",
        "report/teacher_identity_card.xml",
    ],
    "demo": ["demo/IDAFormation_demo.xml"],
    "assets": {
        "web.assets_backend": ["/IDAFormation/static/src/scss/IDAFormationcss.scss"]
    },
    "installable": True,
    "application": True,
}
