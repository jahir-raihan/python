def isValidSubsequence(array, sequence):
    # Write your code here.
    it = iter(array) #iterating through the main array list for checking

    try: #try block to encounter any error and determine result
        for i in sequence: # iterating through the suquence

            while next(it) != i: #checking if i is present in main array and checking if it's in order or not

                pass
        return True # if the iteration complete successfully then return true
    except:
        return False # if iteration error occurs then false


array = [5, 1, 22, 25, 6, -1, 8, 10]
sub = [1, 6, -1, 10]

print(isValidSubsequence(array, sub))