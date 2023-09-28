import sys
import functions as func


def profile():
  
  input1 = 0
  break_flag = False
  while input1 != 3:
  
    # raises an error if user input can not be converted to an int
    try:
      input1 = int(input('1. Log in\n'
                        '2. Guest\n'
                        '3. Quit\n\n'))
    except ValueError:
      print('\nVery very cringe. Try again nerd.\n')
      continue

    # if user chooses to log in this will display the list of profile options
    if input1 == 1:
      profile = 0
      while profile < 1 or profile > 3:
        try:
          profile = int(input('\n1. Profile 1\n'
                   '2. Profile 2\n'
                   '3. Profile 3\n\n'))
        except ValueError:
          print('\nYikes, imagine not choosing a valid profile <3\n')
    
        # these if statements verify that the password the user enters matches the 
        # password that is assigned to each profile in profiles_info.py. If not, alerts
        # the user and has them try again, until they get it right
        if profile == 1:
          while True:
            password = input('\nPassword: ')

            break_flag = func.validate_password('profile1', password)

            if break_flag:
              return
            
              
        elif profile == 2:
          while True:
            password = input('\nPassword: ')
            
            break_flag = func.validate_password('profile2', password)

            if break_flag:
              return
            
              
        elif profile == 3:
          while True:
            password = input('\nPassword: ')
            
            break_flag = func.validate_password('profile3', password)

            if break_flag:
              return

    elif input1 == 2:
      pass

    elif input1 == 3:
      sys.exit('Quit')

'''  
Step 1: Creating profile1 profile2 profile3. 
I am unsure what this will look like. 
How can you create profiles with unique properties. 
Are objects a thing in python? It does
Would each profile be a function? 
I think these will be objects.
Hard code each profile to have their own passcodes and perms
Step 2:  

'''
'''
Problems so far
1. Not a problem, per se, but will need to update main menu options to allow them to 
choose which list they want to edit/see based on their permissions
'''