if __name__ == '__main__':
    n = int(input())
    results = []
    scoreList = []
    for i in range(n):
        name = input()
        score = float(input())
        results.append([name, score])
        scoreList.append(score)
        i = i+1
        
    scoreList = sorted(set(scoreList))
    m = scoreList[1]
    nameList = []
    for val in results:
        if m == val[1]:
            nameList.append(val[0])
    nameList.sort()
    for nm in nameList:
        print(nm)
