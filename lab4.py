class TourPackage:
    def __init__(self, country="невідомо", duration=0, price=100, rating=0, agency_name="невідомо"):
        self.__country = country
        self.__duration = duration
        self.__price = price
        self.rating = rating
        self.agency_name = agency_name



    def get_country(self):
        return self.__country

    def get_duration(self):
        return self.__duration

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"Путівка в {self.__country}, Тривалість: {self.__duration} днів, Ціна: {self.__price} євро, Рейтинг: {self.rating} зірок, Агенство: {self.agency_name}"

    def __repr__(self):
        return f"TourPackage(country='{self.__country}', duration={self.__duration}, price={self.__price}, rating={self.rating}, agency_name='{self.agency_name}')"

    def __del__(self):
        print(f"Путівку в {self.__country} видалено")


if __name__ == "__main__":
    tour1 = TourPackage()
    tour2 = TourPackage("Греція", 7, 500, 5, "Укртурагент")
    tour3 = TourPackage("США", 14, 1200, 4, "Легкотур")

    print(tour1)
    print(tour2)
    print(tour3)

