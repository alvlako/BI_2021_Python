units = ['g', 'm', 'min']
units_alternative = ['gram', 'metre', 'minute']
units_pairs = ['stone', 'km', 'h']
units_pairs_alt = ['stone', 'kilometre', 'hour']
convert_method = [6350.29318, 1000, 60]
while True:
    print("Available units: g,stone,m,km,min,h. Print exit to exit")
    user_exit = []
    try:
        user_exit.append(input())
        if user_exit[0] == "exit" or user_exit[0] == "Exit":
            break
    except EOFError:
        continue
    print("Type 1st unit name (convert from)")
    unit_1 = str(input())
    print("Type how much units 1 you have")
    try:
        unit_number = int(input())
    except ValueError:
        print("You have to type numeric value")
    print("Type 2nd unit name (convert to)")
    unit_2 = str(input())

    def my_converter(unit_1, unit_2):
        try:
            index1 = (units+units_alternative+units_pairs+units_pairs_alt).index(unit_1)
            real_index1 = index1 % len(units)
            list_n_1 = index1//len(units)
        except ValueError:
            print("1st unit is not supported")
        try:
            index2 = (units+units_alternative+units_pairs+units_pairs_alt).index(unit_2)
            real_index2 = index2 % len(units)
            list_n_2 = index2//len(units)
            if real_index1 == real_index2 and (list_n_1 == list_n_2 or list_n_1 == (list_n_2+1) or list_n_2 == (list_n_1+1)):
                print("You typed the same units! It is not supported!")
            if real_index1 != real_index2:
                print("These types are not convertable")
            if real_index1 == real_index2 and (list_n_1 != list_n_2 or list_n_1 != (list_n_2+1) or list_n_2 != (list_n_1+1)):
                if list_n_1 > list_n_2:
                    converted_value = unit_number*convert_method[real_index1]
                    print(str(converted_value)+" "+str(unit_2))
                if list_n_1 < list_n_2:
                    converted_value = unit_number/convert_method[real_index2]
                    print(str(converted_value)+" "+str(unit_2))
        except ValueError:
            print("2nd unit is not supported")
    my_converter(unit_1, unit_2)
    
