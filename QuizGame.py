print('------------------------------')
print('       Quiz game in Python    ')
print('------------------------------')

start = input('\nDo you want to play the game? ')

# if condition to check whether user wants to play or not

if start.lower() != "yes":  
    quit()
else:
    print('Let\'s get started!')

# initializing score to zero so we can increment score after every correct answer
score = 0 

# if-else loop for checking if the user gives correct answer or not 
# using .lower() function because when the user inputs the answer it will be processed in lower case format

answer = input('CPU stands for? ')

if answer.lower() == 'central processing unit':
    print('Correct')
    score += 1
else:
    print('Incorrect')   


answer = input('GPU stands for? ')

if answer.lower() == 'graphical processing unit':
    print('Correct')
    score += 1
else:
    print('Incorrect')


answer = input('RAM stands for? ')

if answer.lower() == 'random access memory':
    print('Correct')
    score += 1
else:
    print('Incorrect')

answer = input('ROM stands for? ')

if answer.lower() == 'read only memory':
    print('Correct')
    score += 1
else:
    print('Incorrect')


answer = input('IP stands for? ')

if answer.lower() == 'internet protocol':
    print('Correct')
    score += 1
else:
    print('Incorrect')


answer = input('HTML stands for? ')

if answer.lower() == 'hypertext markup language':
    print('Correct')
    score += 1
else:
    print('Incorrect')


answer = input('CSS stands for? ')

if answer.lower() == 'cascading style sheets' or 'cascading style sheet':
    print('Correct')
    score += 1
else:
    print('Incorrect')                

# calculating score by incrementing score by 1 after every correct answer

print('You got ' + str(score) + ' questions correct.')

# calculating percentage 

percentage = ((score/ 7) * 100)

# using %.2f which will print only 2 numbers after decimal

percentage = '%.2f' % percentage

print('You got ' +  str(percentage) + '%')

print('\nCongratulation!! You played well.\n')