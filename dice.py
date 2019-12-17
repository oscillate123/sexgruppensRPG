import random

def n_dice(number_of_dice):
    dice_sum = 0

    for i in range(0, number_of_dice):
        dice_sum += random.randint(1,6)

    return dice_sum
