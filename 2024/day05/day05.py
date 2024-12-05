import math

update_to_children = {}
correct_update_middle_nums = []
corrected_update_middle_nums = []
with open('input.txt') as input_fd:
    for line in input_fd:
        if '|' in line:
            # Save the children of each number
            updates = line.strip().split('|')
            update_to_children.setdefault(updates[0], []).append(updates[1])
        elif ',' in line:
            updates = line.strip().split(',')
            prev_updates = []
            updates_to_be_corrected = [x for x in updates]
            correct = True
            for update in updates:
                if update in update_to_children:
                    # Check if the previous updates are children of the current update
                    children_updates = update_to_children[update]
                    if all([prev_update not in children_updates for prev_update in prev_updates]):
                        pass
                    else:
                        correct = False
                        # Get incorrect previous updates in the same order as the updates
                        incorrect_prev_updates = [x for x in updates_to_be_corrected if x in prev_updates and x in children_updates]
                        print(f"Incorrect updates: {updates_to_be_corrected}! Problem at {update} with previous updates {incorrect_prev_updates}. Starting correction...")
                        # Paste updates in the new order
                        updates_before_correction = [x for x in updates_to_be_corrected[:updates_to_be_corrected.index(update)] if x not in incorrect_prev_updates]
                        updates_after_correction = updates_to_be_corrected[(updates_to_be_corrected.index(update) + 1):]
                        updates_to_be_corrected = updates_before_correction + [update] + incorrect_prev_updates + updates_after_correction
                prev_updates.append(update)
            # Get middle number of the updates
            if correct:
                middle_num = int(updates[math.ceil(len(updates)/2) - 1])
                correct_update_middle_nums.append(middle_num)
                print(f"Correct updates: {updates}. Middle num: {middle_num}")
            else:
                middle_num = int(updates_to_be_corrected[math.ceil(len(updates_to_be_corrected)/2) - 1])
                corrected_update_middle_nums.append(middle_num)
                print(f"Corrected updates: {updates_to_be_corrected}. Middle num: {middle_num}")

print(sum(correct_update_middle_nums))
print(sum(corrected_update_middle_nums))
