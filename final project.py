import mysql.connector as mys
mycon=mys.connect(host='localhost',user='root',passwd='bentom',database='admin')
from tabulate import tabulate

def accsessteacheradmin() :
    while True:
              
               print('Enter "1" to view TEACHER details')
               print('Enter "2" to insert new details into TEACHER details')
               print('Enter "3" to update existing details from TEACHER details')
               print('Enter "4" to delete a detail of a particular student from TEACHER details')
               print('Enter "5" to exit this TEACHER details')
               enter=(input('ur choice pls:'))
               if enter=='1':
                   print('==================================================================================================================')  
                   mycursor=mycon.cursor()
                   mycursor.execute('select*from student')
                   mydata=mycursor.fetchall()
                   l=[]
                   for row in mydata:
                      l.append(row)
                   print(tabulate(l,headers=['ID','NAME','CLASS','SECTION','SEX','NATIONALITY','SALARY','SUBJECT'])) 
                   print()
                   print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+'*2)
                   print('*************************************************************'*2)
               elif enter=='2':
                   print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+'*2)
                   a='y'
                   while a=='y' or a== 'Y':
                       mycursor=mycon.cursor()
                       eno=(input('Enter ID'))
                       if eno.isdigit():
                           pass
                       else:
                           print('only int')
                           eno=int(input('eid'))
                       x=[]
                       mycursor.execute('select id from teacher')
                       mydata=mycursor.fetchall()
                       for row in mydata:
                           for i in row:
                               x.append(i)
                       if  eno not in x :
                           en=int(eno)
                           pass
                       else:
                           print(' SORRY ID ALREADY EXISTS ')
                           break
                       same=input('Enter NAME')
                       if same.isalpha():
                           pass
                       else:
                           print('only string')
                           same=input('enter name')
                       clas=(input('Enter CLASS'))
                       if clas.isdigit():
                           clas=int(clas)
                           pass
                       else:
                           print('wrong only int')
                           clas=int(input('e'))
                       section=input('Enter SECTION')
                       if section.isalpha():
                           pass
                       else:
                           print('only string')
                           section=input('enter name')
                       sex=input('Enter M/F')
                       if sex.isalpha():
                           pass
                       else:
                           print('only string')
                           sex=input('enter name')
                       na=input('Enter Nationalility')
                       if na.isalpha():
                           pass
                       else:
                           print('only string')
                           na=input('enter name')
                       sal=(input('enter salary'))
                       if sal.isdigit():
                           sal=int(sal)
                           pass
                       else:
                           print('wrong only int')
                           sal=int(input('e'))
                       sub=input('enter sub')
                       if sub.isalpha():
                           pass
                       else:
                           print('only string')
                           sub=input('enter name')
                       q='insert into teacher values ({0},"{1}",{2},"{3}","{4}","{5}",{6},"{7}")'.format(en,same,clas,section,sex,na,sal,sub)
                       mycursor.execute(q)
                       mycon.commit()
                       print('*****************************************Succesfully added***************************************************')
                       a=input('Do you want to enter more STUDENT details?(Y/N):')
                       if a=='n' or a=='N' or a=='y' or a=='Y':
                           pass
                       else:
                           print('wrong choice')
                           a=input('do u want to enter more statement:')
                       print('=============================================================================================================')
               elif enter=='3':
                   print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+'*2)
                   a='y'
                   while a=='y' or a=='y':
                       mycursor=mycon.cursor()
                       q=input('enter ur change: ')
                       f=input('enter ur condition (only id):id=')
                       mycursor.execute("update  teacher set " + str(q) + " where id =" +f)
                       mycon.commit()
                       print('succesfully updated')
                       a=input('do u want to enter more statement:')
                       if a=='n' or a=='N' or a=='y' or a=='Y':
                           pass
                       else:
                           print('wrong choice')
                           a=input('do u want to enter more statement:')
                       print('===============================================================================================================')

               elif enter=='4':
                   print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+'*2)
                   a='y'
                   while a=='y'or a== 'Y':
                       mycursor=mycon.cursor()
                       q=input('Enter condition from teacher details which is to be deteleted:')
                       mycursor.execute('delete from teacher where '+q)
                       mycon.commit()
                       print('******************************************Succesfully deleted***************************************************')
                       print('================================================================================================================')
                       a=input('do u want to enter more statement(Y/N):')
                       if a=='n' or a=='N' or a=='y' or a=='Y':
                           pass
                       else:
                           print('wrong choice')
                           a=input('do u want to enter more statement:')
                               
               elif enter==5:
                   print('thank u')
                   break
               else:
                   print('WRONG CHOICE')
