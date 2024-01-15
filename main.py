data = {
    "т-293": {},
}


def set_student_name():
    name = input('введите номер ученика: ').lower()
    while name not in [str(i) for i in range(1, len(data[group_get].keys()) + 1)]:
        name = input('в группе нет такого ученика попробуйте еще раз: ').lower()
    return name

def set_student_group():
    group = input('введите номер группы ученика: ').lower()
    while group not in data.keys():
        group = input('вы неправильно ввели номер группы, попробуйте еще раз: ').lower()
    return group

def continue_work():
    is_continue = input('введите \'+\', если хотите прекратить работу с приложением, или \'-\', если выйти: ')
    while is_continue not in '+-':
            is_continue = input('комманда не была распознанна, повторите ввод: ')
    if is_continue == '-':
        return False
    return True

while True:
    answer = input('вы хотите получить информацию об ученике, добавить нового(п, д, у): ').lower()
    while answer not in 'дпу':
        answer = input('не был получен адыкватный ответ, попробуйте еще раз(п, д, у): ').lower()
    match answer:
        case 'д':
            group_add = set_student_group()

            name_add = input('введите имя ученика: ').lower()

            group_health_add = input('введите группу здоровья ученика(смг, основная, подготовительная, лфк): ').lower()
            while group_health_add not in 'смг основная подготовительная лфк'.split():
                group_health_add = input('вы неправильно ввели группу здоровья ученика, попробуйте еще раз: ').lower()

            invalid = True
            while invalid:
                try: 
                    extra_info = input('введите дополнительную информацию в формате(номер телефона:+56211656622, место-проживания:ул пупы 29)')
                    if extra_info:
                        details_save = {value.split(':')[0]: value.split(':')[1] for value in extra_info.split(',')}
                        invalid = False
                    else:
                        details_save = {}
                        invalid = False
                except IndexError:
                    print("вы неправильно ввели данные, обратите внимание на необходимый формат введенных данных, или нажмите enter, чтобы продолжить без их ввода")

            data[group_add][name_add] = (group_health_add, details_save)
            print(f'ученик {name_add} был добавлен/добавлена в базу данных')

            if not continue_work():
                break

        case 'п':
            group_get = set_student_group()
            
            if data[group_get]:
                print('список учащихся группы:')
                for num, i in enumerate(data[group_get].keys()):
                    print(f'{num + 1} - {i}')

                name_get = set_student_name()
                student = data[group_get][list(data[group_get].keys())[int(name_get) - 1]]

                print('студент: ', list(data[group_get].keys())[int(name_get) - 1])
                print('группа: ', group_get)
                print('группа здоровья: ', student[0])
                for detail_name in student[1]:
                    print(f'{detail_name if detail_name[0] != " " else detail_name[1:]}: ', student[1][detail_name])
            else:
                print('в этой группе нет учеников')

            if not continue_work():
                break

        case 'у':
            group_get = set_student_group()

            if data[group_get]:
                print('список учащихся группы:')
                for num, i in enumerate(data[group_get].keys()):
                    print(f'{num + 1} - {i}')

                name_get = set_student_name()
                
                print(f'ученик {list(data[group_get].keys())[int(name_get) - 1]} был удален/удаленна из базы данных')
                del data[group_get][list(data[group_get].keys())[int(name_get) - 1]]
            else:
                print('в этой группе нет учеников')

            if not continue_work():
                break


