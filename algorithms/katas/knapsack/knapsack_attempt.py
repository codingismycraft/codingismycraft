class Item:
    def __init__(self, w, v):
        self.w = w
        self.v = v

    def __repr__(self):
        return f'Item({self.w, self.v})'


def solve_bags(weights, values, max_capacity):
    weights.append(0)
    values.append(0)
    items=[]
    for i in range(0,len(weights)):
        items.append(Item(weights[i],values[i]))
    items.sort(key=lambda x: x.w)
    bags=[]
    for i in range(0,len(items)):
        bags.append([0]*(max_capacity+1))
    for row_index in range(1,len(items)):
        current_item = items[row_index]
        for col_index in range(1,max_capacity+1):
            previous_value=bags[row_index - 1][col_index]
            if current_item.w>col_index:
                bags[row_index][col_index]=previous_value
            else:
                if bags[row_index-1][col_index-current_item.w]+current_item.v>previous_value:
                    bags[row_index][col_index]=current_item.v+bags[row_index-1][col_index-current_item.w]
                else:
                    bags[row_index][col_index] = previous_value

    return bags[-1][-1],_selected_items(bags,items)

def _selected_items(bags,items):
    sum_value=0
    row_index=len(items)-1
    col_index=len(bags[0])-1
    selected_items=[]
    while sum_value<bags[-1][-1]:
        if bags[row_index][col_index]>bags[row_index-1][col_index]:
            selected_items.append(items[row_index])
            col_index-=items[row_index].w
            sum_value += items[row_index].v
            row_index-=1
        else:
            row_index-=1
    return selected_items


