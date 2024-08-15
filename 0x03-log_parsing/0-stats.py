#!/usr/bin/python3
"""
log parsing
"""
import sys


def display_metrics(total_bytes: int, code_frequency: dict) -> None:
    """
    Display the computed metrics.
    """
    print(f"File size: {total_bytes}")
    for code, frequency in sorted(code_frequency.items()):
        if frequency > 0:
            print(f"{code}: {frequency}")


def process_logs():
    """
    Main function to process log entries and compute metrics.
    """
    total_bytes = 0
    entry_count = 0
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    code_frequency = {code: 0 for code in valid_codes}

    try:
        for log_entry in sys.stdin:
            entry_count += 1
            parts = log_entry.split()

            if len(parts) > 2:
                status = parts[-2]
                if status in code_frequency:
                    code_frequency[status] += 1

            try:
                total_bytes += int(parts[-1])
            except (IndexError, ValueError):
                pass

            if entry_count % 10 == 0:
                display_metrics(total_bytes, code_frequency)

        display_metrics(total_bytes, code_frequency)

    except KeyboardInterrupt:
        display_metrics(total_bytes, code_frequency)
        raise


if __name__ == "__main__":
    process_logs()
