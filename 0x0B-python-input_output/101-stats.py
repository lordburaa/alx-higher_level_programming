#!/usr/bin/python3
"""Reads from standard input """


def print_stats(size, status_code):
    """print accumulate metrixa
    """
    print("File size: {}".format(size))
    for key in sorted(status_code):
        print("{}: {}".format(key, status_code[key]))

if __name__ == "__main__":
    import sys

    size = 0
    status_code = {}
    valid_code = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 0:
                print_stats(size, status_code)
                count =  1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_code:
                    if status_code.get(line[-2], -1) == -1:
                        status_code[line[-2]] = 1
                    else:
                        status_code[line[-2]] += 1
            except IndexError:
                pass
        print_stats(size, status_code)
    except KeyboardInterrupt:
        print_stats(size, status_code)
        raise
