#!/usr/bin/env python3
import sys
import traceback

def format_exception():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    tb_lines = [line.rstrip('\n') for line in
                traceback.format_exception(exc_type, exc_value, exc_traceback)]
    return "\n".join(tb_lines)
