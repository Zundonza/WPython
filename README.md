# WPython
Развлекательный проект, который сокращает ключевые слова Python.

Существует два режима:
```
Python  -> WPython
WPython -> Python
```

Например, вот несколько сокращённых ключевых слов:
```
continue -> cnt
class -> cls
else -> es
await -> awt
```
<details>
    <summary>Несокращённый код</summary>
    
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
</details>

<details>
  <summary>Сокращённый код</summary>
  
    imp math as m
    imp asyncio
    
    df process_data(data):
        if data is N:
            rt N
        
        tr:
            if isinstance(data, str):
                rt len(data)
            
            el isinstance(data, (int, float)):
                result = data ** 2
                if result > 1000:
                    rs ValueError("Слишком большое число!")
                
                rt result
            
            es:
                rs TypeError("Неподдерживаемый тип данных!")
        ex ValueError as ve:
            prt(f"Ошибка значения: {ve}")
            rt -1
        ex Exception as exe:
            prt(f"Ошибка: {exe}")
            rt -1
        fnl:
            prt("Завершение обработки данных.")
    
    ayc df async_task():
        prt("Начинаем асинхронную операцию...")
        awt asyncio.sleep(2)
        prt("Асинхронная операция завершена.")
        rt T
    
    cls DataProcessor:
        df __init__(self):
            self.data = []
    
        df add_data(self, item):
            glb added
            if item nt in self.data:
                self.data.append(item)
                added = T
            es:
                added = F
        
        df display_data(self):
            prt("Текущие данные:", self.data)
        
        df filter_data(self):
            self.data = [item fr item in self.data if isinstance(item, (int, float)) a item > 0]
        
        df calculate_total(self):
            total = sum(self.data)
            rt total
    
    df main():
        processor = DataProcessor()
        
        fr item in [N, "Привет", 5, -3.5, 42, "Python"]:
            if isinstance(item, (int, float)) a item >= 0:
                processor.add_data(item)
        
        processor.display_data()
        processor.filter_data()
        total = processor.calculate_total()
        
        prt(f"Сумма положительных чисел: {total}")
    
        square = lb x: x ** 2
        prt(f"Квадрат 3: {square(3)}")
    
        tr:
            asyncio.run(async_task())
        ex RuntimeError as re:
            prt(f"Асинхронная ошибка: {re}")
    
        wh T:
            response = inp("Введите число (или 'exit' для выхода): ")
            if response == "exit":
                brk
            tr:
                value = float(response)
                result = process_data(value)
                prt(f"Результат обработки: {result}")
            ex:
                prt("Ошибка: введите корректное число.")
                cnt
    
    if __name__ == "__main__":
        main()
</details>

Аргументы программы:
```
--debug       Режим отладки
--print-words Напечатать все сокращения
--to-wpy      Включить режим Python -> WPython (другой по дефолту)
--save-file   Сохраняет файл, получившийся при переводе из одного формата в другой
--auto-exec   Выполнять файл после перевода форматов. Нет смысла при параметре --to-wpy
```

Использование:
```
python3 wpi.py <file> <args>
```
