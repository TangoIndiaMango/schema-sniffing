
extra_attrs = {"type": "", "tag": "", "description": "", "required": False}


def detect_string(value):
    string_attributes = {"type": "string"}
    return {**extra_attrs, **string_attributes}


def detect_integer(value):
    integer_attributes = {"type": "integer"}
    return {**extra_attrs, **integer_attributes}


def detect_boolean(value):
    boolean_attributes = {"type": "boolean"}
    return {**extra_attrs, **boolean_attributes}


def detect_enum(value):
    enum_attributes = {"type": "enum"}
    return {**extra_attrs, **enum_attributes}


def detect_array(value, item_type):
    array_attributes = {"type": "array", "items": item_type}
    return {**extra_attrs, **array_attributes}



# print(detect_string(int))
