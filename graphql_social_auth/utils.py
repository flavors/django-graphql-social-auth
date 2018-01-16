import re

dashed_to_camel_regex = re.compile(r'(?!^)_([a-zA-Z])')


def dashed_to_camel(dashed_data):
    data = {}
    for key, value in dashed_data.items():
        if isinstance(value, dict):
            value = dashed_to_camel(value)

        dashed_key = dashed_to_camel_regex\
            .sub(lambda match: match.group(1).upper(), key)

        data[dashed_key] = value
    return data
