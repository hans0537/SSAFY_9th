class PublicTransport:
    totPas = 0
    passenger = 0
    profit = 0

    def __init__(self, name, fare):
        self.name = name
        self.fare = fare

    def get_in(self):
        PublicTransport.passenger += 1
        PublicTransport.totPas += 1
        # 요금이 다를수 있으니 객체 생성후 탑승하면 요금 추가
        PublicTransport.profit += self.fare
        
    def get_off(self):
        PublicTransport.passenger -= 1

    @classmethod
    def get_profit(cls):
        return cls.profit

class Bus(PublicTransport):

    def __init__(self, limit):
        self.limit = limit

    def get_in(self, p):
        print(f"정원: {self.limit} | 현재 인원: {PublicTransport.passenger}")
        if self.limit == PublicTransport.passenger:
            print("더이상 탑승할 수 없습니다")
            return

        PublicTransport.profit += p.fare
        PublicTransport.passenger += 1
        PublicTransport.totPas += 1
        
p1 = PublicTransport("a", 1250)
p2 = PublicTransport("b", 1250)
p3 = PublicTransport("c", 1000)
p4 = PublicTransport("d", 1450)
p5 = PublicTransport("e", 900)
p6 = PublicTransport("f", 900)
p7 = PublicTransport("g", 900)

bus1 = Bus(5)
bus1.get_in(p1)
bus1.get_in(p2)
bus1.get_in(p3)
bus1.get_in(p4)
bus1.get_in(p5)
bus1.get_in(p6)
bus1.get_in(p7)

print(PublicTransport.get_profit())
print(PublicTransport.passenger)
print(PublicTransport.totPas)