def showstudent(name):
    while True:
        print('Enter "1" if u want to retrieve your attendence for a particular date')
        print('Enter "2" if u want to retrieve the attendence for a your name')
        print('Enter "3" if u want to return')
        choice=(input('enter your choice'))
        if choice=='1':
            f=input('enter your date (format(DD/MM/YYYY))')
            if '"' in f:
               pass
            else:
                f='"'+f+'"'
            if '"' in name:
                pass
            else:
                name='"'+name+'"'
            mycursor=mycon.cursor()
            mycursor.execute("select date,attendance from attendance where name= "+name +" and date="+f)#CHECK
            mydata=mycursor.fetchall()
            l=[]
            for row in mydata:
                l.append(row)
            print(tabulate(l,headers=['DATE','ATTENDANCE']))
            print()
            
        elif choice=='2':
            #N=input('enter name')
            if '"' in name:
                pass
            else:
                name='"'+name+'"'
            mycursor=mycon.cursor()
            mycursor.execute("select*from attendance where name="+name)
            mydata=mycursor.fetchall()
            l=[]
            for row in mydata:
                l.append(row)
            print(tabulate(l,headers=['NAME','DATE','ATTENDANCE'])) 
            print()
        elif choice=='3':
            print('thank you')
            break
        else:
            print('wrong choice')
    
def custom():
    while True:
        print('Enter "1" if u want to retrieve the attendence for a particular date')
        print('Enter "2" if u want to retrieve the attendence for a particular name')
        print('Enter "3" if u want to return')
        choice=(input('enter your choice'))
        if choice=='1':
            f=input('enter your date (format(DD/MM/YYYY))')
            mycursor=mycon.cursor()
            x=[]
            mycursor.execute('select date from attendance')
            mydata=mycursor.fetchall()
            
            if '"' in f:
                pass
            else:
                f='"'+f+'"'
            
            mycursor.execute("select*from attendance where date= "+(f))
            mydata=mycursor.fetchall()
            l=[]
            for row in mydata:
                l.append(row)
            print(tabulate(l,headers=['NAME','DATE','ATTENDANCE']))
            print()
        elif choice=='2':
                f=input('enter your NAME')
                if '"' in f:
                    pass
                else:
                    f='"'+f+'"'
                mycursor=mycon.cursor()
                mycursor.execute("select*from attendance where name= "+f)
                mydata=mycursor.fetchall()
                l=[]
                for row in mydata:
                   l.append(row)
                print(tabulate(l,headers=['NAME','DATE','ATTENDANCE'])) 
                print()
        elif choice=='3':
            print('thank you')
            break
        else:
            print('wrong choice') 
def teacherdetail(name):#check again
    
    if '"' in name:
        pass
    else:
        name='"'+name+'"'
    mycursor=mycon.cursor()
    mycursor.execute("select*from teacher where name="+name)
    mydata=mycursor.fetchall()
    l=[]
    for row in mydata:
        l.append(row)
    print(tabulate(l,headers=['ID','NAME','CLASS','SECTION','SEX','NATIONALITY','SALARY','SUBJECT']))
    print()
    
def see():
   while True:
       print('Enter "1" if you want to see custom attendence')
       print('Enter "2" if you just want to retrieve ')
       print('Enter "3" if u want to return')
       enter=(input('enter choice'))
       if enter=='1':
           custom()
       elif enter=='2':
           mycursor=mycon.cursor()
           mycursor.execute('select*from attendance')
           mydata=mycursor.fetchall()
           l=[]
           for row in mydata:
              l.append(row)
           print(tabulate(l,headers=['NAME','DATE','ATTENDANCE'])) 
           print()
           print('*********************************************************************************')
       elif choice=='3':
            print('thank you')
            break
       else:
            print('wrong choice')
