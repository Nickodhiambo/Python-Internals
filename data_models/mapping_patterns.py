#!/,usr/bin/env python

def match_case(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'author': [*names]}:
            return [names]

        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]

        case {'type': 'book'}:
            raise ValueError(f'Invalid book record: {record}')

        case _:
            raise ValueError('Invalid record')

