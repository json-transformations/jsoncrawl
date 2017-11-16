import sys

PY3 = sys.version_info.major == 3

string_type, text_type = (str, str) if PY3 else (str, unicode)
int_type, long_type = (int, int) if PY3 else (int, long)
