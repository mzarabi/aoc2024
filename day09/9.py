with open("day09/input.txt", "r") as file:
    input = file.read().split()

def parse_input(diskMap):
    return [int(size) for size in diskMap]

def solution1(diskMap):
    blocks = parse_input(diskMap)
    currentFileId = 0
    currentFreeSpaceId = len(blocks) // 2
    currentPosition = 0
    checksum = 0
    processingFreeSpace = False

    while blocks:
        blockSize = blocks.pop(0)
        if processingFreeSpace:
            for _ in range(blockSize):
                checksum += currentPosition * currentFreeSpaceId
                currentPosition += 1
                blocks[-1] -= 1
                if blocks[-1] == 0:
                    blocks = blocks[:-2]
                    currentFreeSpaceId -= 1
        else:
            for _ in range(blockSize):
                checksum += currentPosition * currentFileId
                currentPosition += 1
            currentFileId += 1
        processingFreeSpace = not processingFreeSpace

    return checksum

def solution2(diskMap):
    diskLayout = []
    for index, value in enumerate(diskMap):
        fileId = None if index % 2 else index // 2
        blockSize = int(value)
        if blockSize > 0:
            diskLayout.append([fileId, blockSize])

    currentIndex = 0
    while currentIndex < len(diskLayout):
        currentIndex += 1
        fileId, blockSize = diskLayout[-currentIndex]
        if fileId is None:
            continue

        for freeIndex in range(len(diskLayout) - currentIndex):
            freeFileId, freeBlockSize = diskLayout[freeIndex]
            if freeFileId is None and freeBlockSize >= blockSize:
                if freeBlockSize == blockSize:
                    diskLayout[freeIndex][0] = fileId
                else:
                    diskLayout[freeIndex][1] -= blockSize
                    diskLayout.insert(freeIndex, [fileId, blockSize])
                diskLayout[-currentIndex][0] = None
                break

    checksum = position = 0
    for fileId, blockSize in diskLayout:
        if fileId is not None:
            checksum += fileId * blockSize * (position + ((blockSize - 1) / 2))
        position += blockSize

    return int(checksum)

print(solution1(input))
print(solution2(input))