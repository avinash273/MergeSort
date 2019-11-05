#Merge Code Begin
#Merging_algo function to divide the array into two halves
#Left to middle will be first half
#middle to right will be next half
import time
def merging_algo(input_array, left, middle, right):
    num1=middle-left+1
    num2=right-middle

    left_array=[0]*(num1)
    right_array=[0]*(num2)

    for i in range(0,num1):
        left_array[i]=input_array[left+i]

    for j in range(0,num2):
        right_array[j]=input_array[middle+1+j]

#initializing index of the array which get split
    i=0
    j=0
    k=left

    while i<num1 and j<num2:
        if left_array[i]<=right_array[j]:
            input_array[k]=left_array[i]
            i=i+1
        else:
            input_array[k]=right_array[j]
            j=j+1
        k=k+1

    while i<num1:
        input_array[k]=left_array[i]
        i=i+1
        k=k+1

    while j < num2:
        input_array[k] = right_array[j]
        j += 1
        k += 1

#This functions splits the array recrsively every time into two halves
def merge_sort_call(input_array,left,right):
    if left < right:
        #Dividing Index to get the middle point of the array
        middle = (left+(right-1))//2
        merge_sort_call(input_array, left, middle)
        merge_sort_call(input_array, middle+1, right)
        merging_algo(input_array, left, middle, right)
#At end of each call we are calling merging_algo to sort by splitting the subsets
#Merge Sort Program End



#Input Array to verify the merge sort working
#Accepting inputs from command line by user
#input array contains the user input
input_array = list()
print("\nMERGE SORT")
Array_Size = int(input("Enter the number of elements you want sort:"))
print ('Enter numbers in array by pressing ENTER key after each element')

n=0

for i in range(Array_Size):
    n = int(input("Number:"))
    input_array.append(int(n))
print ('Input Array Given: ',input_array)

#calculating the start time and end time of Merge sort
#calling Merge sort by passing input array and size
start_time=time.clock()
merge_sort_call(input_array,0,Array_Size-1)
end_time=time.clock()-start_time
#once Sort is completed capturing the end time

print("\nOutput Array After MergeSort")
for i in range(Array_Size):
    print("%d" %input_array[i]),

print("\nTime Taken to Merge Sort the Numbers is: %s" %end_time)
#Code Complete

