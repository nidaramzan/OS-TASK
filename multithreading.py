import multiprocessing, threading, time

sem1 = threading.Semaphore()
sem2 = threading.Semaphore()
sem3 = threading.Semaphore()
sem4 = threading.Semaphore()
sem5 = threading.Semaphore()


waiting_chairs = int(input("\n \t Enter the number of available chairs in shop: ")) 
operated_chairs = int(input("\t Enter number of chair under operation by barber: ")) 
status = input("\t Please enter status of barber's chair: \n \t TRUE/true \n \t FALSE/false \t")   # it will be false if it is not occupied  


print("\nChairs in the shop: ",waiting_chairs)  
print("Operated Chairs in the shop: ",operated_chairs)  
print("Barber's status: ",status) 


b_sleep=0                                                   #0 means barber is awake 

def Customer():
                                                            #global waiting_chairs
                                                            #global status
    global operated_chairs

    while waiting_chairs>=operated_chairs:                  #operated_chairs<=waiting_chairs:


        if (status==True and operated_chairs==waiting_chairs):
                                                            #time.sleep(5)
            sem3.release()                                    #Semsignal(sem3)
                                                            #print("semaphore sem3",sem3)
            print("%s tries to release lock"%(threading.current_thread().name))
            print("Third semaphore's value is: ",sem3._value)
            balk()
            sem4.release()
            print("%s tries to release lock"%(threading.current_thread().name))
           
            print("Fourth semaphore's value is: ",sem4._value)
            break
        elif (status==True and operated_chairs < waiting_chairs):
            operated_chairs+=1
            #time.sleep(5)
            sem2.release()
            print("%s tries to release lock"%(threading.current_thread().name))
            print("second semaphore's value: ",sem2._value)
            time.sleep(5)
            print("Chairs used",operated_chairs)
        else:
                                                            #time.sleep(7)
                                                            #print("releasing semaphore sem1")
            sem1.release()                                  #Semsignal(sem1) +1
                                                            #print("semaphore sem1",sem1)
            print("%s tries to release lock"%(threading.current_thread().name))
            print("First semaphore's value: ",sem1._value)
            getHaircut()
            break

def barber():
    if(status==False and operated_chairs==0):
        b_sleep=1
        print("barber has gone to sleep")
    elif(status==True):
        pass
    elif(operated_chairs!=0 and status==False):
        b_sleep=0
        cutHair()


def getHaircut():
                                            #global waiting_chairs
    global operated_chairs                  #operated_chair is globally declare over here
    global status                           #global variable
                                            #print("tries to aquire semaphore")
    sem1.acquire()                          #semWait(sem1) -1
    print("%s tries to release lock"%(threading.current_thread().name))
    print("semaphore sem1 value: ",sem1._value)
    status=True
    if(status==True and operated_chairs==0):
        pass
    else:
        print("The status of Barber's chair :",status)
                                                #sem2.release()
                                                #time.sleep(1)
                                                #print("%s tries to release"%(threading.current_thread().name))
                                                #print("semaphore sem2 value: ",sem2._value)
    sem4.acquire()
    sem2.acquire()
    if(operated_chairs==0):
        pass
    else:
                                                #status=False
                                                #time.sleep(1)
                                                #print("%s tries to release lock"%(threading.current_thread().name))
                                                #print("fifth semaphore value: ",sem5._value)
        operated_chairs=operated_chairs-1
    print("%s tries to release lock"%(threading.current_thread().name))
    print("Fourth semaphore value: ",sem4._value)
    print("Third semaphore value: ",sem2._value)
    print("Chairs used: ",operated_chairs)
    Customer()



def balk():
    sem3.acquire()                  
                                                        #print("semaphore sem3:",sem3)
    print("\n ")
    print("%s tries to release lock \t"%(threading.current_thread().name))
    print("Third semaphore value: ",sem3._value)
    if(operated_chairs==waiting_chairs):
       time.sleep(2)
       print("The customer which is unattended has left the shop")
    elif(operated_chairs==0):
        pass

def cutHair():
    global status
                                                    #print("tries to acquie semaphore sem2")
                                                    #sem2.acquire()             #semWait(sem2)
                                                    #print("semaphore sem2 has a value",sem2)
                                                    #print("%s tries to release lock"%(threading.current_thread().name))
                                                    #print("semaphore sem2 value: ",sem2._value)
    if(status==False):
       print("The chair of Barber is empty at the moment ")
   
    elif(status==True):
       print("The chair of Barber is occupied at the moment")

def main():
                                                        # start=time.clock()
                                                        #p1=multiprocessing.Process(target=Customer)
                                                        #p2=multiprocessing.Process(target=cutHair)

                                                        #p1.start()
                                                        #p2.start()
                                                        #p1.join()
                                                        #p2.join()

    thread1 = threading.Thread(target = Customer)       #call to customer function
    thread2 = threading.Thread(target = getHaircut)         #call to getHaircut
    thread3 = threading.Thread(target = cutHair)            #call to cutHair
    thread4 = threading.Thread(target = barber)             #call to barber
    thread5 = threading.Thread(target = balk)               #call to balk

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    print("\n \t@@@DONE WITH ALL THE THREADS@@@")


                                                    # finish=time.clock()
                                                    # end_d=finish-start
                                                    # print("time = ",x)
                                                    #print(f'Finished in{round(finish-start,2)}seconds')
main()                                           #calling our main function
