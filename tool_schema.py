TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current system time",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "calculate_area",
            "description": "Calculate area of a rectangle using length and width",
            "parameters": {
                "type": "object",
                "properties": {
                    "length": {
                        "type": "number",
                        "description": "Length of rectangle"
                    },
                    "width": {
                        "type": "number",
                        "description": "Width of rectangle"
                    }
                },
                "required": ["length", "width"]
            }
        }
    },

    {
        "type":"function",
        "function":{
            "name":"read_file",
            "description":"Read the contents of a text file and return the information present in it.",
            "parameters":{
                "type":"object",
                "properties":{
                    "filename":{
                        "type":"string",
                        "description":"Name of the file to read"
                    }
                },
                "required":["filename"]
            }
        }
    }
]
