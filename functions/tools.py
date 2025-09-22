from find_video import find_video

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
        }
    ]

    TOOLS_MAP = {"find_video": find_video}

    return TOOLS, TOOLS_MAP