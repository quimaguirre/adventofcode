import math

update_to_children = {}
correct_update_middle_nums = []
with open('small_input.txt') as input_fd:
    for line in input_fd:
        if '|' in line:
            updates = line.strip().split('|')
            update_to_children.setdefault(updates[0], []).append(updates[1])
            current_lvl = 1
            for update in updates:
                if update in update_to_lvl:
                    old_lvl = update_to_lvl[update]
                    if old_lvl > current_lvl:
                        current_lvl = old_lvl
                    else:
                        update_to_lvl[update] = current_lvl
                        if update in update_to_children:
                            for child in update_to_children[update]:
                                if child not in update_to_lvl:
                                    update_to_lvl[child] = current_lvl + 1
                                else:
                                    child_old_lvl = update_to_lvl[child]
                                    if child_old_lvl < current_lvl + 1:
                                        update_to_lvl[child] = current_lvl + 1
                else:
                    update_to_lvl[update] = current_lvl
                current_lvl += 1
            #print(updates[0], update_to_lvl[updates[0]], updates[1], update_to_lvl[updates[1]])
        elif ',' in line:
            updates = line.strip().split(',')
            prev_updates = []
            correct_updates = True
            for update in updates:
                if update in update_to_children:
                    children_updates = update_to_children[update]
                    if all([prev_update not in children_updates for prev_update in prev_updates]):
                        prev_updates.append(update)
                    else:
                        correct_updates = False
                        print(f"Incorrect updates: {updates}")
                        break
            if correct_updates:
                middle_num = int(updates[math.ceil(len(updates)/2) - 1])
                correct_update_middle_nums.append(middle_num)
                print(f"Correct updates: {updates}. Middle num: {middle_num}")
            #update_lvls = [update_to_lvl[update] for update in updates]
            #diff_lvls = [x - update_lvls[i - 1] for i, x in enumerate(update_lvls)][1:]
            #if (sum(n < 0 for n in diff_lvls) == 0):
            #    middle_num = int(updates[round(len(updates)/2)])
            #    correct_update_middle_nums.append(middle_num)

#print(update_to_lvl)
#print(update_to_children)
print(sum(correct_update_middle_nums))
