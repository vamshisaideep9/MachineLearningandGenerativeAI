from pydantic import BaseModel, Field, field_validator, ValidationError


class Device(BaseModel):
    mac_address: str 
    is_active: bool 


class NetworkConfig(BaseModel):
    ip_address: str 
    port: int
    devices: list[Device] = Field(default_factory=list)


    @field_validator("port")
    @classmethod 
    def port_validation(cls, p:int) -> int:
        if p >= 1024 and p <= 65535:
            return p
        else: 
            raise ValueError("Port Value should be in between 1024 and 65535")
        



try:
    payload = {
        "ip_address": "192.168.1.1",
        "port": "1024",
        "devices": [{
            "mac_address": "00:1A:2B:3C:4D",
            "is_active": "true"
        }]
    }


    network = NetworkConfig(**payload)
    print(network.model_dump())
except ValidationError as e:
    print(e.json())
    

