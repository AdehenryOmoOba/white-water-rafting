best_style = True

print("RAYMOND'S DRESSING GAME")
print()
tops = input('Would you prefer a HOODIE or a BUTTONED LONG SLEEVE SHIRT? ')
if tops.lower() == 'hoodie':
    dress = print('A Hoodie is best mostly when the weather is cold.')
elif tops.lower() == 'buttoned long sleeve':
    dress = print( 'A Longe Sleeve Buttoned Shirt is the best pick for an official occasion mostly a dinner date or a meeting.')
else:
    print('Your choice was not found in the availabe clothes. Please choose between a HOODIE or a BUTTONED LONG SLEEVE SHIRT')
print()
down = input('Now let us help you choose the best trouser for your outfit. Would you go for a JEAN or SLACKS? ')
if down.lower() == 'jean':
    dress = print('A Jean is not bad a choice, They Work At For Any Age Or Size! Style has No size ')
elif down.lower() == 'slacks':
    dress = print('Slacks are comfortable and would be the best fit for an official event.')
else:
    print('Your choice was not found in the availabe clothes. Please choose between a Jean or a Slack')
print()
shoes = input('What doo you think about wearing a SNEAKER or a SHOE? ')
if shoes.lower() == 'sneakers':
    dress = print('A Sneaker goes with everything, pick up your best sneaker brand and I doubt there is no doubt that it will match every clothing style. ')
elif shoes.lower() == 'shoe':
    dress = print('Shoes in deed can build your confidence in an occasion and will always be best for any formal occasion. ')
else:
    print('Your choice was not found in the availabe clothes. Please choose between SNEAKER or a SHOE')

if tops.lower() == 'hoodie' and down.lower() == 'jean' and shoes != 'shoe':
    best_style = True

elif tops.lower() == 'buttoned long sleeve shirt' and down.lower == 'slacks':
    best_style = True

else:
    best_style = False
    

print()
print(f'You chose to put on a {tops.capitalize()} with a {down.capitalize()} and finally with a {shoes.capitalize()}')
print()
if best_style:
    print('You are in deed a fashionista, you really got game ')

else:
    print('Not a bad choice, but I suggest you step up a bit')