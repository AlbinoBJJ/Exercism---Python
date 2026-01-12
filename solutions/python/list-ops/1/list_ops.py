def append(list1, list2):
    return list1 + [item for item in list2]


def concat(lists):
    return [item for list_ in lists for item in list_]


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    return len(list)


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    acc = initial
    for item in list:
        acc = function(acc, item)
    return acc


def foldr(function, list, initial):
    return initial if not list else function(foldr(function, list[1:], initial), list[0])


def reverse(list):
    return list[::-1]
