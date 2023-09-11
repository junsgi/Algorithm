# https://www.acmicpc.net/problem/14503
import sys
sys.setrecursionlimit(200)
input = sys.stdin.readline

n, m = map(int, input().split())
rx, ry, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]