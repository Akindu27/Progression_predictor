# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1956405
# Date: 03/12/2022


students_marks={}                               #opened a dictionary to add the user inputed student marks with outcomes.
acceptable_marks=(0,20,40,60,80,100,120)
progress_count=0
trailer_count=0
retriever_count=0
exclude_count=0

def integer_validation (message):                                                    #used a user defined function for check the validity of the user's input
    
    while True:                                         #used a while loop to iterate until the user's input satisfy the logic
        try:
            mark_entry=int(input(message))
            if ((mark_entry > 120) or (mark_entry not in acceptable_marks)):
                print("...Out of range...")
                continue
            if ((mark_entry < 0) or (mark_entry not in acceptable_marks)):
                print("...Out of range...")
                continue
            break
        except ValueError:
            print("...Integer Required...")
    return mark_entry

while True:                                                                                             #used another while loop to iterate multiple outcomes
    student_id=input("\nEnter student's ID: ")
    if len(student_id) == 8 and student_id[0].lower()=='w':
        if student_id not in students_marks :
            
            pass_mark = integer_validation ("\nPlease enter your credits at pass: ")        #called out the integer_validation user defined function
            defer_mark = integer_validation ("Please enter your credits at defer: ")
            fail_mark = integer_validation ("Please enter your credits at fail: ")
                    
            total= pass_mark + defer_mark + fail_mark                                       #checking the conditions of the user's input and displaying the outcome
            if total == 120 :                                               
                if pass_mark == 120:
                    print("\nProgress")
                    progress_count+=1
                    students_marks[student_id]="Progress -",pass_mark,defer_mark,fail_mark      #adding the student id as the key with input marks and the outcomes as values to the dictionary.
                elif pass_mark == 100:
                    print("\nProgress (module trailer)")
                    trailer_count+=1
                    students_marks[student_id]="Progress (module trailer) -",pass_mark,defer_mark,fail_mark
                elif pass_mark + defer_mark >= fail_mark:
                    print("\nModule retriever")
                    retriever_count+=1
                    students_marks[student_id]="Module retriever -",pass_mark,defer_mark,fail_mark
                elif pass_mark  + defer_mark < fail_mark:
                    print("\nExclude")
                    exclude_count+=1
                    students_marks[student_id]="Exclude -",pass_mark,defer_mark,fail_mark
                while True:                                                                                     #used another while loop to ask the user whether is in need for enter more inputs or need to quit
                    print("\nWould you like to enter another set of data?")
                    response=input("Enter 'y' for yes or 'q to quit and view results: ").lower()
                    if response=="y":
                        break
                    elif response =="q":
                        break
                    else :
                        print("...Wrong Input...")
                        continue
                if response=="y":
                    continue
                elif response =="q":
                    print("-"*75,"\nHistogram")                                                         #prints the histogram with the outcomes using asteriks one after another
                    print('Progress\t',progress_count,': ',progress_count*'*','\n'
                          'Trailer    \t' ,trailer_count,': ',trailer_count*'*','\n'
                          'Retriever\t',retriever_count,': ',retriever_count*'*','\n'
                          'Excluded\t',exclude_count,': ',exclude_count*'*')
                    outcomes= progress_count + trailer_count + retriever_count + exclude_count
                    print('\n',outcomes," outcomes in total.\n"+"-"*75)
                    print("Part 4: \n")
                    for (student,marks) in students_marks.items():                                      #used (key,value) method in a for loop to print the saved data in the dictionary.
                        print(student, ":",marks[0], marks[1],",",marks[2],",",marks[3])
                    break
            else:
                print("...Total incorrect...")                        
        else:
            print("You have entered the same Student ID before! ")
    else:
        print("Wrong ID number... Please enter an ID with 8 characters starting with 'w'.\n")               
           
