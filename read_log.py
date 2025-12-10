#!/usr/bin/env python3
"""
Read Nginx log files from a source directory and print them.
This script reads all log files from the specified directory and prints
each line so it can be saved to a database later.
"""

import argparse
import os
from pathlib import Path


def main():
    """Main function to parse arguments and read log files."""
    parser = argparse.ArgumentParser(
        description='Read Nginx log files from a source directory and print them.'
    )
    parser.add_argument(
        '--source',
        type=str,
        required=True,
        help='Path to the directory containing log files (e.g., /var/logs/nginx/access.logs)'
    )
    
    args = parser.parse_args()
    
    print(args.source)


if __name__ == '__main__':
    main()

