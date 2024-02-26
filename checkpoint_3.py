#Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
string_var= 'Ainara Bilbao'
number_var = 46
list_var = [1, 2, 3, 4, 5]
boolean_var = True


#Exercise 2:  Use an index to grab the first 3 letters in your string, store that in a variable. 

user = 'Ainara Bilbao'
nombre_apellido = user[0:3]

print(nombre_apellido)

#Exercise 3: Use an index to grab the first element from your list.

animals = 'Gato, Perro, Caballo, Burro'
first_element = animals[0]

print(first_element)

#Exercise 4: Create a new number variable that adds 10 to your original number.

number = 2
new_number = number + 10

print(new_number)

#Exercise 5: Use an index to get the last element in your list.

string_variable = 'Ainara Bilbao'
last_element = string_variable [-1]

print(last_element)

#Exercise 6: Use split to transform the following string into a list.
names = 'harry,alex,susie,jared,gail,conner'

list = names.split(',')

print(list)

#Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.
sentence = "hoy no para de llover"
first_word = sentence[:3]
upper_first_word = first_word.upper()
new_string = upper_first_word + sentence[3:]

#Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
sentence = "Me encanta el número"
number = 7

print(f"{sentence} {number}.")

#Exercise 9: Print “hello world”.
sentence = "hello world"

print(sentence)