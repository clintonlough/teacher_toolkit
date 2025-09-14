import unittest
import os
from io import StringIO
from contextlib import redirect_stdout
from functions.main import print_cost, _get_client, gpt_model

RUN_LIVE = os.getenv("OPENAI_LIVE") == "1"

@unittest.skipUnless(RUN_LIVE, "Set OPENAI_LIVE=1 to run live OpenAI tests")
class TestOpenAILive(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
    # Will raise if OPENAI_API_KEY missing (as your _get_client does)
        cls.client = _get_client()
    
    def test_conversation(self):
        messages = [
                    {"role": "developer", "content": "Reply with ≤5 words."},
                    {"role": "user", "content": "Say hello"},
                ]
        resp = self.client.responses.create(
            model=gpt_model,
            input=messages,
            temperature=0,
        )
        txt = resp.output_text.strip()
        self.assertLessEqual(len(txt.split()), 5)
        self.assertTrue(txt)  # not empty


class TestMain(unittest.TestCase):
    def test_verbose_cost(self):
        buf = StringIO()
        with redirect_stdout(buf):
            print_cost(True, 20, 40, 60)
        s = buf.getvalue()
        lines = s.strip().splitlines()
        self.assertEqual(lines[0], "Input tokens: 20")
        self.assertEqual(lines[1], "Output tokens: 40")
        self.assertEqual(lines[2], "Total tokens: 60")
        self.assertTrue(lines[3].startswith("Estimated cost is USD $"))

        
    
        











if __name__ == "__main__":
    unittest.main()