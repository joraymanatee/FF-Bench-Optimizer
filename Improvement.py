from Compilier import compileAll

def collect_names():
    names_list = {}
    while True:
        first_name = input("Enter your players First Name (or 'q' to quit): ")
        if first_name.lower() == 'q':
            break
        last_name = input("Enter your players Last Name (or 'q' to quit): ")
        if last_name.lower() == 'q':
            break
        names_list.append((first_name, last_name))
        print('Now add your next player.')
    return names_list

print(collect_names())
#sorted_Dictionary = print(compileAll())
sorted_Dictionary = {'Christian McCaffrey': 0, 'CeeDee Lamb': 1}

for key in sorted_Dictionary:
    if 


