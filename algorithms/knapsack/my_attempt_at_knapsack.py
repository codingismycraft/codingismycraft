def initial_loop(available_weight, weights, values, item_number, old_weight_list, old_value_list):
    """Doesnt work, isnt used"""
    current_weight = 0
    current_value = 0
    item_in_bag = False
    current_weight_list = [0, 0, 0, 0, 0]
    current_value_list = [0, 0, 0, 0, 0]
    for index in range(0, available_weight):
        if index - current_weight >= weights[item_number] and values[item_number] >= old_value_list[
            index] and item_in_bag == False:  # Adds the item
            current_weight += weights[item_number]
            current_value += values[item_number]
            item_in_bag = True
        if old_value_list[index - current_weight] > current_value:  # Transfers the value of the previous list
            current_value += old_value_list[index - current_weight]
            current_weight += old_weight_list[index - current_weight]
        current_weight_list[index] = current_weight
        current_value_list[index] = current_value
    if item_number + 1 < len(weights):
        initial_loop(available_weight, weights, values, item_number + 1, current_weight_list, current_value_list)
    print(current_weight_list)


def first_loop(available_weight, weights, values):
    """Doesnt work, isnt used"""
    current_weight = 0
    current_value = 0
    item_in_bag = False
    current_weight_list = [0, 0, 0, 0, 0]
    current_value_list = [0, 0, 0, 0, 0]
    for i in range(0, available_weight):
        if weights[0] <= i and item_in_bag == False:
            current_weight_list[i] = weights[0]
            current_value_list[i] = values[0]
            item_in_bag = True
            current_weight = weights[0]
            current_value = values[0]
        current_weight_list[i] = current_weight
        current_value_list[i] = current_value
    initial_loop(available_weight, weights, values, 1, current_weight_list, current_value_list)
    # print(current_value_list)


def other_loops(available_weight, weights, values, item_number, old_weight_list, old_value_list, old_item_list):
    """doesnt work, isnt used"""
    current_weight_list = [0, 0, 0, 0, 0, 0, 0]
    current_value_list = [0, 0, 0, 0, 0, 0, 0]
    current_item_list = [[], [], [], [], []]
    for i in range(0, available_weight):
        if weights[item_number] <= i and values[item_number] >= old_value_list[i]:  # The item can be added and the old
            leftover = i - weights[item_number]
            current_weight_list[i] = weights[item_number] + old_weight_list[leftover]
            current_value_list[i] = values[item_number] + old_value_list[leftover]
            current_item_list[i].append(item_number)
        else:
            current_weight_list[i] = old_weight_list[i]
            current_value_list[i] = old_value_list[i]
            current_item_list[i].append(old_item_list[i])

    print(current_weight_list)
    print(current_value_list)
    print(old_item_list)
    print("\n")
    other_loops(available_weight, weights, values, item_number + 1, current_weight_list, current_value_list,
                current_item_list)


def dict_loop(available_weight, weights, values, item_number, previous_line):
    """Kinda works"""
    current_line = {"weight": [], "value": [], "item_no": [[], [], [], [], [], [], []]}
    for i in range(0, available_weight):
        if weights[item_number] <= i and values[item_number] >= previous_line["value"][i]:  # we fit the current item and possibly some leftovers
            leftover = i - weights[item_number]
            if leftover > 0:
                current_line["weight"].append(weights[item_number] + previous_line["weight"][leftover])
                current_line["value"].append(values[item_number] + previous_line["value"][leftover])
                current_line["item_no"][i].append(item_number)
                if previous_line["item_no"][leftover] > []:
                    print("leftover", previous_line["item_no"][leftover])
                    current_line["item_no"][i].append(previous_line["item_no"][leftover])
            else:
                current_line["weight"].append(weights[item_number])
                current_line["value"].append(values[item_number])
                current_line["item_no"][i].append(item_number)

        else:  # its better to fit the combination of the previous line

            current_line["weight"].append(previous_line["weight"][i])
            current_line["value"].append(previous_line["value"][i])

    if item_number == 4:
        print(current_line)
        print(previous_line)
        return
    dict_loop(available_weight, weights, values, item_number + 1, current_line)


previous_line = {"weight": [0, 0, 0, 0, 0, 0, 0], "value": [0, 0, 0, 0, 0, 0, 0],
                 "item_no": [[], [], [], [], [], [], []]}
available_weight = 7
weights = [1, 2, 2, 4, 7]
values = [10, 20, 30, 40, 70]
item_number = 0
dict_loop(available_weight, weights, values, item_number, previous_line)
# other_loops(available_weight,weights,values,item_number,previous_line)
# first_loop(available_weight, weights, values)
