def cube_finder(n):
    cubes = {}
    for i in range(1,n+1):
        cubes[i] = i**3
    return cubes

num = int(input("enter the number as your wish to see the cubes of that numbers :"))
print(cube_finder(num))