def mark():
    x=[]
    mycursor=mycon.cursor()
    mycursor.execute('select name from  student')
    mydata=mycursor.fetchall()
    for row in mydata:
        for i in row:
            x.append(i)
    date=input('Enter your DATE(DD/MM/YYYY) to mark absent/present')
    t=[]
    mycursor.execute('select date from attendance')
    mydata=mycursor.fetchall()
    for row in mydata:
        for i in row:
            t.append(i)
    if  date not in x :
        en=date
        pass
    else:
        print(' wrong id only ')
        #break 
    for i in x:
        name=i
        d=en
        attendence=input('Is '+i+' Present/Absent(only enter P/A) :')
        x= attendence.upper()
        if x=='P' or x=='A':
            pass
        else:
            print('enter only correct attendance (only P/A)')
            break
        attendence=attendence.upper()
        q='insert into attendance values ("{0}","{1}","{2}")'.format(name,d,attendence)
        mycursor.execute(q)
        mycon.commit()
        print('**************************************************Succesfully Added**************************************************')
def teacher(name):
    while True:
         
        print('Enter "1" to mark the attendance of the students')
        print('Enter "2" to see your register')
        print('Enter "3" to see your personal details')
        print('Enter "4" if u want to return')
        enter=(input('enter choice'))
        if enter=='1':
            mark()
        elif enter=='3':
            
            teacherdetail(name)
        elif enter=='2':
            see()
        elif enter=='4':
            break
        else:
            print('wrong choice')
def logteacher(name):
       for j in range(2,-1,-1):
            x=[]
            mycursor=mycon.cursor()
            mycursor.execute('select name from teacher')
            mydata=mycursor.fetchall()
            for row in mydata:
                  for i in row:
                        x.append(i)
                
            #name=input('Enter UserName:')
            password=input('Enter Password')
            if name in x :
                  if password=='1234':
                        teacher(name)
                        break
                  else:
                    print(' Wrong PASSWORD only '+ str(j+1) +' chances left ')
            else:
                print(' UserName not identified ')
                break
def accesesstudents(name):
    print('****************************************************************************************************************')
    print('Hey here are your details')
    #N=input('enter name')
    if '"' in name:
        pass
    else:
        name='"'+name+'"'
    
    print('------------------------------------------------------------------')
    mycursor=mycon.cursor()
    mycursor.execute('select*from student where name='+name)
    mydata=mycursor.fetchall()
    l=[]
    for row in mydata:
        l.append(row)
    print(tabulate(l))
    print()
    print('=================================================================================================================')
    
def accesesstudent(name):
    while True:
        print('Enter "1" if you want to see your details')
        print('Enter "2" if you want to see your attendence details')
        print('Enter "3" if u want to return')
        choose=(input('Enter your choice'))
        if choose=='1':
            accesesstudents(name)
        elif choose=='2':
            showstudent(name)
        elif choose=='3':
            print('THANK YOU HAVE A NICE DAY')
            break
        else:
            print('wrong choice')
def logstudent(name):
    for j in range(3,0,-1):
        x=[]
        mycursor=mycon.cursor()
        mycursor.execute('select name from student')
        mydata=mycursor.fetchall()
        for row in mydata:
            for i in row:
                x.append(i)
                
            #name=input('Enter UserName:')
        password=input('Enter Password')
        if name in x :
                if password=='1234':
                    accesesstudent(name)
                    break
                else:
                    print(' Wrong PASSWORD only '+ str(j+1) +' chances left ')
        else:
            print(' UserName not identified ')
            break 
   
    
