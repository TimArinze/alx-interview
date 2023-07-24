#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened"""
    keys = set()
    opened_boxes = []
    keys.add(0)
    keys.update(boxes[0])
    # opened_boxes.append(boxes[0])
    indexed_boxes = {
            i: boxes[i] for i in range(len(boxes))
            }
    for i in range(len(boxes)):
        for key in indexed_boxes.keys():
            if key in keys:
                keys.update(indexed_boxes[key])
                # opened_boxes.append(indexed_boxes[key])
    # print(keys)
    # print(indexed_boxes)
    indexed_boxes_keys_set = set(indexed_boxes.keys())
    if keys == indexed_boxes_keys_set:
        return True
    else:
        return False
