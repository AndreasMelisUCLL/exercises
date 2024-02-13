# Write your code here
def card_value(string):
    # facecards = ['Jack', 'Queen', 'King']  
    # for i, facecard in enumerate(facecards):
    #     if string == facecard:
    #         return 11 + i 
    if string == 'Jack': return 11
    if string == 'Queen': return 12
    if string == 'King': return 13
    if string == 'Ace': return 1
    return int(string)