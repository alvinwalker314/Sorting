def selection_sort( arr ):
    if len(arr) == 0:
        return arr
    else:
        iterations = len(arr)
        c_index = 0
        m_index = 0
        while c_index < iterations:
            m_index = c_index
            for i in range(c_index + 1, iterations):
                if arr[m_index] >= arr[i]:
                    m_index = i
                else:
                    continue
            arr[c_index], arr[m_index] = arr[m_index] , arr[c_index]
            c_index += 1
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    if len(arr) == 0:
        return arr
    else:
        iterations = len(arr)
        current = iterations
        while current != 0:
            for i in range(current):
                if i == current - 1:
                    pass
                else:
                    if arr[i] >= arr[i+1]:
                        arr[i] , arr[i+1] = arr[i+1], arr[i]
                    else:
                        pass
            current -= 1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort_with_neg( arr ):
    if len(arr) == 0:
        return arr
    else:
        uniques = {x: 0 for x in range(min(arr), max(arr)+ 1)}
        keys = [x for x in uniques.keys()]
        print(f"Dictionary before counting: {uniques}")
        for x in arr:
            uniques[x] += 1
            print(f"Dictionary after counting: {uniques}")
        for num, key in enumerate(keys):
            if num != len(keys) - 1:
                uniques[keys[num + 1]] += uniques[key]
            else:
                pass
        print(f"Dictionary after adding: {uniques}")
        slid_uniques = {}
        for num, key in enumerate(keys):
            if num == 0:
                slid_uniques[key] = 0
            else:
                slid_uniques[key] = uniques[keys[num-1]]
        print(f"Dictionary after sliding: {slid_uniques}")
        sorted_list = [x for x in range(len(arr))]
        for x in arr:
            i = slid_uniques[x]
            sorted_list[i] = x
            slid_uniques[x] += 1
        print(arr)
        print(sorted_list)
        return sorted_list

def count_sort( arr ):
    if len(arr) == 0:
        return arr
    else:
        uniques = {x: 0 for x in range(min(arr), max(arr)+ 1)}
        keys = [x for x in uniques.keys()]
        for x in arr:
            if x >= 0:
                uniques[x] += 1
            else:
                return "Error, negative numbers not allowed in Count Sort"
        for num, key in enumerate(keys):
            if num != len(keys) - 1:
                uniques[keys[num + 1]] += uniques[key]
            else:
                pass
        slid_uniques = {}
        for num, key in enumerate(keys):
            if num == 0:
                slid_uniques[key] = 0
            else:
                slid_uniques[key] = uniques[keys[num-1]]
        sorted_list = [x for x in range(len(arr))]
        for x in arr:
            i = slid_uniques[x]
            sorted_list[i] = x
            slid_uniques[x] += 1
        print(arr)
        print(sorted_list)
        return sorted_list
        