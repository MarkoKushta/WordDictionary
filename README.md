# WordDictionary
->PROBLEM DESCRIPTION

Given a dictionary D and a non-empty string s where words are joined together, 
create an algorithm which returns the properly tokenized text, 
s’ with spaces inserted between individual words.


->APPROACH

To solve this problem, we have used Python Language because it a very fast language for operating with data and sets. The approach of this code is to find a fast and efficient solution for our enterprise.
All Python’s immutable built-in objects are hashable, so in comparison with java or other languages we need to implement only dictionaries and the logic of recursions. We will read the lines of a text file provided by the professor and will show the output in the VS code terminal. 


->ALGORITHM

1. Create a lines array, read input from file, and put it inside the array
2. Create a dictionary and a counter which starts at 0
3. For all lines in lines array, we check the counter and at the end give the key value 1 to the dictionary when the current line has no spaces
4. If counter is 0, length is equal the to the converted decimal value of the current line, counter increments
5. If counter is 1 then corrupt is equal to the current line without spaces, counter increments
6. Call recursive function starting from 0, with the space char
7. Create recursive function
8. Check if current index is equal to the length of corrupt sentence if yes print all possible combinations
9. Initialize temp as a space char
10. Loop i from index to length of the corrupt sentence
11. Replace temp with current corrupt words
12. Add temp to dictionary
13. Call the function recursively, however this time the index starts from i+1, and we add the current word, to our temp and a space character 


->OUTPUT
![output](https://user-images.githubusercontent.com/71281629/173920042-bf3bf83f-fcee-4588-9200-b50d37874897.png)

