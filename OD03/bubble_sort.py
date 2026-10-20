from sorter import BubbleSorter


def test_bubble():
    s = BubbleSorter([3, 1, 2])
    out = s.sort()
    assert out == [1, 2, 3], f"не отсортировалось: {out}"
    assert s.data == [3, 1, 2], f"исходный изменён: {s.data}"  

s = BubbleSorter([5, 7, 4, 3, 8, 2])
print(s.sort())    
    