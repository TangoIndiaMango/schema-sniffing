class SchemaTypes:
    extra_attrs = {"type": "", "tag": "", "description": "", "required": False}

    def __init__(self, value):
        self.value = value

    def detect_type(self, type):
        type_attributes = {"type": type}
        return {**self.extra_attrs, **type_attributes}

    def detect_string(self):
        return self.detect_type("string")

    def detect_integer(self):
        return self.detect_type("integer")

    def detect_boolean(self):
        return self.detect_type("boolean")

    def detect_enum(self):
        return self.detect_type("enum")

    def detect_array(self, item_type):
        array_attributes = {"type": "array", "items": item_type}
        return {**self.extra_attrs, **array_attributes}


# schema_types = SchemaTypes("contact")
# string_attributes = schema_types.detect_string()
# print(string_attributes)
