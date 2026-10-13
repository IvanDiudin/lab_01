# Lab 01: Консольный набор утилит
Python-пакет с CLI для вычисления математических выражений и конвертации единиц измерения.
## Установка
pip install -e .
## Использование
### Калькулятор
python -m toolkit calc "2 + 3 * 4"
14.0
### Конвертер
python -m toolkit convert 1000 --from mm --to m
1.0
### Справка
python -m toolkit --help
## Тесты
python -m pytest tests/ -v
## Автор
Дюдин Иван Сергеевич группа М80-102БВ-26