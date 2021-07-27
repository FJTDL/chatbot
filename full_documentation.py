import datetime
import time
import winsound

#list which will have the activity appended to it as time goes on (advanced feature)
activity = []

# define several functions to make my job easier
# check email function
def check_email(email):
    
    # initialise testing value to false as default
    
    valid_at = False
    while not valid_at:
        valid_dot = 0
        for i in range(0, len(email) + 1):
            valid_dot = 0
            email_check = list(email)
    
            # check for @ character
    
            if "@" in email_check:
                valid_dot += 1
                i += 1
    
            # check for . character
    
            if "." in email_check:
                valid_dot += 1
            else:
                i += 1
        if valid_dot >= 2:
            
            # if both conditions are met then this part of the loop runs
            
            valid_at = True
        else:
            
            # if one or more conditions is not met then this runs
            
            print("\nYour email is not valid")
            email = input("Please enter your email: ")
            check_email(email)


# active function relies on list manipulation of the activity list to append the data later to a text file (advanced feature)
# PLEASE NOTE: This is not collecting personal data and all data is stored on my computer, so this does not violate privacy
def active():
    now = datetime.datetime.now()
    timestamp = str(now.strftime("%Y%m%d_%H:%M:%S"))
    file_object = open('activity.txt', 'a')
    
    # turn list into string to append to data file
    
    activity_string = str(activity)
    file_object.write(name + "  " + activity_string + "  " + timestamp + "\n")

# uniform function
def uniform_function():
    print("The school uses gender specific uniforms with some overlap.\n")
    print("A: Girls\nB: Boys\nC: Neutral\n")
    
    # append user activity for later addition to text file
    
    activity.append(" |Uniform| ")
    which_uniform = input("Please select the corresponding letter. \n").lower()
    if which_uniform not in ['a', 'b', 'c']:
        print("I do not recognise that request")
        
        # append activity to list for addition to data later
        
        activity.append(" |Unknown request| ")
        uniform_function()
    if which_uniform == 'a':
        print("The girls wear a white blouse and knee length skirt until year 13.")
        print("They may wear the school trousers.")
        print("They may wear the cardigan, jersey, scarf and jacket as well.")
        print("They must wear either school approved sandals, or approved shoes with school socks.")
        print("In year 13, they wear a blue blouse and full length skirt.\n")
        activity.append(" |Girls uniform| ")
    if which_uniform == 'b':
        print("The boys wear a grey polo shirt and shorts until year 3.")
        print("They may wear the school trousers.")
        print("They may wear the jersey, scarf and jacket as well.")
        print("They must wear either school approved sandals, or approved shoes with school socks.")
        print("Garters must be worn when in shoes and shorts.")
        print("In year 13, they wear a white polo shirt, otherwise the same.\n")
        activity.append(" |Boys uniform| ")
    if which_uniform == 'c':
        print("Neutrals wear the uniform correlating to their sex.")
        print("We advise they wear the school trousers.\n")
        activity.append(" |Gender neutral uniform| ")
    print("All school uniform is available from the school shop except foot wear.\n")
    
    # run exit code
    
    we_done_here()

# informs user of what can be done to help
def information():
    print("I can help you with:\n")
    print("A: Enrollment.\n")
    print("B: About us\n")
    print("C: Curriculum\n")
    print("D: Other\n")
    print("E: Exit")
    request()


# request for bot to disconnect
def we_done_here():
    end_it_all = input("Alright if I shut down for now? y/n\n").lower()
    if end_it_all == "yes" or end_it_all == "y":
        print("Thank you for your time and consideration.")
        
        # Add timer so people read each message separately
        
        time.sleep(1)
        print("Norm has disconnected")
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        
        # list appends final data
        
        activity.append(" |Finished| ")
        
        # list is converted to string and appended to text file
        
        active()
    else:
        
        # if unknown, then this runs to remind user of what the bot can do
        
        information()


# function that opens and stores data in text file (advanced feature)
def question():
    now = datetime.datetime.now()
    
    # import timestamp to append to file
    
    timestamp = str(now.strftime("%Y%m%d_%H:%M:%S"))
    file_object = open('queries.txt', 'a')
    email = input("Please enter your email: ")
    check_email(email)
    y = input("What's your question: ")
    file_object.write(name + "   from:   " + email + ":   asked:   " + "'" + y + "'" + "   " + timestamp + "\n")
    
    # appends user activity to list for later addition to text file
    
    activity.append(" |Input question| ")
    we_done_here()


