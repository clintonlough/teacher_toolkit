import unittest
import os
from functions.write_file import write_file



class TestWriteFile(unittest.TestCase):

    def test_read_write_file(self):
        filename = "test.txt"
        content = "this is unit-test content"

        full_path = "lesson_plans"
        file_path = os.path.join(full_path,filename)
        abs_path = os.path.abspath(file_path)

        write_file(filename, content)

        with open(abs_path, 'r') as f:
            test_content = f.read()

        self.assertEqual(test_content,content)     


        




if __name__ == "__main__":
    unittest.main()