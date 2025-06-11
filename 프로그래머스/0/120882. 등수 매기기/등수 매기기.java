import java.util.*;
class Node {
    double value;
    int index;
    int rank;

    public Node(double a, int b) {
        this.value = a;
        this.index = b;
        this.rank = 0;
    }
}
class Solution {
    public int[] solution(int[][] score) {
        int[] answer = new int[score.length];
        ArrayList<Node> result = new ArrayList<>();
        for(int i = 0 ; i < score.length ; i++)
            result.add(new Node((double)(score[i][0] + score[i][1]) / 2, i)); // 평균과 인덱스 삽입
        Comparator<Node> value = (a, b) -> Double.compare(a.value, b.value);
        result.sort(value.reversed());
        
        int rank = 1;
        result.get(0).rank = rank;
        for(int i = 1 ; i < result.size() ; i++) {
            rank++;
            if (result.get(i - 1).value == result.get(i).value)
                result.get(i).rank = result.get(i - 1).rank;
            else
                result.get(i).rank = rank;
        }
        Comparator<Node> index = (a, b) -> Double.compare(a.index, b.index);
        result.sort(index);
        for(int i = 0 ; i < result.size(); i++)
            answer[i] = result.get(i).rank;
        return answer;
    }
}