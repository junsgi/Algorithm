#https://school.programmers.co.kr/learn/courses/19344/lessons/242258
def solution(bandage, health, attacks):
    answer = 0
    MAX = health
    cTime, heal, plus = bandage
    time = 0
    for attackTime, damage in attacks:
        
        # 회복 (공격 시간 - 공격이 멈췄던 시간) + (공격까지 걸린 시간 // 시전시간 * 추가 회복량)
        TIME = attackTime - time - 1
        health += (TIME * heal) + (TIME // cTime * plus)
        if health >= MAX: health = MAX
        
        # 공격
        health -= damage
        if health <= 0 :
            return -1
        
        time = attackTime
    return health