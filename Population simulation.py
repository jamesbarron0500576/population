# George Madeley AQA Population Code

def main_menu():
    juveniles_population = 0
    adults_population = 0
    seniles_population = 0
    juveniles_survival_rates = 0
    adults_survival_rates = 0
    seniles_survival_rates = 0
    birth_rate = 0
    new_generation_number = 0
    main_menu_TF = True
    while main_menu_TF == True:
        print("=========================================")
        print("1 - set the generation 0 values")
        print("2 - display the generation 0 values")
        print("3 - run the model")
        print("4 - export data")
        print("5 - quit")
        mm_user_input = int(raw_input(">?"))
        if mm_user_input == 1:
            print("=========================================")
            print("1 - standard generation 0 values")
            print("2 - set generation 0 vaslues")
            g0v_user_input = int(raw_input(">?"))
            if g0v_user_input == 1:
                juveniles_population = 10
                adults_population = 10
                seniles_population = 10
                juveniles_survival_rates = 1
                adults_survival_rates = 1
                seniles_survival_rates = 0
                birth_rate = 2
                new_generation_number = 10
            elif g0v_user_input == 2:
                print("set the generation 0 values for the population numbers for:")
                juveniles_population = int(raw_input("juveniles >?"))
                print("-----------------------------------------")
                adults_population = int(raw_input("adults >?"))
                print("-----------------------------------------")
                seniles_population = int(raw_input("seniles >?"))
                print("-----------------------------------------")
                print("set the generation 0 values for the survival rates for:")
                juveniles_survival_rates = int(raw_input("juveniles >?"))
                print("-----------------------------------------")
                adults_survival_rates = int(raw_input("adults >?"))
                print("-----------------------------------------")
                seniles_survival_rates = int(raw_input("seniles >?"))
                print("-----------------------------------------")
                print("set the generation 0 values for the birth rates for:")
                birth_rates = int(raw_input("birth rates >?"))
                print("-----------------------------------------")
                print("set the generation 0 values for the number of new generation to model. This should e between 5 and 25")
                new_generation_number = int(raw_input("number_of_new_generation >?"))
                new_generation_number_TF = True
                while new_generation_number_TF == True:
                    if new_generation_number < 5 or new_generation_number > 25:
                        print("plase re-enter the number of new generation becasue the previous number you enterted was not between 5 and 25")
                        new_generation_number = int(raw_input("number_of_new_generation >?"))
                        break
                    elif new_generation_number > 5 and new_generation_number < 25:
                        print("now_returning to the main menu")
                        print("=========================================")
                        new_generation_number_TF = False
            else:
                print("an error has occured")
        elif mm_user_input == 2:
            display_generation_0_values(juveniles_population, adults_population, seniles_population, juveniles_survival_rates, adults_survival_rates, seniles_survival_rates, birth_rate, new_generation_number)
        elif mm_user_input == 3:
            run_model(juveniles_population, adults_population, seniles_population, juveniles_survival_rates, adults_survival_rates, seniles_survival_rates, birth_rate, new_generation_number)
        elif mm_user_input == 4:
            export_data(juveniles_population, adults_population, seniles_population, juveniles_survival_rates, adults_survival_rates, seniles_survival_rates, birth_rate, new_generation_number)
        elif mm_user_input == 5:
            print("Are you sure you want to quit?")
            print("1 - Yes, 2 - No")
            mmq_user_input = int(raw_input(">?"))
            if mmq_user_input == 1:
                quit()
            elif mmq_user_input == 2:
                pass
            else:
                print("you entered and invalid input, plezse try again")
        else:
            ("you entered an invalid value, please try again")
            

def display_generation_0_values(juveniles_population, adults_population, seniles_population, juveniles_survival_rates, adults_survival_rates, seniles_survival_rates, birth_rate, new_generation_number):
    print("=========================================")
    print("Values of Population")
    print("Juveniles Population =", juveniles_population)
    print("Adults Population =", adults_population)
    print("Seniles Population =", seniles_population)
    print("-----------------------------------------")
    print("Values of Survival Rates")
    print("Juveniles survival rates =", (juveniles_survival_rates * 100))
    print("Adults survival rates =", (adults_survival_rates * 100))
    print("Seniles survival rates =", (seniles_survival_rates *100))
    print("-----------------------------------------")
    print("Birth rate value")
    print("birth rate = x", birth_rate)
    print("-----------------------------------------")
    print("new generation value")
    print("Number of new generation =", new_generation_number)
    

