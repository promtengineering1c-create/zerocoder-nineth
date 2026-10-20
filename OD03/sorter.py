from abc import ABC, abstractmethod
from typing import TypeAlias

Number: TypeAlias = int # | float


class Sorter(ABC):
    def __init__(self, data: list[Number]) -> None:
        self._data: list[Number] = list(data)
    
    @abstractmethod
    def sort(self) -> list[Number]:
        """Возвращает новый отсортированный список. Исходный не изменяется."""

    @property
    def data(self) -> list[Number]:
        return self._data    

class BubbleSorter(Sorter):
    def sort(self) -> list[Number]:
        result = list(self._data)
        n = len(result)
        for run in range(n - 1):
            for i in range(n - 1 - run):
                if result[i] > result[i + 1]:
                    result[i], result[i + 1] = result[i + 1], result[i]

        return result


class QuickSorter(Sorter):
    def sort(self) -> list[Number]:
        return self._quick_sort(list(self._data))

    def _quick_sort(self, result: Number) -> list[Number]:
        if len(result) <= 1:
            return result
            
        pivot = result[0]
        left, center, right = [], [], []
        for x in result:
            if x < pivot:
                left.append(x)
            elif x > pivot:
                right.append(x)
            else:
                center.append(x)

        return self._quick_sort(left) + center + self._quick_sort(right)


class SelectionSorter(Sorter):
    def sort(self) -> list[Number]:
        result = list(self._data)
        
        n = len(result)
        for i in range(n):

            min_index = i
            for j in range(i + 1, n):
                if result[j] < result[min_index]:
                    min_index = j

            result[i], result[min_index] = result[min_index], result[i]

        return result 


class InsertionSorter(Sorter):
    def sort(self) -> list[Number]:
        result = list(self._data)
        
        n = len(result)
        for i in range(1, n):
            key = result[i]
            j = i - 1

            while j >= 0 and result[j] > key:
                result[j + 1] = result[j]
                j -= 1

            result[j + 1] = key   

        return result