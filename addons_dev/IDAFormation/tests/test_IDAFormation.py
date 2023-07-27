# See LICENSE file for full copyright and licensing details.

from odoo.tests import common


class Testcentre(common.TransactionCase):
    def setUp(self):
        super(Testcentre, self).setUp()
        self.student_student_obj = self.env["student.student"]
        self.teacher_obj = self.env["centre.teacher"]
        self.centre_centre_obj = self.env["centre.centre"]
        self.centre_standard_obj = self.env["centre.standard"]
        self.res_company_obj = self.env["res.company"]
        self.assign_roll_obj = self.env["assign.roll.no"]
        self.centre_id = self.env.ref("centre.demo_centre_1")
        self.standard_medium = self.env.ref("centre.demo_standard_medium_1")
        self.year = self.env.ref("centre.demo_academic_year_2")
        self.currency_id = self.env.ref("base.INR")
        self.sch = self.env.ref("centre.demo_centre_1")
        self.country_id = self.env.ref("base.in")
        self.std = self.env.ref("centre.demo_standard_standard_1")
        self.state_id = self.env.ref("base.state_in_gj")
        self.subject1 = self.env.ref("centre.demo_subject_subject_1")
        self.subject2 = self.env.ref("centre.demo_subject_subject_2")
        self.student_student = self.env.ref("centre.demo_student_student_2")
        self.student_done = self.env.ref("centre.demo_student_student_6")
        student_list = [self.student_done.id]
        self.student_student._compute_student_age()
        self.student_student.check_age()
        self.student_student.admission_done()
        self.student_student.set_alumni()
        # Create academic Year
        self.academic_year_obj = self.env["academic.year"]
        self.academic_year = self.academic_year_obj.create(
            {
                "sequence": 7,
                "code": "2012",
                "name": "2012 Year",
                "date_start": "2012-01-01",
                "date_stop": "2012-12-31",
            }
        )
        self.academic_year._check_academic_year()
        self.academic_month_obj = self.env["academic.month"]
        # Academic month created
        self.academic_month = self.academic_month_obj.create(
            {
                "name": "May",
                "code": "may",
                "date_start": "2012-05-01",
                "date_stop": "2012-05-31",
                "year_id": self.academic_year.id,
            }
        )
        self.academic_month._check_year_limit()
        self.assign_roll_no = self.assign_roll_obj.create(
            {"standard_id": self.std.id, "medium_id": self.standard_medium.id}
        )
        self.assign_roll_no.assign_rollno()

    def test_centre(self):
        self.assertEqual(
            self.student_student.centre_id,
            self.student_student.standard_id.centre_id,
        )
