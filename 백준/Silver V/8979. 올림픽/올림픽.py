def medal_country(countrys, m, n):
    result = dict()
    for i in range(1, n+1):
        result[i] = 0
    medals = [tuple(i[1:]) for i in countrys]
    medals = set(medals)
    medals = list(medals)
    sorted_country = sorted(medals, key = lambda x: (x[0], x[1], x[2]), reverse=True)
    
    
    for i in range(len(countrys)):
        for j in range(len(sorted_country)):
            if tuple(countrys[i][1:]) == sorted_country[j]:
                result[countrys[i][0]] = j+1
    return result[m]


def main():
    n, m  = map(int, input().split())
    country = [list(map(int, input().split())) for _ in range(n)]
    result = medal_country(country, m, n)
    return result
        
if __name__ == "__main__":
    print(main())
    