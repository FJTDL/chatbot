import datetime
import time
import winsound

activity = []

# check email function
def check_email(email):
    valid_at = False
    while not valid_at:
        valid_dot = 0
        for i in range(0, len(email) + 1):
            valid_dot = 0
            email_check = list(email)
            if "@" in email_check:
                valid_dot += 1
                i += 1
            if "." in email_check:
                valid_dot += 1
            else:
                i += 1
        if valid_dot >= 2:
            valid_at = True
        else:
            print("Your email is not valid")
            email = input("Please enter your email: ")
            check_email(email)


def invasion_of_privacy():
    now = datetime.datetime.now()
    timestamp = str(now.strftime("%Y%m%d_%H:%M:%S"))
    file_object = open('activity.txt', 'a')
    activity_string = str(activity)
    file_object.write(name + "  " + activity_string + "  " + timestamp)


# define several functions to make my job easier
def arts():
    print("We offer cultural groups, music groups, drama, dance and visual arts.")
    print("Year 9 students are able to join the dance and drama classes to accelerate in these subjects.")
    print("All students take art and music in their first year, at later years it is an option.")
    activity.append(" |arts| ")
    we_done_here()

# uniform function
def uniform_function():
    print("The school uses gender specific uniforms with some overlap.")
    print("A: Girls\nB: Boys\nC: Neutral")
    activity.append(" |Uniform| ")
    which_uniform = input("Please select the corresponding letter. ").lower()
    if which_uniform == 'a':
        print("The girls wear a white blouse and knee length skirt until year 13.")
        print("They may wear the school trousers.")
        print("They may wear the cardigan, jersey, scarf and jacket as well.")
        print("They must wear either school approved sandals, or approved shoes with school socks.")
        print("In year 13, they wear a blue blouse and full length skirt.")
        activity.append(" |Girls uniform| ")
    if which_uniform == 'b':
        print("The boys wear a grey polo shirt and shorts until year 3.")
        print("They may wear the school trousers.")
        print("They may wear the jersey, scarf and jacket as well.")
        print("They must wear either school approved sandals, or approved shoes with school socks.")
        print("Garters must be worn when in shoes and shorts.")
        print("In year 13, they wear a white polo shirt, otherwise the same.")
        activity.append(" |Boys uniform| ")
    if which_uniform == 'c':
        print("Neutrals wear the uniform correlating to their sex.")
        print("We advise they wear the school trousers.")
        activity.append(" |Gender neutral uniform| ")
    print("All school uniform is available from the school shop except foot wear.")
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
    end_it_all = input("Alright if I shut down for now?\n").lower()
    if end_it_all == "yes":
        print("Thank you for your time and consideration.")
        # Add timer so people read each message separately
        time.sleep(2)
        print("Norm has disconnected")
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        activity.append(" |Finished| ")
        invasion_of_privacy()
    else:
        information()


# function that opens and stores data in excel spreadsheet
def excel_sheet():
    now = datetime.datetime.now()
    timestamp = str(now.strftime("%Y%m%d_%H:%M:%S"))
    file_object = open('data.txt', 'a')
    email = input("Please enter your email: ")
    check_email(email)
    y = input("What's your question: ")
    file_object.write(name + "   from:   " + email + ":   asked:   " + "'" + y + "'" + "   " + timestamp + "\n")
    activity.append(" |Input question| ")
    we_done_here()


# allows for user to request desired information from categories
def request():
    print("\n")
    request_1 = input("Please select the letter according to what your question relates to.\n").lower()
    if request_1 == 'a':
        enrollment()
        activity.append(" |enrollment| ")
        # continue at later date
    elif request_1 == 'b':
        our_values()
        activity.append(" |Our values| ")
    elif request_1 == 'c':
        print("You have selected: Curriculum.")
        activity.append(" |Curriculum| ")
    elif request_1 == 'd':
        print("You have selected: Other")
        excel_sheet()
    elif request_1 == 'e':
        print("Exiting")
        we_done_here()
    else:
        print("I'm sorry, but I do not recognise that request, remember:")
        information()
        activity.append(" |Unknown request| ")


# option 1: enrollment.
# function takes age and education parameters to determine eligibility.
def enrollment():
    print("You have selected enrollment. Here, we will check you/your child's eligibility.")
    continue_enrollment = input("Do you wish to continue?").lower()
    if continue_enrollment == "yes" or continue_enrollment == "y":
        age = int(input("How old is your child?\n"))
        education = input("Has your child completed year 8?")
        if age >= 12 and education == "yes":
            print("Your child is eligible.")
            print("If your child is over 18, we recommend meeting with us to discuss enrollment.")
            activity.append(" |Eligible child| ")
            we_done_here()
        else:
            print("Your child is inapplicable.")
            activity.append(" |Inapplicable child| ")
            we_done_here()


# option 2: our values
def our_values():
    print("You have selected our values. Here, we will explain our schools values.")
    # assign values to all list values later
    four_pillars = ["A: Sport.", "B: Academics.", "C: Arts.", "D: Service.", "E: Other"]
    results = "MAGS is one of the top performing schools in the country, averaging 100 scholarships a year."
    decile = "MAGS is a decile 7 school."
    UE = "MAGS has an UE achievement of close to 70%."
    inclusiveness = "Our school supports rainbow societies, religions and will not stand for bullying."
    academic_achievement = [results, decile, UE]
    values = ["A: Four pillars", "B: Uniform", "C: Inclusiveness", "D: Academic achievement"]
    # set up for printing desired results
    print(values)
    selection_of_values = input("Please select the correlating letter, or press E to exit.\n").lower()
    if selection_of_values == 'a':
        print("You have chosen the four pillars, which are:")
        activity.append(" |Four pillars| ")
        print(four_pillars)
        pillar = input("Please select the letter of the pillar you would like information on, or F to exit.").lower()
        if pillar == 'a':
            print("You have chosen sport")
            print("if you can think of a sport, we either already offer it or are happy to start offering it.")
            activity.append(" |Sport| ")
        elif pillar == 'b':
            print("You have chosen academics.")
            activity.append(" |Academics| ")
            # i want to print the values across three lines
        elif pillar == 'c':
            print("You have chosen arts.")
            activity.append(" |Arts| ")
            arts()
        elif pillar == 'd':
            print("You have chosen service.")
            print("MAGS has close involvement with our community.")
            print("We offer service clubs in environment, fund raising and mental health.")
            activity.append(" |Service| ")
        elif pillar == 'e':
            print("You have selected other.")
            activity.append(" |Other| ")
            excel_sheet()
        elif pillar == 'f':
            we_done_here()
        else:
            print("I'm sorry, but i do not recognise that request.")
            activity.append(" |Unrecognised request| ")
            information()
    elif selection_of_values == 'b':
        print("You have chosen uniform.")
        uniform_function()
    elif selection_of_values == 'c':
        print("You have chosen inclusiveness")
        activty.append(" |Inclusiveness| ")
        print(inclusiveness)
    elif selection_of_values == 'd':
        print("You have academic achievement")
        activity.append(" |Academic achievement| ")
        print(academic_achievement)
    elif selection_of_values == 'e':
        information()
    else:
        print("I'm sorry, I don't recognise that request")
        activity.append(" |Unrecognised request| ")
        information()


# actual program outside of thae functions defined above
winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
print("Hello, I am Norm.\n")
print("I can the virtual assistant of Mount Albert Grammar School.")
name = input("What is your name?\n")
assist = input("Are you in need of assistance {}?\n".format(name)).lower()
if assist == "yes" or assist == "y":
    information()
else:
    we_done_here()
