def solve(num_heads, num_legs):
    chickens = int((4*num_heads - num_legs) / 2)
    rabbits = int((num_legs - 2*num_heads) / 2)
    print(chickens / rabbits)
solve()