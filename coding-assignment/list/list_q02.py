"""
@leetcode
There are n teams numbered from 0 to n - 1 in a tournament; each team is also a node in a DAG.

You are given the integer n and a 0-indexed 2D integer array edges of length m representing the DAG,
where edges[i] = [ui, vi] indicates that there is a directed edge from team ui to team vi in the graph.

A directed edge from a to b in the graph means that team a is stronger than team b and team b is weaker
than team a.

Team a will be the champion of the tournament if there is no team b that is stronger than team a.

Return the team that will be the champion of the tournament if there is a unique champion, otherwise,
return -1.

Input: n = 3, edges = [[0,1],[1,2]]
Output: 0
Explanation: Team 1 is weaker than team 0. Team 2 is weaker than team 1. So the champion is team 0.

Input: n = 4, edges = [[0,2],[1,3],[1,2]]
Output: -1
Explanation: Team 2 is weaker than team 0 and team 1. Team 3 is weaker than team 1. But team 1 and
team 0 are not weaker than any other teams. So the answer is -1.
"""


class Solution:
    @staticmethod
    def find_champion(n: int, edges: list[list[int]]) -> int:
        """
        :param n: Number of teams
        :param edges: The relations between teams
        :return: The winning team if unique else -1

        Intuition: The winning team is the one with the least amount of weaknesses i.e., the team which occurs
        the least in edges[i][1] for i in edges.
        """
        res = [0] * n #a list in which the index is the team number and the value is the number of weaknesses
        for i in edges:
            res[i[1]] += 1 #adding the amount of weaknesses to res
        strongest = 0 #the strongest team
        m = 0 #a variable to make sure multiple strongest teams dont exist
        for i in range(1, len(res)): #find the team with minimum weaknesses
            if res[strongest] > res[i]:
                strongest = i
                m = 0
            elif res[strongest] == res[i]:
                m += 1
        return -1 if m else strongest #if there is a unique champion return it else -1
