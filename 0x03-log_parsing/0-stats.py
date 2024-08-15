#!/usr/bin/env python3
"""
Log parsing
"""
import sys
import re
from collections import defaultdict


def print_stats(total_size, status_codes):
    """
    Print the computed statistics.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    """
    Main function
    """
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0
    pattern = r'^\S+ - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'

    try:
        for line in sys.stdin:
            line = line.strip()
            match = re.match(pattern, line)
            if match:
                status_code = int(match.group(1))
                file_size = int(match.group(2))
                total_size += file_size
                status_codes[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
