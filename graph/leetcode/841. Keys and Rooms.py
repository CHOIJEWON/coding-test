from collections import deque


class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = [False] * len(rooms)
        queue = deque()

        queue.append(0)  # 0번 방에서 시작

        while queue:
            current_index = queue.popleft()
            if not visited[current_index]:  # 방문하지 않았다면
                visited[current_index] = True
                for key in rooms[current_index]:
                    if not visited[key]:  # 아직 방문하지 않은 방의 키라면
                        queue.append(key)

        return 'true' if all(visited) else 'false'


rooms_arr = [[1, 3], [3, 0, 1], [2], [0]]

test = Solution()
print(test.canVisitAllRooms(rooms_arr))