
#!usr/bin/env python3
import unittest
from emails import find_email

class EmailsTest(unittest.TestCase):
        def test_basic(self):#no argv o primeiro parametro e o sript file
                testcase = [None,"Bree","Campbell"]#como o metodo find_email ja foi importado
                expected = "breee@abc.edu"#o primeiro parametro vai ser none ja que o metodo ja vai ser chamado no teste
                self.assertEqual(find_email(testcase),expected)


        def test_one_name(self):
                testcase = [None,"John"]
                expected = "Missing parameters"
                self.assertEqual(find_email(testcase),expected)

        def test_two_name(self):
                testcase = [None,"Roy","Cooper"]
                expected = "No email address found"
                self.assertEqual(find_email(testcase),expected)

if __name__ == '__main__':
        unittest.main()
