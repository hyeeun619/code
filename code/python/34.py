#날짜별 전력사용량
electricity_usage = [
    {"date" : "2024-11-01", "usage": 12.5},
    {"date" : "2024-11-02", "usage": 15.3},
    {"date" : "2024-11-03", "usage": 10.8},
    {"date" : "2024-11-04", "usage": 14.2},
    {"date" : "2024-11-05", "usage": 13.6},
]
from abc import ABC, abstractmethod

# 부모(추상클래스)
class ElectricityDate(ABC):
    def __init__(self, usage_date):
        self._usage_date = usage_date
        self._total_usage = 0

    # 총 사용량 계산
    def calculate_total_date(self):
        self._total_usage = sum(item['usage']for item in self._usage_date)
        return self._usage_date 
        
    # 특정 날짜의 전력 사용량 반환
    def get_usage_on_date(self, date):
        for item in self.get_usage_on_date :



    # 일반 메서드
    #  새로운 날짜의 전력 사용량 추가
    def add_usage(self, date, usage):
    # 특정 날짜의 전력 사용량 데이터를 삭제
    def remove_usage(self, date):


# 자식클래스
class HomeDletricityDate(ElectricityDate):