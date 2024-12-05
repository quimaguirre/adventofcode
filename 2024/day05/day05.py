import math

update_to_children = {}
correct_update_middle_nums = []
corrected_update_middle_nums = []
with open('small_input.txt') as input_fd:
    for line in input_fd:
        if '|' in line:
            updates = line.strip().split('|')
            update_to_children.setdefault(updates[0], []).append(updates[1])
        elif ',' in line:
            updates = line.strip().split(',')
            prev_updates = []
            updates_corrected = [x for x in updates]
            correct_updates = True
            for update in updates:
                if update in update_to_children:
                    children_updates = update_to_children[update]
                    if all([prev_update not in children_updates for prev_update in prev_updates]):
                        prev_updates.append(update)
                    else:
                        correct_updates = False
                        print(f"Incorrect updates: {updates}! Starting correction...")
                        incorrect_prev_updates = [prev_update in children_updates for prev_update in prev_updates]
                        updates_before_correction = updates.split(incorrect_prev_updates[0])[0]
                        updates_corrected = updates_before_correction + [update] + incorrect_prev_updates
                        continue
                else:
                    prev_updates.append(update)
            if correct_updates:
                middle_num = int(updates[math.ceil(len(updates)/2) - 1])
                correct_update_middle_nums.append(middle_num)
                print(f"Correct updates: {updates}. Middle num: {middle_num}")
            else:
                middle_num = int(updates_corrected[math.ceil(len(updates_corrected)/2) - 1])
                corrected_update_middle_nums.append(middle_num)
                print(f"Corrected updates: {updates_corrected}. Middle num: {middle_num}")

#print(update_to_children)
print(sum(correct_update_middle_nums))
print(sum(corrected_update_middle_nums))
