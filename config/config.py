import os
class Config:
    BASE_URL=os.getenv("BASE_URL","https://example.com")
    TIMEOUT=int(os.getenv("TIMEOUT", 10))




