class Solution {
    public int[] solution(int[] answers) {
        int[] a = new int[]{1, 2, 3, 4, 5}, b = new int[]{2, 1, 2, 3, 2, 4, 2, 5}, c = new int[]{3,3,1,1,2,2,4,4,5,5};
        int x = 0, y = 0, z = 0;
        for(int i = 0 ; i < answers.length; i++)
        {
            if (a[i % 5] == answers[i]) x++;
            if (b[i % 8] == answers[i]) y++;
            if (c[i % 10] == answers[i]) z++;
        }
        int max = Math.max(x, Math.max(y, z));
        int[] arr = new int[]{x, y, z};
        int len = 0;
        for(int i : arr)
            if (i == max) len++;
        int[] answer = new int[len];
        len = 0;
        for(int i = 0 ; i < 3; i++)
            if (arr[i] == max) answer[len++] = i + 1;
        return answer;
    }
}