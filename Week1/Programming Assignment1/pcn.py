from itertools import chain
from itertools import islice

def parse(filePath):
    with open(filePath, "rb") as f:
        try:
            lines = iter(f)
            numVars = int(next(lines))
            cubeCount = int(next(lines))
            cubes = [None]*cubeCount
             
            for i in range(cubeCount):
                line = next(lines)
                cubes[i] = tuple(islice(map(int, line.split()), 1, None))

            return (numVars, tuple(cubes))

        except Exception as error:
            raise AssertionError("Bad pcn file {}".format(filePath)) from error

def write(f, numVars, cubes):
    endl = "\n"

    f.write(str(max(max(map(abs, cube)) for cube in cubes)))
    f.write(endl)
    f.write(str(len(cubes)))
    f.write(endl)
    
    cubes = tuple(set(tuple(sorted(cube, key=abs)) for cube in cubes))

    for cube in cubes:
        f.write(' '.join(map(str, chain((len(cube),), cube))))
        f.write(endl)

    f.write(endl)
