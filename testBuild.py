import unittest
import subprocess
from testSuite_1_1.testCases.TestCase_1415 import TestCase_1415
from testSuite_1_1.testCases.TestCase_1416 import TestCase_1416
from testSuite_1_1.testCases.TestCase_1417 import TestCase_1417
from testSuite_1_1.testCases.TestCase_1418 import TestCase_1418
from testSuite_1_1.testCases.TestCase_1419 import TestCase_1419

def check_packages():
    update = subprocess.run('apt-get -y update'.split(), stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                         shell=False, encoding='utf-8')
    if update.returncode != 0:
        return update.stderr
    else:
         packages = ['gimp', 'vlc', 'vim-console', 'xorg-xvfb', 'pip']
         f = open("cat.txt", 'w')
         for i in range(len(packages)):
             # cmd = ['grep', packages[i]]
             # input = open("cat.txt")
             # grep = subprocess.run(cmd, stdin=input, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
             #                       encoding='utf-8')
             # input.close()
             # if len(grep.stdout.split('\n')[0]) != packages[i]:
             print(f"Installing package {packages[i]}")
             install = subprocess.run(f'apt-get install -y --force-yes {packages[i]}'.split(), stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE,
                                      encoding='utf-8')
             if install.returncode != 0:
                 return install.stderr
         cmd = ['rm', 'cat.txt']
         subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, encoding='utf-8')
         return "Все пакеты успешно установлены"


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCase_1415('test_firefox'))
    suite.addTest(TestCase_1415('test_gimp'))
    suite.addTest(TestCase_1415('test_vlc'))
    suite.addTest(TestCase_1415('test_vim'))
    suite.addTest(TestCase_1416('test_ip_link'))
    suite.addTest(TestCase_1416('test_cat'))
    suite.addTest(TestCase_1416('test_down'))
    suite.addTest(TestCase_1416('test_is_up'))
    suite.addTest(TestCase_1416('test_interrupts'))
    suite.addTest(TestCase_1417('test_create_file'))
    suite.addTest(TestCase_1417('test_buffer'))
    suite.addTest(TestCase_1417('test_delete_file'))
    suite.addTest(TestCase_1418('test_view_list'))
    suite.addTest(TestCase_1418('test_file_creation'))
    suite.addTest(TestCase_1418('test_file_copy'))
    suite.addTest(TestCase_1418('test_recursion_copy'))
    suite.addTest(TestCase_1418('test_move_file'))
    suite.addTest(TestCase_1418('test_remove_file'))
    suite.addTest(TestCase_1418('test_remove_catalog'))
    suite.addTest(TestCase_1418('test_search_validation'))
    suite.addTest(TestCase_1419('test_add'))
    suite.addTest(TestCase_1419('test_change_password_testuser'))
    suite.addTest(TestCase_1419('test_prohibition_of_change'))
    suite.addTest(TestCase_1419('test_check_change_passwd_with_root'))
    suite.addTest(TestCase_1419('test_delete_data'))
    return suite

if __name__ == '__main__':
    # print("Проверка пакетов...")
    # print(check_packages())
    unittest.TextTestRunner(verbosity=2).run(suite())
    # test_files = glob.glob('test_*.py')
    # module_strings = [test_file[0:len(test_file) - 3] for test_file in test_files]
    # suites = [unittest.defaultTestLoader.loadTestsFromName(test_file) for test_file in module_strings]
    # test_suite = unittest.TestSuite(suites)
    # test_runner = unittest.TextTestRunner().run(test_suite)