def accesesadmin():
    while True:
        print('Enter "1" for using teachers information')
        print('Enter "2" for using students information')
        print('Enter "3" if u want to return')
        choose=(input('Enter your option'))
        if choose=='1':
            accsessteacheradmin()
        elif choose=='2':
           while True:
              
               print('Enter "1" to view STUDENT details')
               print('Enter "2" to insert new details into STUDENT details')
               print('Enter "3" to update existing details from STUDENT details')
               print('Enter "4" to delete a detail of a particular student from STUDENT details')
               print('Enter "5" to exit this STUDENT details')
               enter=(input('ur choice pls:'))
               if enter=='1':
                   print('==================================================================================================================')  
                   mycursor=mycon.cursor()
                   mycursor.execute('select*from student')
                   mydata=mycursor.fetchall()
                   l=[]
                   for row in mydata:
                      l.append(row)
                   print(tabulate(l,headers=['ID','NAME','CLASS','SECTION','SEX','NATIONALITY'])) 
                   print()
                   print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+'*2)
                   print('*************************************************************'*2)
               elif enter=='2':
                   print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+'*2)
                   a='y'
                   while a=='y' or a== 'Y':
                       mycursor=mycon.cursor()
                       eno=(input('Enter ID'))
                       if eno.isdigit():
                           eno=int(eno)
                           pass
                       else:
                           print('only int')
                           eno=int(input('enter id'))
                           
                       x=[]
                       mycursor.execute('select id from student')
                       mydata=mycursor.fetchall()
                       for row in mydata:
                           for i in row:
                               x.append(i)
                       if  eno not in x :
                           en=eno
                           pass
                       else:
                           print(' ID EXISTS')
                           break
                       same=input('Enter NAME')
                       if same.isalpha():
                           pass
                       else:
                           print('only str')
                           same=input('enter name')
                       clas=(input('Enter CLASS'))
                       if clas.isdigit():
                           clas=int(clas)
                           pass
                       else:
                           print('only int')
                           clas=int(input('enter class'))
                           
                       section=input('Enter SECTION')
                       if section.isalpha():
                           pass
                       else:
                           print('only str')
                           section=input('enter sec')
                       sex=input('Enter M/F')
                       if sex.isalpha():
                           pass
                       else:
                           print('only str')
                           sex=input('enter sec')
                       na=input('Enter Nationalility')
                       if na.isalpha():
                           pass
                       else:
                           print('only str')
                           na=input('enter sec') 
                       q='insert into student values ({0},"{1}",{2},"{3}","{4}","{5}")'.format(en,same,clas,section,sex,na)
                       #s='insert into attendance values("{0}")'.format(same)
                       mycursor.execute(q)
                       mycon.commit()
                       print('*****************************************Succesfully added***************************************************')
                       a=input('Do you want to enter more STUDENT details?(Y/N):')
                       print('=============================================================================================================')
               elif enter=='3':
                   print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+'*2)
                   a='y'
                   while a=='y' or a=='Y':
                       mycurcor=mycon.cursor()
                       q=input('enter ur change :')
                       f=input('enter ur condition (only id):id=')
                       mycursor.execute("update  student set  "+ str(q) +"  where id = "+f)
                       mycon.commit()
                       print('succesfully updated')
                       a=input('do u want to enter more statement:')
                       print('===============================================================================================================')
               elif enter=='4':
                   print('+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+'*2)
                   a='y'
                   while a=='y'or a== 'Y':
                       mycursor=mycon.cursor()
                       q=input('Enter condition from student details which is to be deleted:')
                       mycursor.execute('delete from student where '+q)
                       
                       mycon.commit()
                       print('******************************************Succesfully deleted***************************************************')
                       print('================================================================================================================')
                       a=input('do u want to enter more statement(Y/N):')
                               
               elif enter=='5':
                   break
        elif choose=='3':
            print('\t\t\t\t\t\t\tTHANK YOU HAVE A NICE DAY')
            break
        else:
            print('wrong choice')

def logadmin():
    for i in range(2,-1,-1):
        username=input('Enter ADMIN UserName:')
        password=input('Enter ADMIN  Password')
        if username=='admin':
            if password=='1234':
                accesesadmin()
                print('\t\t\t\t\t\t********************WELCOME ADMIN TO MAINPAGE******************')
                break
            else:
                print('Wrong password given given ' +  str(i) +  '  more chances left')
        else:
            print('UserName not identified'+ str(i) +'more chances')
            
        
    

    
    
def main():
    print('\n\t\t\t\t\t\t******************************************************\t\t\t\t\t\t\t\t\t\t\t')
    print('\n\t\t\t\t\t\t**********************WELCOME*************************\t\t\t\t\t\t\t\t\t\t\t')
    print('\n\t\t\t\t\t\t******************************************************\t\t\t\t\t\t\t\t\t\t\t')
    while True:
        
        print('Please enter "1" for using as a ADMIN')
        print('Please enter "2" for using as a TEACHER')
        print('Please enter "3" for using as a STUDENT')
        print('Please enter "4" for to EXIT')
        choice=(input('enter ur field'))
        if choice=='3':
            print('\t\t\t\t\t\t******************WELCOME TO STUDENT LOGIN***************')
            name=input('Enter your NAME')
            logstudent(name)
        elif choice=='1':
            print('\t\t\t\t\t\t*****************WELCOME TO ADMIN LOGIN******************')
            logadmin()
        elif choice=='2':
            print('\t\t\t\t\t\t****************WELCOME TO TEACHER LOGIN******************')
            name=input('Enter your NAME')
            logteacher(name)
        elif choice=='4':
            print('bye')
            break
        else:
            print('WRONG CHOICE')
            
main()

