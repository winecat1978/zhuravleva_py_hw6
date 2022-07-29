# Самая далекая планета
orbits = [(1,3),(2.5,10),(7,2),(6,6),(4,3)]
def find_farthest_orbit(orbits):
    s_max = orbits[0][0]*orbits[0][1]
    i_max = orbits[0]
    i = 0
    while i < len(orbits):
        if orbits[i][0]*orbits[i][1] > s_max and orbits[i][0] != orbits[i][1]:
            s_max = orbits[i][0]*orbits[i][1]
            i_max = i
        i+=1
    return orbits[i_max]
print(*find_farthest_orbit(orbits))

