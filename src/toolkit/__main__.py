import argparse
import sys

from toolkit.calculator import calculate
from toolkit.converter import convert
from toolkit.errors import ToolkitError


def main():
    parser = argparse.ArgumentParser(prog="toolkit")
    subparsers = parser.add_subparsers(dest="command")
    calc_parser = subparsers.add_parser("calc")
    calc_parser.add_argument("expression")
    conv_parser = subparsers.add_parser("convert")
    conv_parser.add_argument("value", type=float)
    conv_parser.add_argument("--from", dest="from_unit", required=True)
    conv_parser.add_argument("--to", dest="to_unit", required=True)
    args = parser.parse_args()
    try:
        if args.command == "calc":
            result = calculate(args.expression)
            print(result)
        elif args.command == "convert":
            result = convert(args.value, args.from_unit, args.to_unit)
            print(result)
        else:
            parser.print_help()
            sys.exit(0)
    except ToolkitError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(2)
if __name__ == "__main__":
    main()