#!/usr/bin/env python
from typing import Optional

def show_count(count: int, singular: str, plural: Optional[str]=''):
    if count == 1:
        return f'{str(count)} {singular}'
    count_str = str(count) if count else 'no'
    if not plural:
        plural = f'{singular}s'
    return f'{count_str} {plural}'
