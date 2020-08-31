#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author  :   JingV
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution(object):
    def canVisitAllRooms(self, rooms):
        # bfs => (已进入的房间, 未进入的房间)
        room_count, visited_rooms, queue = len(rooms), [0], [rooms[0]]
        while queue:
            if len(visited_rooms) == room_count:
                return True
            avaliable_rooms = queue.pop(0)
            for room in avaliable_rooms:
                if room not in visited_rooms:
                    visited_rooms.append(room)
                    queue.append(rooms[room])
        return False


def main():
    solution = Solution()
    tests = [
        [[1], [2], [3], []],
        [[1, 3], [3, 0, 1], [2], [0]],
        [[2, 3], [], [2], [1, 3, 1]]
    ]
    for rooms in tests:
        print(solution.canVisitAllRooms(rooms))


if __name__ == "__main__":
    main()
