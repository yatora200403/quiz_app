import random
import connect

def random_answer_flag_quiz() -> list:
    answer_list = []
    
    data = connect.get_db("SELECT * FROM tb_card")
    flags_name = [i[1] for i in data]

    for i in range(0,3):
        rand_num = random.randint(0, len(flags_name)-1)
        if i == 0:
            answer = flags_name[rand_num]
            answer_list.append(flags_name[rand_num])
        else:
            answer_list.append(flags_name[rand_num])
        
        flags_name.remove(flags_name[rand_num])
        random.shuffle(flags_name)
    random.shuffle(answer_list)
    return [answer_list, answer]

def random_answer_country_name() -> str:
    data = connect.get_db("SELECT * FROM tb_card")
    flag_name = [i[1] for i in data]

    rand_num = random.randint(0, len(flag_name)-1)
    answer = flag_name[rand_num]

    return answer

def random_answer_math_quiz() -> list:
    number_list = []
    for i in range(2):
        number_list.append(random.randint(1,20))
    return number_list
    
    