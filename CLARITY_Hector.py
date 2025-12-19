from random import randint

def clarity() : 
    print("***************************** CLARITY *****************************\n\nThe system has been loaded, ready to hack X)\n\nInfo : \n\n  Clarity is a system witch refines results with victim's data you gave.\n  Here is the list of the informations accept by clarity : \n\n   1. Name\n\n   2. Surname\n\n   3. Birthdate\n\n   4. Pet's name\n\n   5. Child's name\n\n   6. Child's birthdate\n\n   7. Wedding date\n\n   8. Size of the password\n\n   9.Type of password (number, alphanumeric, alphanumeric + special caractere)\n\n  Firstly, clarity will tries the 1000 most used password. If the systeme didn't find the victim's password, the second wave is lauched. Second wave is trying password with the info you gave\n  If Clarity does not allowed to hack the victime, the third wave is lauched. The third wave try the 1 000 000 most used password.\n  Finaly, if the victim isn't been hacked yet, the system goes to is final phase. The final wave try random password until the victim isn't hacked (but not retrying password of precedent wave) \n\n")
    tries = 0
    clarity_password = '' 
    tested_password = []
    password = '1304'
    info_victim_input = input("Is you have information usable by clarity about the victim (y or n) : ")
    if info_victim_input == 'y' : #PrÃ©paration au lancement de la vague 1
        type_info = list(input("Select the numbers associated to the info you have (ex : 1;2;3;4): "))
        d_info = {1 : 'name', 2 : 'surname', 3 : 'birthdate', 4 : "pet's name", 5 : "child's name", 6 : "child's birthdate", 7 : 'weeding date', 8 : 'size of the password', 9 : 'type of the password'}
        for k in type_info :
            list_info = d_info[type_info[k]]
    alphabet_chiffre = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print("Clarity with parameters {type_info} has been loaded, ready to lauch the first wave.")
    first_wave_launching = input("Is you want to lauch the first wave (y or n) : ")
    if first_wave_launching == 'y' :
        while clarity_password != password :
            for j in list_info :
                if j == 1 :
                    name = j
                    clarity_password = name
                    if clarity_password == password : 
                        break
                    else : 
                        tested_password.append(clarity_password)
                        tries += 1
                    for a in range(100) : 
                        clarity_password = name + str(a)
                        if clarity_password == password : 
                            break
                        else : 
                            tested_password.append(clarity_password)
                            tries += 1
                    for b in range(20) : 
                        for c in range(b) : 
                            for d in range(len(name)) :
                                random_index = randint(0,len(name - 1))
                                for e in alphabet_chiffre : 
                                    if b == 0 : 
                                        name.pop(random_index)
                                        clarity_password = name.insert(random_index, e)
                                        if clarity_password == password : 
                                            break
                                        else : 
                                            tested_password.append(clarity_password)
                                            tries += 1
                                    else : 
                                        clarity_password = name[random_index] + e
                                        if clarity_password == password : 
                                            break
                                        else : 
                                            tested_password.append(clarity_password)
                                            tries += 1
    elif first_wave_launching == 'n' : 
        print('No problem, you can come back later !')
    print(f"The victim has been hacked. The password is {clarity_password}. Victim has been hacked in {tries} tries")
clarity()
