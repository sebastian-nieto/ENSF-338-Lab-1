import json
import timeit
import matplotlib.pyplot as plt

def processlargefile():
    
    with open("Lab 1\\large-file.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
    

    size = 1000
    data2 = data[:size]

    timings = timeit.repeat(lambda: modify_size(data2), repeat=1000, number=1)

    plt.hist(timings, bins=20, edgecolor='black')
    plt.xlabel('Time(s)')
    plt.ylabel('Frequency')
    plt.title(f'Distribution of Processing Time for 1000 Records')
    plt.grid(True)
    plt.savefig('output.3.3.png')
    plt.show()

    with open("Lab 1\\output.2.3.json", 'w', encoding='utf-8') as file:
        json.dump(data[::-1], file)

def modify_size(data2):
    for record in data2:
        record['size'] = 42

if __name__ == "__main__":
    processlargefile()
