from functions.find_video import find_video
from functions.write_file import write_file

def get_tools():
    TOOLS = [
        {
            "type": "function",
            "name": "find_video",
            "description": "Search YouTube and return up to N results as title+url. "
                        "Use this for finding videos to match the user's request.",
            "parameters": {
                "type": "object",
                "properties": {
                    "search_query": {"type": "string", "description": "Search terms"},
                },
                "required": ["search_query"]
            }
        },

        {
            "type": "function",
            "name": "write_file",
            "description": "writes a lesson summary to a file with appropriate markdown. File contents matches lesson summary structure",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {"type": "string", "description": "name of the file to write to"},
                    "content": {"type": "string", "description": "lesson summary content to write in the file"}
                },
                "required": ["filename", "content"]
            }
        }
    ]

    TOOLS_MAP = {"find_video": find_video, "write_file": write_file}

    return TOOLS, TOOLS_MAP