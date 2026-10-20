from sorter import QuickSorter


def test_quick_sort():
    s = QuickSorter([3, 1, 2, 1, 3])
    out = s.sort()
    assert out == [1, 1, 2, 3, 3], f"не отсортировалось: {out}"
    assert out is not s._data, "sort вернул ссылку на внутренний список"
    assert s.data == [3, 1, 2, 1, 3], f"исходный изменён: {s.data}"

s = QuickSorter([5, 2, 9, 0, 1, 5, 3])  
print(s.sort())  