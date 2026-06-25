#Loop-> logic repeatition 
#for loop for <condition>: iteration i =3,6
#                       <command> x 3 | x 6
# for i in range(5):# range 0-4   [ 0<i<5= 1 2 3 4 ]
# # for -> keyword i-> variable in-> keyword  range
#     print(i) # print(i)-> 0 1 2 3 4  
# for j in range(11,17): # 11<=j <17
#     # j -> 11 ... 17
#     print(j)
# for k in range(0,11,2):# 0-10 # step size
#     print(k) # 0+2 (1),2+2 (2), 4+2 ()
#     # 0 2 4  6 8 10
# for(int i=0;i<4;i++){ #i<4 i 0 1 2 3 we work range of values int i=4 ,i <1000
#     cout <<i<<endl;
# }
# for i in range(5) i==5 -> loop terminate
# int i=0 ; i<5 ; i++==i+1
#while loop 
count=1 # int # 1 2 3 4 5
while count<=5:# while condition count <=5:  # True / false condition
    #while True: # while False-> loop body will not execute
    # count <=5  1 <= 5 -> 1 is less than or equal 5->T 7<=5->False
    print(count) 
    # base condition -> stop condition it helps to terminate a loop
    count+=1 # logic count +=1 count=count+1 count*=1-> conut =conut*1

# iteration 1 coount =1 1<=5 T -> print(1) -> count=1+1 // 2
# iteration 2 count =2 2<=5 T ->print(2)-> count=2+1 //3
#.
#.
#iteration n count =5 5<=5 T ->.... count=5+1=6
# iteration last count =6 6<=5->F -> X
#           Nested Loops
# for i in range(3): # for -> range 0 1 2-> i=0 and i <3 
#     # iteration 2 : i+=1 i=1 i<3 T
#     # iteration 3 : i+1= 2 T
#     # iteration 4 :i+1=3 i<3 F
#     for j in range(3): # j=0 j<3-> T | j=j+1 j=1 j<3| j=2 2<3 | j=3 j<3 ( F)
#         print(i,j) # i =0 j=0 # i=0 j=1 # i=0 j=2
#                     # i=1 j=0 #i=1 j=1 # i=1 j=2
#                     # i=2 j=0 # i=2 j=2 # i=2 j=1
# #--Pattern Printing
for i in range(5):# i=0 i<5
    for j in range(i+1): # range( i + 1) # j=0 range(1) j<1
        print("*",end="") # *  end =""-> space
    print()# nextline 

# Break Statement -> Stop 
for i in range(5): #I=0 I<5 i=1  i=2 i=3
    if i==3: # if 0==3 ->F 3==3:
        break
    print(i) # 0 1 2
# Continue
for i in range(5):
    if i==3:
        continue # i value skip -> excetion would continue
    print(i) # 0 1 2 4
# pass -> placeholder
print("pass") 
for i in range(5):
    if i==3:
        pass # continue | break
    print(i) #0 1 2 3 4
# Do while
# #  
# do{
#     cout <<"name"<<endl;
# }
# # name
# # name
# # name
# # name

# while(i<3){ # i=0 i< i=1  i =2
#     cout <<i<<endl; # 0 1 2 
#     i+=1;# i=3
# }