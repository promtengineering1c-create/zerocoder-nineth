from sorter import InsertionSorter


def test_insertion_sort():
    # обычный случай
    s = InsertionSorter([3, 1, 2])
    out = s.sort()
    assert out == [1, 2, 3], f"не отсортировалось: {out}"
    assert out is not s._data, "sort вернул ссылку на внутренний список"
    assert s.data == [3, 1, 2], f"исходный изменён: {s.data}"

s = InsertionSorter([-3, 5, 0, -8, 1, 10])
print(s.sort())    