import math as m
import asyncio

def process_data(data):
    if data is None:
        return None
    
    try:
        if isinstance(data, str):
            return len(data)
        
        elif isinstance(data, (int, float)):
            result = data ** 2
            if result > 1000:
                raise ValueError("Слишком большое число!")
            
            return result
        
        else:
            raise TypeError("Неподдерживаемый тип данных!")
    except ValueError as ve:
        print(f"Ошибка значения: {ve}")
        return -1
    except Exception as exe:
        print(f"Ошибка: {exe}")
        return -1
    finally:
        print("Завершение обработки данных.")

async def async_task():
    print("Начинаем асинхронную операцию...")
    await asyncio.sleep(2)
    print("Асинхронная операция завершена.")
    return True

class DataProcessor:
    def __init__(self):
        self.data = []

    def add_data(self, item):
        global added
        if item not in self.data:
            self.data.append(item)
            added = True
        else:
            added = False
    
    def display_data(self):
        print("Текущие данные:", self.data)
    
    def filter_data(self):
        self.data = [item for item in self.data if isinstance(item, (int, float)) and item > 0]
    
    def calculate_total(self):
        total = sum(self.data)
        return total

def main():
    processor = DataProcessor()
    
    for item in [None, "Привет", 5, -3.5, 42, "Python"]:
        if isinstance(item, (int, float)) and item >= 0:
            processor.add_data(item)
    
    processor.display_data()
    processor.filter_data()
    total = processor.calculate_total()
    
    print(f"Сумма положительных чисел: {total}")

    square = lambda x: x ** 2
    print(f"Квадрат 3: {square(3)}")

    try:
        asyncio.run(async_task())
    except RuntimeError as re:
        print(f"Асинхронная ошибка: {re}")

    while True:
        response = input("Введите число (или 'exit' для выхода): ")
        if response == "exit":
            break
        try:
            value = float(response)
            result = process_data(value)
            print(f"Результат обработки: {result}")
        except:
            print("Ошибка: введите корректное число.")
            continue

if __name__ == "__main__":
    main()
