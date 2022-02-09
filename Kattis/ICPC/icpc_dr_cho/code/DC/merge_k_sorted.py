def mergeKLists(lists):
    result = []

    def mergeLists(l1, l2):
        if not l1 or len(l1) == 0:
            result.extend(l2)
            return result
        if not l2 or len(l2) == 0:
            result.extend(l1)
            return result

        if l1[0] < l2[0]:
            result.append(l1[0])
            mergeLists(l1[1:], l2)
        else:
            result.append(l2[0])
            mergeLists(l1, l2[1:])
        return result

    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            result = []  # clear the result for mergeLists method
            merged.append(mergeLists(l1, l2))
        lists = merged

    return lists[0]


if __name__ == "__main__":
    print(mergeKLists([[1, 5, 6], [2, 7, 8], [0, 3, 9, 11]]))
