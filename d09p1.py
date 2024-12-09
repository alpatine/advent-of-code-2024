from itertools import batched


class File:
    def __init__(self, id: int, length: int, space: int):
        self.id = id
        self.length = length
        self.space = space
    
    def __repr__(self):
        return f"({self.id},{self.length},{self.space})"

def readDataFile() -> str:
    with open('d09data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[File]:
    files = []
    for id, pair in enumerate(batched(data, 2)):
        file_length = int(pair[0])
        if len(pair) == 2: space_lengh = int(pair[1])
        else: space_lengh = 0
        files.append(File(id, file_length, space_lengh))
    return files

def compress(files: list[File]) -> list[int]:
    blocks = []

    left_pos = 0
    right_pos = len(files) - 1

    while True:
        # fill left
        left_file = files[left_pos]
        if left_file.length == 0: break
        blocks += [left_file.id] * left_file.length
        left_file.length = 0
        left_pos += 1
        if left_pos > right_pos: break

        # fill right
        while left_file.space > 0 :
            right_file = files[right_pos]
            can_fill = min(left_file.space, right_file.length)
            blocks += [right_file.id] * can_fill
            left_file.space -= can_fill
            right_file.length -= can_fill
            if right_file.length == 0: right_pos -= 1
    
    return blocks

def calculate_checksum(files: list[int]) -> int:
    total = 0
    for pos, num in enumerate(files):
        total += pos * num
    return total

def d09p1(data: str) -> int:
    files = parseData(data)
    compressed_files = compress(files)
    checksum = calculate_checksum(compressed_files)
    return checksum
    
if __name__ == '__main__':
    data = readDataFile()
    result = d09p1(data)
    print(result)
