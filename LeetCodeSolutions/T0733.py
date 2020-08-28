#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   T0733.py
@Time    :   2020/08/17 08:41:16
@Author  :   LaLaLa
@Version :   1.0
@Contact :   None
@License :   None
@Desc    :   None
'''


class Solution():
    def floodFill(self, image, sr, sc, newColor):
        if not image or not image[0]:
            return
        source_color = image[sr][sc]
        # 如果要修改的颜色与原颜色相同, 则直接返回image
        if source_color == newColor:
            return image
        row, colum = len(image), len(image[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = [(sr, sc)]
        while queue:
            temp = queue.pop(0)
            # 居然忘记改source position的color
            image[temp[0]][temp[1]] = newColor
            for direction in directions:
                target_r, target_c = temp[0] + direction[0], temp[1] + direction[1]
                if 0 <= target_r < row and 0 <= target_c < colum and image[target_r][target_c] == source_color:
                    queue.append((target_r, target_c))
        return image


def main():
    solution = Solution()
    test = [
        # (
        #     [
        #         [1, 1, 1],
        #         [1, 1, 0],
        #         [1, 0, 1],
        #     ],
        #     1, 1, 2
        # ),
        # (
        #     [
        #         [1],
        #         [1],
        #         [1],
        #     ],
        #     1, 0, 2
        # ),
        # (
        #     [
        #         [1, 1, 1]
        #     ],
        #     0, 1, 2
        # ),
        # (
        #     [],
        #     1, 1, 2
        # ),
        # (
        #     [[]],
        #     1, 1, 2
        # ),
        (
            [[0, 0, 0], [0, 1, 1]],
            1, 1, 1
        ),
    ]
    for image, sr, sc, newColor in test:
        print(solution.floodFill(image, sr, sc, newColor))


if __name__ == "__main__":
    main()
