def older_than_27():
    import sys
    return True if sys.version_info[:2] < (2, 7) else False