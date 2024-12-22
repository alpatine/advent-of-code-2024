from collections import Counter


def readDataFile() -> str:
    with open('d22data.txt') as dataFile:
        return dataFile.read()

def parseData(data: str) -> list[list[int]]:
    return [int(num) for num in data.splitlines()]

def calculate_prices(start: int, steps: int) -> list[tuple[int, int, int, tuple[int, int, int, int]]]:
    history: list[tuple[int, int, int, tuple[int, int, int, int]]] = [(start, start % 10, None, None)]
    n = start
    
    for step in range(steps):
        n = ((n * 64) ^ n) % 16777216
        n = ((n // 32) ^ n) % 16777216
        n = ((n * 2048) ^ n) % 16777216
        if step < 3: history.append((n, n % 10, n % 10 - history[-1][1], None))
        else:
            change = n % 10 - history[-1][1]
            seq = tuple([h[2] for h in history[-3:]] + [change])
            history.append((n, n % 10, change, seq))
        
    return history

def d22p2(data: str, steps: int) -> int:
    initial_numbers = parseData(data)

    sequence_counter = Counter()

    for num in initial_numbers:
        buyer_sequences = Counter()
        prices = calculate_prices(num, steps)
        for price in prices:
            seq = price[3]
            if seq is not None and seq not in buyer_sequences:
                buyer_sequences[seq] = price[1]
        sequence_counter.update(buyer_sequences)

    most_common_sequence = sequence_counter.most_common()[0]
    return most_common_sequence[1]

if __name__ == '__main__':
    data = readDataFile()
    result = d22p2(data, 2000)
    print(result)
