import logging

from django.utils.six import StringIO
from django.test import TestCase

from students.models import Student
from students import signals

class StudentSignalsests(TestCase):

    def test_log_student_updated_added_event(self):
        """Check logging signal for newly created dtudent"""
        # add own root handler to catch student signals output
        out = StringIO()
        handler = logging.StreamHandler(out)
        logging.root.addHandler(handler)

        # now create student, this should raise new message inside our logger output file
        student = Student(first_name='Demo', last_name='Student')
        student.save()

        # check output file content
        out.seek(0)
        self.assertEqual(out.readlines()[-1],
                         'Student added: Demo Student (ID: %d)\n' % student.id)

        # now update existing student and check last line in out
        student.ticket = '12345'
        student.save()
        out.seek(0)
        self.assertEqual(out.readlines()[-1],
                         'Student updated: Demo Student (ID: %d)\n' % student.id)

        # remove our handler from root logger
        logging.root.removeHandler(handler)