# allows for user to request desired information from categories
def request():
    print("\n")
    request_1 = input("Please select the letter according to what your question relates to.\n").lower()
    if request_1 == 'a':
        print("If your child has completed year 8 and is under 16 they are applicable for year 9.")
        print("Questions may be left under the 'Other' option.\n")
        
        # run exit code
        
        we_done_here()
        
        # append activity to list for later addition
        
        activity.append(" |enrollment| ")
    elif request_1 == 'b':
        our_values()
        
        # append activity to list for later addition
        
        activity.append(" |Our values| ")
    elif request_1 == 'c':
        print("You have selected: Curriculum.\n")
        
        # append activity to list for later addition
        
        activity.append(" |Curriculum| ")
        print("Our school proudly offers subjects across all 6 vocational pathways.")
        print("All students must take up to level 1 maths and english.")
        print("All students must take up to year 10 social studies, PE and science.\n")
        print("Year 9 students must complete a rotation in their first year.")
        print("This includes: 2 languages, technology, visual art, music and health.")
        print("Year 9 students may also take optional classes that are either extra to their courses or in the place of another.\n")
        
        # run exit code
        
        we_done_here()
    elif request_1 == 'd':
        print("You have selected: Other")
        question()
    elif request_1 == 'e':
        print("Exiting")
        
        # run exit code
        
        we_done_here()
    else:
        print("I'm sorry, but I do not recognise that request, remember:")
        
        # unknown request results in bot reminding user of what it can do
        
        information()
        
        # append activity to list for later addition
        
        activity.append(" |Unknown request| ")


# our values
def our_values():
    print("\nYou have selected our values. Here, we will explain our schools values.")
    
    # assign values to all list values later
    four_pillars = ["A: Sport.", "B: Academics.", "C: Arts.", "D: Service."]
    
    results = "MAGS is one of the top performing schools in the country, averaging 100 scholarships a year."
    decile = "MAGS is a decile 7 school."
    UE = "MAGS has an UE achievement of close to 70%."
    inclusiveness = "Our school supports rainbow societies, religions and will not stand for bullying.\n"
    academic_achievement = [results, decile, UE]
    values = ["A: Four pillars", "B: Uniform", "C: Inclusiveness", "D: Academic achievement"]
    
    # set up for printing desired results
    
    print(values)
    
    selection_of_values = input("Please select the correlating letter, or press E to exit.\n").lower()
    if selection_of_values == 'a':
        print("\nYou have chosen the four pillars, which are:")
        
        # append user activity to list for later addition to text file
        
        activity.append(" |Four pillars| ")
        print(four_pillars)
        pillar = input("Please select the letter of the pillar you would like information on, or E to exit.").lower()
        
        # nested if function for pillar request
        
        if pillar == 'a':
            print("\nYou have chosen sport")
            print("if you can think of a sport, we either already offer it or are happy to start offering it.\n")
            
            # append user activity to list for later addition to text file
            
            activity.append(" |Sport| ")
            
            # run exit code
            
            we_done_here()
        elif pillar == 'b':
            activity.append(" |Academics| ")
            print(results)
            print(decile)
            print(UE)
            print("\n")
            
            # run exit code
            
            we_done_here()
        elif pillar == 'c':
            print("\nYou have chosen arts.")
            
            # append user activity to list for later addition to text file
            
            activity.append(" |Arts| ")
            print("We offer cultural groups, music groups, drama, dance and visual arts.")
            print("Year 9 students are able to join the dance and drama classes to accelerate in these subjects.")
            print("All students take art and music in their first year, at later years it is an option.\n")
            
            # run exit code
            
            we_done_here()
        elif pillar == 'd':
            print("\nYou have chosen service.")
            print("MAGS has close involvement with our community.")
            print("We offer service clubs in environment, fund raising and mental health.\n")
            
            # append user activity to list for later addition to text file
            
            activity.append(" |Service| ")
            
            # run exit code
            
            we_done_here()
        elif pillar == 'e':
            
            # run exit code
            
            we_done_here()
        else:
            print("\nI'm sorry, but i do not recognise that request.")
            
            # append user activity to list for later addition to text file
            
            activity.append(" |Unrecognised request| ")
            
            # display what the bot can do, since an recognised request has been entered
            
            information()
    elif selection_of_values == 'b':
        print("\nYou have chosen uniform.")
        uniform_function()
    elif selection_of_values == 'c':
        print("\nYou have chosen inclusiveness")
        
        # append user activity to list for later addition to text file
        
        activity.append(" |Inclusiveness| ")
        print(inclusiveness)
        
        # run exit code
        
        we_done_here()
    elif selection_of_values == 'd':
        print("\nYou have academic achievement")
        
        # append user activity to list for later addition to text file
        
        activity.append(" |Academic achievement| ")
        print(academic_achievement)
        
        # run exit code
        
        we_done_here()
    elif selection_of_values == 'e':
        
        # bot displays what it can do for the user
        
        information()
    else:
        print("\nI'm sorry, I don't recognise that request")
        
        # append user input to list for later addition to text file
        
        activity.append(" |Unrecognised request| ")
        information()


# actual program outside of the functions defined above
winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
print("Hello, I am Norm.\n")
print("I can the virtual assistant of Mount Albert Grammar School.")
name = input("What is your name?\n")
assist = input("Are you in need of assistance {}? y/n\n".format(name)).lower()
if assist == "yes" or assist == "y":
    information()
else:
    # run exit code
    we_done_here()
