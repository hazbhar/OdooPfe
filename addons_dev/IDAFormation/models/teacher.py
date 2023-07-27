# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class centreTeacher(models.Model):
    """Defining a Teacher information."""

    _name = "centre.teacher"
    _description = "Teacher Information"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    employee_id = fields.Many2one(
        "hr.employee",
        "Employee ID",
        ondelete="cascade",
        delegate=True,
        required=True,
        help="Enter related employee",
    )
    standard_id = fields.Many2one(
        "centre.standard",
        "Responsibility of Group",
        help="Standard for which the teacher responsible for.",
    )
    stand_id = fields.Many2one(
        "standard.standard",
        "Course",
        related="standard_id.standard_id",
        store=True,
        help="""Select standard which are assigned to teacher""",
    )
    subject_id = fields.Many2many(
        "subject.subject",
        "subject_teacher_rel",
        "teacher_id",
        "subject_id",
        "Course-Subjects",
        help="Select subject of teacher",
    )
    centre_id = fields.Many2one(
        "centre.centre", "Campus", help="Select centre"
    )
    category_ids = fields.Many2many(
        "hr.employee.category",
        "teacher_category_rel",
        "emp_id",
        "categ_id",
        "Tags",
        help="Select employee category",
    )
    department_id = fields.Many2one(
        "hr.department", "Department", help="Select department"
    )

    phone_numbers = fields.Char("Phone Number", help="Student PH no")

    @api.onchange("standard_id")
    def _onchange_standard_id(self):
        for rec in self:
            rec.centre_id = (
                rec.standard_id
                and rec.standard_id.centre_id
                and rec.standard_id.centre_id.id
                or False
            )

    @api.model
    def create(self, vals):
        """Inherited create method to assign value to users for delegation"""
        teacher_id = super(centreTeacher, self).create(vals)
        user_obj = self.env["res.users"]
        user_vals = {
            "name": teacher_id.name,
            "login": teacher_id.work_email,
            "email": teacher_id.work_email,
        }
        ctx_vals = {
            "teacher_create": True,
            "centre_id": teacher_id.centre_id.company_id.id,
        }
        user_rec = user_obj.with_context(ctx_vals).create(user_vals)
        teacher_id.employee_id.write({"user_id": user_rec.id})

        return teacher_id

    @api.onchange("address_id")
    def onchange_address_id(self):
        """Onchange method for address."""
        if self.address_id:
            self.work_phone = (self.address_id.phone or False,)
            self.mobile_phone = self.address_id.mobile or False

    @api.onchange("department_id")
    def onchange_department_id(self):
        """Onchange method for deepartment."""
        self.parent_id = (
            self.department_id
            and self.department_id.manager_id
            and self.department_id.manager_id.id
        ) or False

    @api.onchange("user_id")
    def onchange_user(self):
        """Onchange method for user."""
        if self.user_id:
            self.name = self.name or self.user_id.name
            self.work_email = self.user_id.email
            self.image = self.image or self.user_id.image

    @api.onchange("centre_id")
    def onchange_centre(self):
        """Onchange method for centre."""
        partner = self.centre_id.company_id.partner_id
        self.address_id = partner.id or False
        self.mobile_phone = partner.mobile or False
        self.work_location_id = partner.id or False
        self.work_email = partner.email or False
        phone = partner.phone or False
        self.work_phone = phone or False
        self.phone_numbers = phone or False
