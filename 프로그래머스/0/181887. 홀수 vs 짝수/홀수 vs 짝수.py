def solution(num_list):
    return max(sum([num_list[i] for i in range(len(num_list)) if i % 2]), sum([num_list[i] for i in range(len(num_list)) if i % 2 == 0]))