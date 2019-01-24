def minion_game(string):
    stuart = 0
    kevin = 0

    # for i in range(len(string)):
    #     step = 1
    #     l = 0
    #     m = step
    #     for j in range(1, len(string) - i + 1):
    #         if string[l:m].startswith(('A', 'E', 'I', 'O', 'U')):
    #             kevin += 1
    #         else:
    #             stuart += 1
    #         l = m
    #         m += step
    #
    # if stuart > kevin:
    #     print(f'Stuart {stuart}')
    # elif kevin > stuart:
    #     print(f'Kevin {kevin}')
    # else:
    #     print('Draw')
    # print(f'{stuart} {kevin}')

    vowels = 'AEIOU'

    kev_score = 0
    stu_score = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kev_score += (len(s) - i)
        else:
            stu_score += (len(s) - i)

    if kev_score > stu_score:
        print("Kevin", kev_score)
    elif kev_score < stu_score:
        print("Stuart", stu_score)
    else:
        print("Draw")
    print(f'{stu_score} {kev_score}')


if __name__ == '__main__':
    s = input()
    minion_game(s)


# Take away
# Better understanding of logic is needed

# Kevin and Stuart want to play the 'The Minion Game'.
#
# Game Rules
#
# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string .
#
# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
#
# For better understanding, see the image below:
#
# banana.png
#
# Your task is to determine the winner of the game and their score.
#
# Input Format
#
# A single line of input containing the string .
# Note: The string  will contain only uppercase letters: .
#
# Constraints
#
#
#
# Output Format
#
# Print one line: the name of the winner and their score separated by a space.
#
# If the game is a draw, print Draw.
#
# Sample Input
#
# BANANA
# Sample Output
#
# Stuart 12