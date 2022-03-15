# Dragon's Den
# Quinton Coley, Zach Naden, Edward Smith

import os.path

print('')
print('-----------------------------------------------------------------------')
print("---------------------- Welcome To Dragon's Den ------------------------")
print('-----------------------------------------------------------------------')
print('')


# FRAMEWORK FUNCTION TO CALL OTHER APPLICATIONS
def main():
    print('')
    stud = input("--- Are you new to the Dragon's Den? (Yes or No) ")

    if stud == 'No' or stud == 'no':
        print('')
        print('---', 'Great, opening main menu')
        do_what()

    if stud == 'Yes' or stud == 'yes':
        second_door()


def second_door():
    setup = input("\n--- Would you like to join the Dragon's Den? (Yes or No) ")

    if setup == 'Yes' or setup == 'yes':
        print('')
        print('---', "Great, lets get you signed up!")
        register()

    if setup == 'No' or setup == 'no':
        print('')
        print('---', "Bye now!")


def do_what():
    print('')
    print('---', "What do you want to do? ")
    print('')
    print('---', "Your choices are DragonsDenConnect or BlazerPath: ")
    var = input("")

    if var == "DragonsDenConnect" or var == "dragonsdenconnect":
        dragons_den_connect()

    if var == "BlazerPath" or var == "blazerpath":
        blazerpath()

    else:
        print('')
        print('---', 'Please make an appropriate selection!')
        do_what()


def register():
    f = open('userPass.txt', 'a')
    print('')

    nam = input('--- Enter your desired username: ')
    print('')

    pas = input('--- Enter your desired password: ')
    f.write("\n")
    f.write(nam + "," + pas)

    print("\n *** You have been added to the server!", nam, '***')
    do_what()
    f.close()


###############################################################################

# DICTIONARIES FOR DRAGONSDEN CONNECT
# LISTINGS (CAN ALWAYS ADD MORE)
Hobbies = ['Gaming', 'Concerts', 'Outdoors', 'Fitness', 'Paintball']
Schools = ['UAB', 'Auburn', 'Jeff State', 'University of Alabama', 'Online']
Fields = ['Medical', 'CS', 'Engineering', 'Sociology', 'Biology']
Years = ['Freshman', 'Sophomore', 'Junior', 'Senior', 'Graduate']

# OTHER STUDENTS #IRL WOULD PULL FROM DATABASE OF STUDENTS SIGNED IN TO D.D.
Zach = {
    'School': 'UAB', 'Field': 'CS', 'Year': 'Sophomore', 'Hobby': 'Fitness'}
Edward = {
    'School': 'UAB', 'Field': 'CS', 'Year': 'Sophomore', 'Hobby': 'Paintball'}
Ragan = {
    'School': 'UAB', 'Field': 'Sociology', 'Year': 'Senior', 'Hobby': 'Outdoors'}
Samuel = {
    'School': 'Jeff State', 'Field': 'Engineering', 'Year': 'Sophomore', 'Hobby': 'Outdoors'}
Alosia = {
    'School': 'Online', 'Field': 'Biology', 'Year': 'Graduate', 'Hobby': 'Gaming'}
Evelyn = {
    'School': 'Auburn', 'Field': 'Sociology', 'Year': 'Freshman', 'Hobby': 'Outdoors'}
James = {
    'School': 'Auburn', 'Field': 'CS', 'Year': 'Junior', 'Hobby': 'Fitness'}
Liam = {
    'School': 'University of Alabama', 'Field': 'Engineering', 'Year': 'Senior', 'Hobby': 'Concerts'}
Emma = {
    'School': 'University of Alabama', 'Field': 'Medical', 'Year': 'Junior', 'Hobby': 'Gaming'}
Noah = {
    'School': 'Jeff State', 'Field': 'Medical', 'Year': 'Freshman', 'Hobby': 'Concerts'}

StudentList = [
    Zach, Edward, Ragan, Samuel, Alosia, Evelyn, James, Liam, Emma, Noah]

MyStudentsList = []


###############################################################################

# FUNCTIONS TO TAKE INPUT FROM USER AND STORE FOR USE IN MAIN FUNCTION
def schools_function():
    print('')
    print('---', Schools)
    stest = input('--- Choose from list: Which school do you attend? ')

    if stest not in Schools:
        schools_function()

    else:
        school = stest
        MyStudentsList.append(school)


