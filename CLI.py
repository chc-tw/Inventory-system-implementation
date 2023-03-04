import sys
import  os
username_ = None
password_ = None
def openCLI(ini,username_):
    os.system('clear')
    username = ['boss','sales']
    passward = ['boss','sales']
    if ini ==1:
        print("******************************")
        print("Welcome to CLI invetory system")
        print("******************************")
        flag = 1
        while flag :
            username_ = input("Enter the username: ")
            if username_ == 'q':
                sys.exit()
            if username_ in username:
                flag = 0
                break
            print("username not exist")
        flag = 1
        while flag :
            passward_ = input("Enter the passward: ")
            if passward_ == 'q':
                sys.exit()
            if passward_ in passward:
                flag = 0
                break
            print("passward wrong")
    done = 1
    sales = {'sales': '張馨云', 'boss': '張文鐘'}
    name = sales[username_]
    os.system('clear')
    if username_ == 'boss':
        while done:
            print("*********************************")
            print(f"* Welcome {name} log in system. *")
            print("*********************************")
            print("Select your operation")
            print("[1]  distribution")
            print("[2]  sale")
            print("[3]  look-up")
            print("[4]  sale volume report")
            print("[q]  close system")
            op1 = input("input your operation: ")
            if op1 not in ['1','2','3','4','q']:
                print("----Invalid operation----")
                continue
            while op1 == '1':
                print("********distribution********")
                print("[1]  deliver")
                print("[2]  add")
                print("[3]  decrease")
                print("[4]  import clothes")
                print("[q]  back")
                op2 = input("input your operation: ")
                if op2 not in ['1','2','3','4','q']:
                    print("----Invalid operation----")
                    continue
                if op2 == 'q':
                    os.system('clear')
                    break
                else:
                    done = 0
                    return username_,op1,op2
            while op1 == '2':
                print("************sale************")
                print("[1]  sold")
                print("[2]  return")
                print("[q]  back")
                op2 = input("input your operation: ")
                if op2 not in ['1', '2', 'q']:
                    print("----Invalid operation----")
                    continue
                if op2 == 'q':
                    os.system('clear')
                    break
                else:
                    done = 0
                    return username_,op1, op2
            while op1 == '3':
                print("***********look-up***********")
                print("[1]  number")
                print("[2]  size and color chart")
                print("[3]  sold record")
                print("[4]  return record")
                print("[5]  detail")
                print("[q]  back")
                op2 = input("input your operation: ")
                if op2 not in ['1', '2', '3', '4','5','q']:
                    print("----Invalid operation----")
                    continue
                if op2 == 'q':
                    os.system('clear')
                    break
                else:
                    done = 0
                    return username_,op1, op2
            while op1 == '4':
                done = 0
                op2 = None
                return username_,op1,op2
            if op1 == 'q':
                os.system('clear')
                sys.exit()
    elif username_ == 'sales':
        while done:
            print("*********************************")
            print(f"* Welcome {name} log in system. *")
            print("*********************************")
            print("Select your operation")
            print("[1]  distribution")
            print("[2]  sale")
            print("[3]  look-up")
            print("[4]  sale volume report")
            print("[q]  close system")
            op1 = input("input your operation: ")
            if op1 not in ['1','2','3','4','q']:
                print("----Invalid operation----")
                continue
            while op1 == '1':
                print("********distribution********")
                print("[1]  deliver")
                print("[2]  add")
                print("[3]  decrease")
                print("[q]  back")
                op2 = input("input your operation: ")
                if op2 not in ['1','2','3','q']:
                    print("----Invalid operation----")
                    continue
                if op2 == 'q':
                    os.system('clear')
                    break
                else:
                    done = 0
                    return username_,op1,op2
            while op1 == '2':
                print("************sale************")
                print("[1]  sold")
                print("[2]  return")
                print("[q]  back")
                op2 = input("input your operation: ")
                if op2 not in ['1', '2', 'q']:
                    print("----Invalid operation----")
                    continue
                if op2 == 'q':
                    os.system('clear')
                    break
                else:
                    done = 0
                    return username_,op1, op2
            while op1 == '3':
                print("***********look-up***********")
                print("[1]  number")
                print("[2]  size and color")
                print("[3]  sold record")
                print("[4]  return record")
                print("[q]  back")
                op2 = input("input your operation: ")
                if op2 not in ['1', '2', '3','4','q']:
                    print("----Invalid operation----")
                    continue
                if op2 == 'q':
                    os.system('clear')
                    break
                else:
                    done = 0
                    return username_,op1, op2
            while op1 == '4':
                done = 0
                op2 = None
                return username_,op1,op2
            if op1 == 'q':
                os.system('clear')
                sys.exit()


def inputAction(op1,op2=None):
    if op1 == '1':
        if op2 =='1':
            print("===deliver===")
            try:
                id, size, color, num, store1, store2 =\
                    input("Enter: id,size,color,num,store1,store2 : ").split()
            except:
                print("----Invalid input----")
                return None
            return (id, size, color, num, store1, store2)
        elif op2 =='2':
            print("===add===")
            try:
                id, size, color, num =\
                    input("Enter: id, size, color, num: ").split()
            except:
                print("----Invalid input----")
                return None
            return id, size, color, num
        elif op2 =='3':
            print("===decrease===")
            try:
                id, size, color, num, store =\
                    input("Enter: id,size,color,num,store : ").split()
            except:
                print("----Invalid input----")
                return None
            return id, size, color, num, store
        elif op2 =='4':
            print("===import===")
            try:
                id, place_of_origin, material, sale, manufacture, item_no, cost, price =\
                    input("Entet: id, place_of_origin, material, sale, manufacture, item_no, cost, price : ").split()
            except:
                print("----Invalid input----")
                return None
            return (id, place_of_origin, material, sale, manufacture, item_no, cost, price)
    if op1 == '2':
        if op2 == '1':
            print("===sold===")
            try:
                id, size, color, num, cash_or_card, store, income =\
                    input("Enter: id, size, color, num, cash_or_card, store,income : ").split()
            except:
                print("----Invalid input----")
                return None
            return id, size, color, num, cash_or_card, store, income
        if op2 == '2':
            print("===return===")
            try:
                id, size, color, num, store, sold_date =\
                    input("Enter: id, size,color, num, store,sold_date : ").split()
            except:
                print("----Invalid input----")
                return None
            return id, size, color, num, store, sold_date
    if op1 =='3':
        if op2 =='1':
            print("===number===")
            id = input("Enter: id :")
            return (id)
        elif op2 =='2':
            print("===size and color===")
            id = input("Enter: id :")
            return (id)
        elif op2 =='3':
            print("===sold record===")
            date, store = input("Enter: date, store :").split()
            return (date, store)
        elif op2 =='4':
            #print("===return record===")
            #id = input("Enter: id :")
            return 1
        elif op2 =='5':
            print("===detail===")
            id = input("Enter: id :")
            return (id)

        if id == 'q':
            print("----Invalid input----")
            return None

    if op1 =='4':
        print("===sales volume===")
        try:
            period, date = input("Enter: period, date : ").split()
        except:
            print("----Invalid input----")
            return None
        return (period,date)

if __name__ == '__main__':
    ini =1
    op1,op2 = openCLI(ini)
    ini =0
    temp = inputAction(op1,op2)
    if temp == None or temp=='q':
        openCLI(ini)
    else:
        print(temp)