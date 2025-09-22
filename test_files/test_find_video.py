import unittest
import os
from functions.find_video import find_video, get_credentials



class TestFindVideo(unittest.TestCase):

    def test_video_generation(self):
        response = find_video("cells")
        self.assertTrue(
            any("https://www.youtube.com/watch" in url for url in [v["url"] for v in response])
        )

        self.assertIn("cells", response[0]["description"])

    def test_api_key(self):
        key = get_credentials
        self.assertTrue(key != None)       


        




if __name__ == "__main__":
    unittest.main()