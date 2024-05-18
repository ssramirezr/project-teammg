def computeFirstSets (G):
    first_sets = {}
    calculated = []

    def computeFirst (symbol):
        if symbol in calculated:
            return
        calculated.append(symbol)
        first_sets[symbol] = set()
        for production in G[symbol]:
            for i in range(len(production)):
                if production[i] in G:
                    computeFirst(production[i])
                    #BUG: It adds epsilon after finding the first set of the first symbol. It can only add epsilon
                    #     when all the symbols in the current production produce epsilon.
                    first_sets[symbol] = first_sets[symbol].union(first_sets[production[i]])
                    if "e" not in first_sets[production[i]]:
                        break
                else:
                    first_sets[symbol].add(production[i])
                    break

    for non_terminal in G:
        computeFirst(non_terminal)

    return first_sets

def printFirstSets (sets):
    for non_terminal in sets:
        print(f"First({non_terminal}) = {sets[non_terminal]}")

def main():
    cases = int(input())
    for _ in range(cases):
        m = int(input())
        G = {}
        j = 0
        while j < m:
            l = input()
            l = l.split()
            G[l[0]] = []
            for i in range(1, len(l)):
                G[l[0]].append(l[i])
            j += 1

    first_sets = computeFirstSets(G)
    printFirstSets(first_sets)

if __name__ == "__main__":
    main()