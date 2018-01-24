def linear(N):
    return [2 * n for n in N]

def quad(N):
    return max([min([m for m in N]) for n in N])
