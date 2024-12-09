from itertools import batched
from operator import attrgetter


class File:
    def __init__(self, id: int, start: int, length: int, space: int):
        self.id = id
        self.start = start
        self.length = length
        self.space = space
        self.space_used = 0
    
    def __repr__(self):
        return f"({self.id},{self.start},{self.length},{self.space},{self.space_used})"

def readDataFile() -> str:
    with open('d09data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[File]:
    used_space = 0
    files = []
    for id, pair in enumerate(batched(data, 2)):
        file_length = int(pair[0])
        if len(pair) == 2: space_lengh = int(pair[1])
        else: space_lengh = 0
        files.append(File(id, used_space, file_length, space_lengh))
        used_space += file_length + space_lengh
    return files

def compress(files: list[File]) -> list[File]:
    right_pos = len(files) - 1
    left_pos = 0

    while right_pos > left_pos:
        right_file = files[right_pos]
        for search_pos in range(left_pos, right_pos):
            search_file = files[search_pos]
            if search_file.space - search_file.space_used >= right_file.length:
                right_file.start = search_file.start + search_file.length + search_file.space_used
                search_file.space_used += right_file.length
                break
        right_pos -= 1
    return files        

def calculate_checksum(files: list[File]) -> int:
    total = 0
    for file in sorted(files, key=attrgetter('start')):
        for i in range(file.start, file.start + file.length):
            total += i * file.id
    return total

def d09p2(data: str) -> int:
    files = parseData(data)
    compressed_files = compress(files)
    checksum = calculate_checksum(compressed_files)
    return checksum
    
if __name__ == '__main__':
    data = readDataFile()
    result = d09p2(data)
    print(result)
