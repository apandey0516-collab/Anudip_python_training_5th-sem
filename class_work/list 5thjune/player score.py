#program to display player score
player_score =[]
# input of score from user
for i in range(4):
    score = int(input("enter the score{}".format(i+1)))
    player_score.append(score)
    print("player_score")
    print("score of 11th player",player_score)
    max_score=player_score[0]
    for i in range(1,len(player_score)):
        if(player_score[i]>max_score):
            max_score=player_score[i]