def fields_function():
    print('')
    print('---', Fields)
    ftest = input('--- Choose from list: What are you studying? ')

    if ftest not in Fields:
        fields_function()

    else:
        field = ftest
        MyStudentsList.append(field)


def years_function():
    print('')
    print('---', Years)
    ytest = input('--- Choose from list: What year student are you? ')

    if ytest not in Years:
        years_function()

    else:
        year = ytest
        MyStudentsList.append(year)


def hobbies_function():
    print('')
    print('---', Hobbies)
    htest = input('--- Choose from list: What do you enjoy doing? ')

    if htest not in Hobbies:
        hobbies_function()

    else:
        hobby = htest
        MyStudentsList.append(hobby)


# Dragon's Den Connect App ---------------------------------------------------------------------------------------------

# MAIN FUNCTION FOR CONNECTING
def dragons_den_connect():
    print('')
    print('-----------------------------------------------------------------------')
    print('----------------- Dragons Den Connection Application ------------------')
    print('-----------------------------------------------------------------------')
    print('')

    # MATCHES (STORES COUNTER FOR COMMON INTERESTS)
    sc1 = 0
    sc2 = 0
    sc3 = 0
    sc4 = 0
    sc5 = 0
    sc6 = 0
    sc7 = 0
    sc8 = 0
    sc9 = 0
    sc10 = 0

    ###############################################################################

    # TAKE INPUTS FROM USER AND ADD TO DICTIONARY
    schools_function()
    fields_function()
    years_function()
    hobbies_function()

    school = MyStudentsList[0]
    field = MyStudentsList[1]
    year = MyStudentsList[2]
    hobby = MyStudentsList[3]

    student_dictionary = {
        'School': school, 'Field': field, 'Year': year, 'Hobby': hobby}

    ###############################################################################

    if StudentList[0]['School'] == student_dictionary['School']:
        sc1 += 1
    if StudentList[1]['School'] == student_dictionary['School']:
        sc2 += 1
    if StudentList[2]['School'] == student_dictionary['School']:
        sc3 += 1
    if StudentList[3]['School'] == student_dictionary['School']:
        sc4 += 1
    if StudentList[4]['School'] == student_dictionary['School']:
        sc5 += 1
    if StudentList[5]['School'] == student_dictionary['School']:
        sc6 += 1
    if StudentList[6]['School'] == student_dictionary['School']:
        sc7 += 1
    if StudentList[7]['School'] == student_dictionary['School']:
        sc8 += 1
    if StudentList[8]['School'] == student_dictionary['School']:
        sc9 += 1
    if StudentList[9]['School'] == student_dictionary['School']:
        sc10 += 1

    ###############################################################################

    if StudentList[0]['Field'] == student_dictionary['Field']:
        sc1 += 1
    if StudentList[1]['Field'] == student_dictionary['Field']:
        sc2 += 1
    if StudentList[2]['Field'] == student_dictionary['Field']:
        sc3 += 1
    if StudentList[3]['Field'] == student_dictionary['Field']:
        sc4 += 1
    if StudentList[4]['Field'] == student_dictionary['Field']:
        sc5 += 1
    if StudentList[5]['Field'] == student_dictionary['Field']:
        sc6 += 1
    if StudentList[6]['Field'] == student_dictionary['Field']:
        sc7 += 1
    if StudentList[7]['Field'] == student_dictionary['Field']:
        sc8 += 1
    if StudentList[8]['Field'] == student_dictionary['Field']:
        sc9 += 1
    if StudentList[9]['Field'] == student_dictionary['Field']:
        sc10 += 1

    ###############################################################################

    if StudentList[0]['Year'] == student_dictionary['Year']:
        sc1 += 1
    if StudentList[1]['Year'] == student_dictionary['Year']:
        sc2 += 1
    if StudentList[2]['Year'] == student_dictionary['Year']:
        sc3 += 1
    if StudentList[3]['Year'] == student_dictionary['Year']:
        sc4 += 1
    if StudentList[4]['Year'] == student_dictionary['Year']:
        sc5 += 1
    if StudentList[5]['Year'] == student_dictionary['Year']:
        sc6 += 1
    if StudentList[6]['Year'] == student_dictionary['Year']:
        sc7 += 1
    if StudentList[7]['Year'] == student_dictionary['Year']:
        sc8 += 1
    if StudentList[8]['Year'] == student_dictionary['Year']:
        sc9 += 1
    if StudentList[9]['Year'] == student_dictionary['Year']:
        sc10 += 1

    ###############################################################################

    if StudentList[0]['Hobby'] == student_dictionary['Hobby']:
        sc1 += 1
    if StudentList[1]['Hobby'] == student_dictionary['Hobby']:
        sc2 += 1
    if StudentList[2]['Hobby'] == student_dictionary['Hobby']:
        sc3 += 1
    if StudentList[3]['Hobby'] == student_dictionary['Hobby']:
        sc4 += 1
    if StudentList[4]['Hobby'] == student_dictionary['Hobby']:
        sc5 += 1
    if StudentList[5]['Hobby'] == student_dictionary['Hobby']:
        sc6 += 1
    if StudentList[6]['Hobby'] == student_dictionary['Hobby']:
        sc7 += 1
    if StudentList[7]['Hobby'] == student_dictionary['Hobby']:
        sc8 += 1
    if StudentList[8]['Hobby'] == student_dictionary['Hobby']:
        sc9 += 1
    if StudentList[9]['Hobby'] == student_dictionary['Hobby']:
        sc10 += 1

    ###############################################################################

    counter_dictionary = {
        'Zach': sc1, 'Edward': sc2, 'Ragan': sc3,
        'Samuel': sc4, 'Alosia': sc5, 'Evelyn': sc6, 'James': sc7,
        'Liam': sc8, 'Emma': sc9, 'Noah': sc10}

    print(f"\n{counter_dictionary}")

    max_interest = max(counter_dictionary, key=counter_dictionary.get)

    print('')
    print('--- Your Dragon Connect is: ', max_interest)
    print('')
    print('*** Returning to Main Menu ***')
    do_what()


