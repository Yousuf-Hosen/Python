class Airport:
    def __init__(self,code,name,country,latitude,longitude,rate) -> None:
        self.code=code
        self.name=name
        self.country=country
        self.latitude=latitude
        self.longitude=longitude
        self.rate=rate
    

    def __repr__(self) -> str:
        return f"Airport {self.name} in {self.country} lat :{self.latitude} longi: {self.longitude} rate :{self.rate}"
    