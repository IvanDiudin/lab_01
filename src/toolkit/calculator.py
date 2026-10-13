from toolkit.errors import CalculatorError


def tokenize(expression: str) -> list:
    tokens = []
    i = 0
    current_number = ""
    while i < len(expression):
        char = expression[i]
        if char == " ":
            i = i + 1
            continue
        elif char.isdigit() or char == ".":
            current_number = current_number + char
            i = i + 1
        elif char in "+-*/":
            if (
                current_number == ""
                and (len(tokens) == 0 or tokens[-1] in "+-*/")
                and (char == "-" or char == "+")
            ):
                current_number = char
                i = i + 1
                continue
            if current_number == "" and len(tokens) > 0 and tokens[-1] in "+-*/":
                raise CalculatorError("Два оператора подряд")
            if current_number != "":
                tokens.append(current_number)
                current_number = ""
            tokens.append(char)
            i = i + 1
        else:
            raise CalculatorError(f"Недопустимый символ: {char}")

    if current_number != "":
        tokens.append(current_number)

    return tokens


def calculate(expression: str) -> float:
    tokens = tokenize(expression)

    if len(tokens) == 0:
        raise CalculatorError("Пустое выражение")

    i = 0
    while i < len(tokens):
        if tokens[i] == "*" or tokens[i] == "/":
            if tokens[i] == "*":
                result = float(tokens[i - 1]) * float(tokens[i + 1])
            else:
                if float(tokens[i + 1]) == 0:
                    raise CalculatorError("Деление на ноль")
                result = float(tokens[i - 1]) / float(tokens[i + 1])
            del tokens[i - 1 : i + 2]
            tokens.insert(i - 1, str(result))
        else:
            i = i + 1

    i = 0
    while i < len(tokens):
        if tokens[i] == "+" or tokens[i] == "-":
            if tokens[i] == "+":
                result = float(tokens[i - 1]) + float(tokens[i + 1])
            else:
                result = float(tokens[i - 1]) - float(tokens[i + 1])
            del tokens[i - 1 : i + 2]
            tokens.insert(i - 1, str(result))
        else:
            i = i + 1

    return float(tokens[0])
