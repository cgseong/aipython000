from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])  # 시작 노드를 큐에 삽입
    visited[start] = True   # 방문 처리

    while queue:
        node = queue.popleft()  # 큐에서 노드 꺼내기
        print(node, end=" ")

        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)  # 방문하지 않은 이웃 노드를 큐에 삽입
                visited[neighbor] = True   # 방문 처리

# 그래프 예시 (인접 리스트)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 방문 기록 초기화
visited = {node: False for node in graph}

# BFS 실행
bfs(graph, 'A', visited)  # 출력: A B C D E F