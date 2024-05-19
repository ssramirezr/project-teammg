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
                    if i == len(production) - 1:
                        first_sets[symbol] = first_sets[symbol].union(first_sets[production[i]])
                    else:
                        #epsilon rule: if all the first of the non-terminals in the production have e,
                        #then First(current symbol) also does
                        if "e" in first_sets[production[i]]:
                            first_sets[symbol] = unionExcludingEpsilon(first_sets[symbol], first_sets[production[i]])
                        else:
                            first_sets[symbol] = first_sets[symbol].union(first_sets[production[i]])
                    if "e" not in first_sets[production[i]]:
                        break
                else:
                    first_sets[symbol].add(production[i])
                    break

    for non_terminal in G:
        computeFirst(non_terminal)

    return first_sets

def unionExcludingEpsilon(set1, set2):
    set1 = set1.union(set2)
    try:
        set1.discard("e")
    except:
        return set1
    return set1

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