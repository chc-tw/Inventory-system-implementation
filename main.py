from action import action_
import CLI
import os
import pandas as pd
import warnings
print("AWS RDS connecting...")
warnings.filterwarnings("ignore")
###
color = pd.read_csv('Data/color.csv')
color = color['color']
manufacture = pd.read_csv('Data/manufacture.csv')
manufacture = manufacture['manufacture']
clothesType = {'A':'洋裝', 'B':'褲子', 'C':'裙子', 'D':'襯衫','E':'外套','F':'上衣', 'G':'套裝', 'H':'背心', 'L':'鞋子'}
place_of_origin = {'A':'太平', 'B':'廣州', 'H':'香港', 'K':'韓國', 'J':'日本'}
###

ini = 1
username_ = None
action = action_()
action.connect()
sales = {'sales':'張馨云','boss':'張文鐘'}
username_, op1, op2 = CLI.openCLI(ini, username_)
name = sales[username_]
while True:
    if ini == 1:
        ini += 1
    inputArg = CLI.inputAction(op1, op2)
    if inputArg == None or inputArg == 'q':
        username_, op1, op2 = CLI.openCLI(ini, username_)
    os.system('clear')
    if op1 == '1':
        if op2 == '1':
            try:
                action.deliver(inputArg[0],inputArg[1],inputArg[2],inputArg[3],inputArg[4],inputArg[5])
                print("Action Done!")
            except Exception as error:
                print(error)
        elif op2 == '2':
            try:
                action.add(inputArg[0],inputArg[1],inputArg[2],inputArg[3])
                print("Action Done!")
            except Exception as error:
                print(error)
        elif op2 == '3':
            try:
                action.decrease(inputArg[0],inputArg[1],inputArg[2],inputArg[3],inputArg[4])
                print("Action Done!")
            except Exception as error:
                print(error)
        elif op2 == '4':
            try:
                action.importClothes(inputArg[0],inputArg[1],inputArg[2],inputArg[3],inputArg[4],inputArg[5],inputArg[6],inputArg[7])
                print("Action Done!")
            except Exception as error:
                print(error)
    if op1 == '2':
        if op2 == '1':
            try:
                action.sold(inputArg[0], inputArg[1], inputArg[2], inputArg[3], inputArg[4],name, inputArg[5],inputArg[6])
                print("Action Done!")
            except Exception as error:
                print(error)
        elif op2 == '2':
            try:
                action.exchange(inputArg[0], inputArg[1], inputArg[2], inputArg[3], inputArg[4], inputArg[5])
                print("Action Done!")
            except Exception as error:
                print(error)
    if op1 == '3':
        if op2 == '1':
            try:
                table = action.number(inputArg)
                for i in range(len(table)):
                    table['color'][i] = color[table['color'][i]]
                print("Action Done!")
                print(table)
            except Exception as error:
                print(error)
        elif op2 == '2':
            try:
                table = action.colorAndsize(inputArg)
                print("Action Done!")
                for i in range(len(table)):
                    table['color'][i] = color[table['color'][i]]
                print(table)
            except Exception as error:
                print(error)
        elif op2 == '3':
            try:
                table = action.soldRecord(inputArg[0],inputArg[1])
                print("Action Done!")
                for i in range(len(table)):
                    table['color'][i] = color[table['color'][i]]
                    if table['cash_or_card'][i] == 0:
                        table['cash_or_card'][i] = 'cash'
                    else:
                        table['cash_or_card'][i] = 'card'
                print(table)
            except Exception as error:
                print(error)
        elif op2 == '4':
            try:
                table = action.exchangeRecord()
                print("Action Done!")
                for i in range(len(table)):
                    table['color'][i] = color[table['color'][i]]
                print(table)
            except Exception as error:
                print(error)
        elif op2 == '5':
            try:
                table = action.detail(inputArg)
                for i in range(len(table)):
                    table['place_of_origin'][i] = place_of_origin[table['place_of_origin'][i]]
                    table['manufacture'][i] = manufacture[table['manufacture'][i]]
                print("Action Done!")
                print(table)
            except Exception as error:
                print(error)
    if op1 == '4':
        try:
            k1_report, k3_report, k4_report = action.salesVolume(inputArg[0],inputArg[1])
            print("Action Done!")
            print(f"k1 {inputArg[0]} report - {inputArg[1]}")
            print(k1_report)
            print(f"k3 {inputArg[0]} report - {inputArg[1]}")
            print(k3_report)
            print(f"k4 {inputArg[0]} report - {inputArg[1]}")
            print(k4_report)
        except Exception as error:
            print(error)
    input("Press Enter to continue...")
    username_, op1, op2 = CLI.openCLI(ini, username_)