# BlazerPath App -------------------------------------------------------------------------------------------------------


###############################################################################

def blazerpath():
    print('')
    print('-----------------------------------------------------------------------')
    print('----------------------- BlazerPath Application ------------------------')
    print('-----------------------------------------------------------------------')
    print('')

    blazer_path = []
    counter = 0

    ###############################################################################

    # Check for required student files
    for items in range(1):

        for FinancialAid in range(1):

            if os.path.exists("fafsa.txt"):
                blazer_path.append(1)

            else:
                blazer_path.append(2)
                print('')
                print("---", "Please submit FAFSA to receive award letter.")

        for Transcript in range(1):

            if os.path.exists("transcript.txt"):
                blazer_path.append(1)

            else:
                blazer_path.append(2)
                print('')
                print("---", "Please submit transcript to continue.")

        for Immunizations in range(1):

            if os.path.exists("immune.txt"):
                blazer_path.append(1)

            else:
                blazer_path.append(2)
                print('')
                print("---", "Please submit immunizations to continue.")

        for Orientation in range(1):
            attended = input(
                "\n--- Did student attend orientation? (Yes or No) ")

            if attended == "Yes" or attended == "yes":
                blazer_path.append(1)

            else:
                blazer_path.append(2)
                print('')
                print("---",
                      "Must attend orientation before registering for classes.")

            for Registration in range(1):

                if os.path.exists("registration.txt"):
                    blazer_path.append(1)

                else:
                    blazer_path.append(2)
                    print('')
                    print("---", "Increase your knowledge and choose a class.")

                ###############################################################################

        # Add up until the number = the required items
        for i in blazer_path:

            if i == 1:
                counter += 1

    ###############################################################################

    # checking what you have to see if you've met the requirements
    if counter == len(blazer_path):
        print('')
        print('---', "You have completed all necessary requirements!")
        print('')
        print("---", "Welcome to the Dragons Den! <ARRRRGGGHHHHH!!!!")
        print('')
        print('*** Returning to Main Menu ***')
        do_what()

    elif counter == 0:
        print('')
        print('---', "You are missing all necessary requirements")
        print('')
        print("---", "Time to start your path to being a blazer.")
        print('')
        print('*** Returning to Main Menu ***')
        do_what()

    else:
        print('')
        print('---', 'You have met some of the necessary requirements.')
        print('')
        print("---", "You're almost a blazer, don't give up!")
        print('')
        print('*** Returning to Main Menu ***')
        do_what()


###############################################################################

# Framework (main) Function Call
main()
