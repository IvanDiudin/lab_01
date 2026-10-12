from toolkit.errors import ConversionError
LENGTH_TO_METERS = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0}
MASS_TO_KG = {"g": 0.001, "kg": 1.0}
def convert(value: float, from_unit: str, to_unit: str) -> float:
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    group_from = ""
    if from_unit in LENGTH_TO_METERS:
        group_from = "length"
    elif from_unit in MASS_TO_KG:
        group_from = "mass"
    elif from_unit in ["c", "f", "k"]:
        group_from = "temperature"
    else:
        raise ConversionError(f"Неизвестная единица: {from_unit}")
    group_to = ""
    if to_unit in LENGTH_TO_METERS:
        group_to = "length"
    elif to_unit in MASS_TO_KG:
        group_to = "mass"
    elif to_unit in ["c", "f", "k"]:
        group_to = "temperature"
    else:
        raise ConversionError(f"Неизвестная единица: {to_unit}")
    if group_from != group_to:
        raise ConversionError(f"Нельзя конвертировать {from_unit} в {to_unit}")
    if group_from == "length":
        value_in_meters = value * LENGTH_TO_METERS[from_unit]
        result = value_in_meters / LENGTH_TO_METERS[to_unit]
        return float(result)
    elif group_from == "mass":
        value_in_kg = value * MASS_TO_KG[from_unit]
        result = value_in_kg / MASS_TO_KG[to_unit]
        return float(result)
    elif group_from == "temperature":
        if from_unit == "c":
            celsius = value
        elif from_unit == "f":
            celsius = (value - 32) * 5 / 9
        elif from_unit == "k":
            celsius = value - 273.15
        if celsius < -273.15:
            raise ConversionError("Температура ниже абсолютного нуля")
        if to_unit == "c":
            result = celsius
        elif to_unit == "f":
            result = celsius * 9 / 5 + 32
        elif to_unit == "k":
            result = celsius + 273.15
        return float(result)
    return 0.0