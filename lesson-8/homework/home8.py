'''try:
    a=int(input('son:'))
    b=int(input('son2:'))
    c=a/b
    print(c)
except ZeroDivisionError:
 print('siz 0 hato belgiladingiz')'''



'''try:
    number=input('son yozing:')
    n=int(number)
    print (f"you get the integer{n}")
except ValueError:
 print('hato belgiladingiz')'''



'''import os
filepath = '8nd\\new1.py'

if os.path.exists(filepath):
    print('topildi')
else:
    print('unday fayl yoq')'''



'''try:
    number=input('son yozing')
    n=input('ikkinchisini yozing')
    total=int(number)+n
    print(total)
except TypeError:
    print('type hato')'''





'''try:
  with open('lesson1\\neww.txt','r') as file:
    data=file.read()
    print(data)
except PermissionError:
 print('hatolik')'''


'''
try:
    my_list = [10, 20, 30]
    print(my_list[5])
except IndexError:
    print( "IndexError: индекс выходит за пределы списка")



try:
    number = input("Son kiriting (Ctrl+C bosmang): ")
    print("Siz kiritgan son:", number)
except KeyboardInterrupt:
    print("\n KeyboardInterrupt: kiritish bekor qilindi foydalanuvchi tomonidan")



try:
    a = 10
    b = 0
    result = a / b
    print(result)
except ArithmeticError:
    print(" ArithmeticError: arifmetik xatolik yuz berdi")



try:
    with open("encoded_file.txt", "r", encoding="ascii") as f:
        content = f.read()
        print(content)
except UnicodeDecodeError:
    print(" UnicodeDecodeError: faylni kodlashda xatolik yuz berdi")


try:
    my_list = [1, 2, 3]
    my_list.upper()
except AttributeError:
    print(" AttributeError: bu obyektda bunday metod yo'q")

'''



'''with open("encoded_file.txt", "r") as f:
        content = f.read()
        print(content)'''




'''with open(filename, 'r', encoding='utf-8') as file:
        for i in range(n):
            line = file.readline()
            if line == '':
                break
            print(line.strip())'''



'''with open('lesson1\\neww.txt','a') as file:
    data=file.write('aaaa')
    print(data)

with open('lesson1\\neww.txt','r') as file:
    data=file.read()
    print(data)'''



'''def read_last_n_lines(filename, n):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            last_lines = lines[-n:]
            for line in last_lines:
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")'''




'''def read_file_to_list(filename):
    lines_list = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                lines_list.append(line.rstrip('\n'))  # remove trailing newline
        return lines_list
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return []'''




import os
import random
import string

# 1. Find longest words
def find_longest_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        words = f.read().split()
        max_len = max(len(word) for word in words)
        return [word for word in words if len(word) == max_len]

# 2. Count number of lines
def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

# 3. Word frequency
def word_frequency(filename):
    freq = {}
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().replace(',', ' ')
        for word in text.split():
            word = word.lower()
            freq[word] = freq.get(word, 0) + 1
    return freq

# 4. File size
def file_size(filename):
    return os.path.getsize(filename)

# 5. Write list to file
def write_list_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(f"{item}\n")

# 6. Copy file
def copy_file(src, dest):
    with open(src, 'r', encoding='utf-8') as f_src, open(dest, 'w', encoding='utf-8') as f_dest:
        for line in f_src:
            f_dest.write(line)

# 7. Combine lines from two files
def combine_lines(file1, file2, output):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2, open(output, 'w', encoding='utf-8') as out:
        for line1, line2 in zip(f1, f2):
            out.write(line1.strip() + " " + line2)

# 8. Read a random line
def random_line(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return random.choice(lines).strip()

# 9. Check if file is closed
def is_file_closed(filename):
    f = open(filename, 'r', encoding='utf-8')
    print(f.closed)
    f.close()
    print(f.closed)

# 10. Remove newline characters
def remove_newlines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read().replace('\n', '')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# 11. Count words in file
def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().replace(',', ' ')
        return len(text.split())

# 19. Extract characters into list
def extract_characters(filenames):
    chars = []
    for file in filenames:
        with open(file, 'r', encoding='utf-8') as f:
            chars.extend(list(f.read()))
    return chars

# 20. Generate 26 files A.txt to Z.txt
def generate_alphabet_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w', encoding='utf-8') as f:
            f.write(f"This is file {letter}.txt")

# 21. Write alphabet with specified letters per line
def write_alphabet_lines(filename, per_line):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(0, 26, per_line):
            f.write(' '.join(string.ascii_uppercase[i:i+per_line]) + '\n')
