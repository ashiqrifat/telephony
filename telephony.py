import csv
import time

#links printer
def print_line():
    print(' ## Line status ## ')
    print(' Line : Status')
    for i in range(len(links[0])):
        print('  ',links[0][i],'    ',links[1][i] )
#call record print
def print_call_rec():
    print(' ## Call Record ## ')
    print(' From :  To  : Length : Arrival :')
    for item in nlist:
        print(' ',item[0],' '*(2-len(str(item[0]))),':'
              '  ',item[1],' :'
              ' ',item[2],' '*(4-len(str(item[2]))),':'
              ' ',item[3],' '*(5-len(str(item[3]))),':')
#print running calls
def print_running_calls(incall):
    print(' ## Running Calls ## ')
    print(' From :  To  :  End   :')
    for item in running_calls:
        print(' ',item[0],' '*(2-len(str(item[0]))),':'
              '  ',item[1],' :'
              ' ',item[2],' '*(4-len(str(item[2]))),':')
#print busy que
def print_busy_que():
    print(' ## Busy queue ## ')
    print(' From :  To  : Length :')
    for item in busy:
        print(' ',item[0],' '*(2-len(str(item[0]))),':'
              '  ',item[1],' :'
              ' ',item[2],' '*(4-len(str(item[2]))),':'
              ' ',item[3],' '*(5-len(str(item[3]))),':')
def print_p():
    print(' ## information ## ')
    print(' processed :   completed : blocked :  Busy ')
    print(counter)
#bysy connector
def try_busy(busy1):
    print('!!!!!!!!!!!!!!!!!!!!!!!!',busy1)
    
    
#next call variables
def set_call_var(call_no):
    global incall
    global no_busy
    s_events.pop(call_no)
    incall+=1
    print(len(running_calls))  
    if(len(running_calls)<3):
        
        f=nlist[call_no][0]
        t=nlist[call_no][1]
        l=nlist[call_no][2]
        a=nlist[call_no][3]
        e=l+a
        #print('in call lists:',f,t,l,a,e, incall)
        if(links[1][f-1]==0 and links[1][t-1]==0):
            #print("call in", len(running_calls))
            #print(incall-1)
            #print(running_calls)
            links[1][f-1]=1
            links[1][t-1]=1
            temp=[]
            temp.append(f)
            temp.append(t)
            temp.append(e)
            running_calls.append(temp)
            e_events.append(e)
            #print_line()
            nlist.pop(call_no)
            #print_call_rec()
            #print(running_calls)
            #print_running_calls(incall)
        else:
            counter[0]+=1
            counter[3]+=1
            print('busy busy busy',busy)
            incall-=1
            no_busy+=1
            temp2=[]
            temp2.append(f)
            temp2.append(t)
            temp2.append(l)
            temp2.append(a)
            busy.append(temp2)
            nlist.pop(call_no)
            
    else:
        counter[0]+=1
        counter[2]+=1
        print('blocked ',incall)
        nlist.pop(call_no)
        incall-=1

#call close
def pop_to_heaven(popper):
    counter[0]+=1
    counter[1]+=1
    global incall
    incall-=1
    f=running_calls[popper][0]
    t=running_calls[popper][1]
    links[1][f-1]=0
    links[1][t-1]=0
    #print('haven',incall,f,t)
    running_calls.pop(popper)
    e_events.pop(popper)
    if(len(busy)!=0):
        for i in range(len(busy)):
            f=busy[i][0]
            t=busy[i][1]
            if(links[1][f-1]==0 and links[1][t-1]==0):
                links[1][f-1]=1
                links[1][t-1]=1
                l=busy[i][2]
                a=busy[i][3]
                s=min(e_events)
                e=l+s
                temp=[]
                temp.append(f)
                temp.append(t)
                temp.append(e)
                running_calls.append(temp)
                e_events.append(e)
                busy.pop(i)
                break
                
    #print_running_calls(incall)
    

#read csv
with open('f.csv', 'r') as f:
  reader = csv.reader(f)
  nlist = list(reader)

#string to int
for i in range(len(nlist)):
    for j in range(len(nlist[i])):
        nlist[i][j] = int(nlist[i][j])
        
#time delay
print(nlist)
time.sleep(0)

#program strt
#program strt
no_busy = 0
incall = 0
#strt evnt capture
s_events=list()
for i in range(len(nlist)):
    s_events.append(nlist[i][3])
#busy lists
busy=[]
#end events
e_events=list()

counter=[100,80,10,50]
#running calls
running_calls=[]
#initiate lnks
links=[[1,2,3,4,5,6,7,8],[0,0,0,0,0,0,0,0]]

#print calls
#print_call_rec()
#print_line()
print_call_rec()
print_line()
#for loop in range(len(nlist)):
var=1
while var==1:
    time.sleep(0)
    print('')
    print('')
    #print('   START   ',s_events)
    #print('   END   ',e_events)

    if(len(s_events)!=0):
        if(len(e_events)==0):
            print('     event   :',min(s_events))
            ncall=s_events.index(min(s_events))
            set_call_var(ncall)
            print_call_rec()
            print_line()
            print_running_calls(incall)
            print_busy_que()
            
            
        elif(min(s_events)<min(e_events)):
            print('     event   :',min(s_events))
            ncall=s_events.index(min(s_events))
            set_call_var(ncall)

            print_call_rec()
            print_line()
            print_running_calls(incall)
            print_busy_que()
            
        elif(min(s_events)>min(e_events)):
            print('     event   :',min(e_events))
            popper = e_events.index(min(e_events))
            pop_to_heaven(popper)

            print_call_rec()
            print_line()
            print_running_calls(incall)
            print_busy_que()     
        else:
            print('    else    ')
    elif(len(e_events)!=0):
        print('     event  time :',min(e_events))
        popper = e_events.index(min(e_events))
        pop_to_heaven(popper)

        
        print_call_rec()
        print_line()
        print_running_calls(incall)
        print_busy_que()
        
        if(len(busy)!=0):
                for i in range(len(busy)):
                    f=busy[i][0]
                    t=busy[i][1]
                    if(links[1][f-1]==0 and links[1][t-1]==0):
                        try_busy(busy[i])
    else:
        print('sim comp')
        break
        
#print_call_rec()
#print_busy_que(no_busy)
#print(busy)
#print_line()
#print(counter)
