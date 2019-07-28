# Group a list of items into bins based on defined percentages
def create_weighted_bin (percentages, total):
    if sum(percentages) != 100:
        raise AssertionError("Percentages must add up to 100!")
    allocations = []
    curr_low = 0
    running_total = 0
    for percentage in percentages:
        allocation_size = int(total*percentage/100.0)
        running_total += allocation_size
        allocations.append({
            "low" : curr_low,
            "high": running_total - 1
        })
        curr_low = running_total
    return allocations

# Assign message to an item in the list based on the weights
def assign_message(percentages, total_items, messages):
    
    weighted_bins = create_weighted_bin(percentages, total_items)
    print(weighted_bins)
    
    assigned_messages = []

    message_index = 0
    count = 0
    current_bin = weighted_bins.pop(0)
    bin_range = range(current_bin['low'], current_bin['high']+1)
    while count < total_items:
        if count in bin_range:
            assigned_messages.append(messages[message_index])
            count += 1
        else:
            message_index += 1
            if len(weighted_bins) > 0 :
                current_bin = weighted_bins.pop(0)
                bin_range = range(current_bin['low'], current_bin['high']+1)

    return assigned_messages

if __name__ == "__main__":
    messages = ['message 20%', 'message 30%', 'message 40%', 'message 10%']
    assigned_messages = assign_message([20, 30, 40, 10], 100, messages)
    print('Allocations: %d' % len(assigned_messages))
    idx = 0
    for m in assigned_messages:
        print ('%d - %s' % (idx, m))
        idx += 1
