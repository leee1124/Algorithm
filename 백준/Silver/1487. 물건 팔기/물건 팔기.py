n = int(input())

price = []
for i in range(n):
    income, outcome = map(int, input().split())
    price.append([income, outcome])

price.sort(key = lambda x:(x[0], x[1]))

totalRevenue = [0] * n

for i in range(n):#price[i][0]은 판매가격
    for j in range(i, n):#price[j][1]은 고객별 배달비
        margin = price[i][0] - price[j][1] #판매가격에서 고객별 배달비를 빼서 마진을 구함
        if margin > 0: #해당 판매 가격으로 판매시 마진이 남는 경우
            totalRevenue[i] += margin # 해당 판매 가격으로 얻을 수 있는 토탈 수익을 구함

result = [price[i][0] for i in range(n) if totalRevenue[i] == max(totalRevenue)] #마진을 최대로 남길 수 있는 판매가격을 저장

if sum(totalRevenue) == 0:
    print(0)
else:
    print(min(result)) #마진이 최대로 남는 판매가격이 다수인 경우, 낮은 판매가를 출력