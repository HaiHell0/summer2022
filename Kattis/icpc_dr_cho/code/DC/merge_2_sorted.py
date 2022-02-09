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


if __name__ == "__main__":
    print(mergeLists([1, 5, 6], [2, 7, 8]))
    print(mergeLists([1, 5, 6], None))
