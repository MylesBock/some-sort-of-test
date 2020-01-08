import json
"""
problem one
---
Given some malformed json and a valid equivalent
 write a function to transform the malformed json to the valid equivalent
 
Requirements:
only one import is allowed (json)
all tests in `test/test_problem_one.py` must pass with pytest (see README.md)
"""


class ProblemOne:
    def __init__(self):
        pass

    # solution credit to: https://github.com/brianforan
    @staticmethod
    def transform_me(data):
        for cluster in data["clusters"]:
            cluster["cluster"] = {
                "server": cluster["server"],
                "insecure-skip-tls-verify": cluster["insecure-skip-tls-verify"]
            }
            del cluster["server"]
            del cluster["insecure-skip-tls-verify"]

        for context in data["contexts"]:
            context["context"] = {
                "cluster": context["cluster"],
                "namespace": context["namespace"],
                "user": context["user"]
            }
            del context["cluster"]
            del context["namespace"]
            del context["user"]

        data["users"] = [data["users"]]            
        
        return data
