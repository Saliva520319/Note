#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Given a binary tree, return the bottom-up level order traversal of
# its nodes' values.

from __future__ import print_function

import collections


class TreeNode(object):

    __slots__ = ['val', 'left', 'right']

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_order_bottom(root):
    if not root:
        return []
    q = collections.deque()
    result = collections.deque()
    q.append(root)
    q.append(None)

    while len(q):
        node = q.popleft()
        result.appendleft([])
        while node:
            result[0].append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if len(q):
                node = q.popleft()
            else:
                break
        if len(q):
            q.append(None)

    return list(result)


if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    print(level_order_bottom(node1))