def calculation(juveniles_population, adults_population, seniles_population, juveniles_survival_rates, adults_survival_rates, seniles_survival_rates, birth_rate, new_generation_number, data_table):
    row_changer = 0
    calculation_TF = True
    while calculation_TF == True:
        try: 
            if row_changer == 0:
                data_table[row_changer][0] = row_changer
                data_table[row_changer][1] = juveniles_population
                data_table[row_changer][2] = adults_population
                data_table[row_changer][3] = seniles_population
                data_table_total = data_table[row_changer][1] + data_table[row_changer][2] + data_table[row_changer][3]
                data_table[row_changer][4] = data_table_total
            elif row_changer > 0:
                data_table[row_changer][0] = row_changer
                data_table[row_changer][1] = ((data_table[row_changer-1][2]) * 2)
                data_table[row_changer][2] = ((data_table[row_changer-1][1]) * juveniles_survival_rates)
                data_table[row_changer][3] = (((data_table[row_changer-1][2]) * adults_survival_rates) + ((data_table[row_changer-1][3]) * seniles_survival_rates))
                data_table_total = data_table[row_changer][1] + data_table[row_changer][2] + data_table[row_changer][3]
                data_table[row_changer][4] = data_table_total
            data_table_checker_y = 0
            data_table_checker_x = 0
            for y in range(new_generation_number + 1):
                for x in range(5):
                    if data_table[data_table_checker_y][data_table_checker_x] == 0:
                        if data_table_checker_y == 0 and data_table_checker_x == 0:
                            pass
                        else:
                            data_table[data_table_checker_y][data_table_checker_x] = "_"
                    elif data_table[data_table_checker_y][data_table_checker_x] > 0:
                        data_table[data_table_checker_y][data_table_checker_x] == str(data_table[data_table_checker_y][data_table_checker_x])
                    else:
                        pass
                    data_table_checker_x = data_table_checker_x + 1
                data_table_checker_x = 0
                data_table_checker_y = data_table_checker_y + 1
            row_changer = row_changer + 1
        except:
            return(data_table)
    
def run_model(juveniles_population, adults_population, seniles_population, juveniles_survival_rates, adults_survival_rates, seniles_survival_rates, birth_rate, new_generation_number):
    data_table = [[0 for row in range(5)] for col in range(0, (new_generation_number + 1))]
    x_axis_label = ["G", "J", "A", "S", "T"]
    data_table = calculation(juveniles_population, adults_population, seniles_population, juveniles_survival_rates, adults_survival_rates, seniles_survival_rates, birth_rate, new_generation_number, data_table)
    print("=========================================")
    print("G = Generation")
    print("J = juveniles")
    print("A = Adults")
    print("S = Seniles")
    print("T = Total")
    print(x_axis_label)
    for row in range(len(data_table)):
        print(data_table[row])
    print("now returning to main menu")

def export_data(juveniles_population, adults_population, seniles_population, juveniles_survival_rates, adults_survival_rates, seniles_survival_rates, birth_rate, new_generation_number):
    import os
    print("Name the file:")
    output_name = raw_input(">?")
    export_data_TF = True
    while export_data_TF == True:
        if os.path.exists(output_name) == True:
            print("A file with the same name already exists.")
            print("Do you want to overwrite this file?")
            print("1 - Yes, 2 - No.")
            overwrite_answer = int(raw_input(">?"))
            if overwrite_answer == 1:
                data_table = [[0 for row in range(5)] for col in range(0, (new_generation_number + 1))]
                data_table = calculation(juveniles_population, adults_population, seniles_population, juveniles_survival_rates, adults_survival_rates, seniles_survival_rates, birth_rate, new_generation_number, data_table)
                myfile = open(output_name, 'w')
                generation_number = 1
                for row in range(len(data_table)):
                    myfile.write('Generation' + str(generation_number) + '=' + str(data_table[row]))
                    generation_number = generation_number + 1
                myfile.close()
                print("your file has been saved successfully")
                break
            elif overwrite_answer == 2:
                print("please set a new name for your file")
                output_name = raw_input(">?")
            else:
                print("the value you enter was not accepted, please try again")
        elif os.path.exists(output_name) == False:
            data_table = [[0 for row in range(5)] for col in range(0, (new_generation_number + 1))]
            data_table = calculation(juveniles_population, adults_population, seniles_population, juveniles_survival_rates, adults_survival_rates, seniles_survival_rates, birth_rate, new_generation_number, data_table)
            myfile = open(output_name, 'w')
            generation_number = 1
            for row in range(len(data_table)):
                myfile.write('Generation' + str(generation_number) + '=' + str(data_table[row]))
                generation_number = generation_number + 1
            myfile.close()
            print("your file has been saved successfully")
            break
    

main_menu()
