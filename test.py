import unittest
import json
from schema_format import generate_schema


class TestGenerateSchema(unittest.TestCase):

    def test_generate_schema(self):
        sample_data = {
            "message": {
                "status": "ABCDEFGHIJKL",
                "creationTime": 240,
                "startTime": 626,
                "endTime": 353,
                "creator": {
                    "id": "ABCDEFGHIJKLMNOPQRSTUVWXYZA",
                    "nickname": "ABCDEFGHIJKLMNOPQ",
                    "title": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                    "accountType": "ABCDE",
                    "countryCode": "ABCD",
                    "orientation": "ABCDEFGHIJKLMNO"
                },
                "participants": [
                    {
                        "user": {
                            "id": "ABCDEFGHIJKLMN",
                            "nickname": "ABCDEFGHIJKLMN",
                            "title": "ABCDEFGHIJK",
                            "accountType": "ABCDEFGHIJKLMNOPQRSTUVWX",
                            "countryCode": "ABCDEFGH",
                            "orientation": "ABCDEFGHIJKLMNOPQRSTUVWXY"
                        },
                        "creator": False,
                        "ranking": 498,
                        "numberOfTrades": 862,
                        "performance": "ABCDEFGHIJKLMNOPQRSTUVW"
                    }
                ],
                "participantIds": [
                    "ABCDEFGHIJKLMNOPQRST",
                    "ABCDEFGHIJKLMNOPQRSTUVWXY"
                ]
            }
        }

        # Write the sample data to a temporary JSON file
        with open("sample.json", "w") as f:
            json.dump(sample_data, f)

        # Generate a schema
        generate_schema("sample.json", "sample_schema.json")

        # Read the generated schema
        with open("sample_schema.json", "r") as f:
            generated_schema = json.load(f)

        # Define the expected schema based on the sample data
        expected_schema = expected_schema = {
            'type': 'array',
            'tag': '',
            'description': '',
            'required': False,
            'status': {
                'type': 'string',
                'tag': '',
                'description': '',
                'required': False
            },
            'creationTime': {
                'type': 'integer',
                'tag': '',
                'description': '',
                'required': False
            },
            'startTime': {
                'type': 'integer',
                'tag': '',
                'description': '',
                'required': False
            },
            'endTime': {
                'type': 'integer',
                'tag': '',
                'description': '',
                'required': False
            },
            'creator': {
                'type': 'array',
                'tag': '',
                'description': '',
                'required': False,
                'id': {
                    'type': 'string',
                    'tag': '',
                    'description': '',
                    'required': False
                },
                'nickname': {
                    'type': 'string',
                    'tag': '',
                    'description': '',
                    'required': False
                },
                'title': {
                    'type': 'string',
                    'tag': '',
                    'description': '',
                    'required': False
                },
                'accountType': {
                    'type': 'string',
                    'tag': '',
                    'description': '',
                    'required': False
                },
                'countryCode': {
                    'type': 'string',
                    'tag': '',
                    'description': '',
                    'required': False
                },
                'orientation': {
                    'type': 'string',
                    'tag': '',
                    'description': '',
                    'required': False
                }
            },
            'participants': {
                'type': 'array',
                'items': {
                    'type': 'array'
                },
                'tag': '',
                'description': '',
                'required': False
            },
            'participantIds': {
                'type': 'enum',
                'tag': '',
                'description': '',
                'required': False
            }
        }

        self.maxDiff = None
        print(generated_schema)
        print("==============")

        print("==============")
        print(expected_schema)

        self.assertEqual(generated_schema, expected_schema)


if __name__ == '__main__':
    unittest.main()
