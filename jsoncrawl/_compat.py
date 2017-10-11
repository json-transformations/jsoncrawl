import sys

PY3 = sys.version_info.major == 3

string_type, text_type = (str, str) if PY3 else (str, unicode)
