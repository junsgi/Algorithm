import java.util.Queue;
import java.util.LinkedList;
class Solution {
    private static final int[][] DIRE = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
    
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        
        for(int i = 0 ; i < m ; i++) {
            for(int j = 0 ; j < n ; j++) {
                if (picture[i][j] != 0) {
                    numberOfArea++;
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, bfs(i, j, picture));
                }
            }
        }
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
    
    private int bfs(int x, int y, int[][] graph) {
        int num = graph[x][y];
        Queue<Node> que = new LinkedList<>();
        
        int result = 0;
        que.offer(new Node(x, y));
        graph[x][y] = 0;
        while (!que.isEmpty()) {
            Node temp = que.poll();
            int ax = temp.x;
            int ay = temp.y;
            result++;
            
            for(int[] d : DIRE) {
                int tx = ax + d[0];
                int ty = ay + d[1];
                if (!(0 <= tx && tx < graph.length && 0 <= ty && ty < graph[0].length)) continue;
                if (graph[tx][ty] != num) continue;
                graph[tx][ty] = 0;
                que.offer(new Node(tx, ty));
            }
        }
        return result;
    }
    
}

class Node {
    int x;
    int y;
    Node(int i, int j) {
        this.x = i;
        this.y = j;
    }
}