from sorter import SelectionSorter


def test_selection_sort():
    s = SelectionSorter([3, 1, 2])
    out = s.sort()
    assert out == [1, 2, 3], f"не отсортировалось: {out}"      # поймал бы `>`
    assert out is not s._data, "sort вернул ссылку на внутренний список"
    assert s.data == [3, 1, 2], f"исходный изменён: {s.data}"

s = SelectionSorter([64, 25, 12, 22, 11])
print(s.sort())