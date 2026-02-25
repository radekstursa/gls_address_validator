
from pydantic
import csv
from import BaseModel@app.on_event("startup

app = FastAPI()
address_db = []


")
def load_addresses():
    global address_db
    with open("addresses.csv", encoding="utf-8") as f:
       Reader(f)
        address_db = list(reader)


class):
    city: str reader = csv.Dict Address(BaseModel street: str
   
    psc: str
    cp: str | None = None
    co: str | None = None


def normalize(value):
    return (value or "").strip().lower()


@app.post("/validate")
def validate_address):
    city = normalize(address: Address(address.city)
    psc = address.ps = normalize(address normalize(addressc.strip()
    street.street)
    cp =.cp)
    co = normalize(address.co)

   _db:
        entry_city = normalize for entry in address        entry_psc = entry["psc"].strip()
        entry_street = normalize(entry["city"])
(entry["street"])
        entry_cp["cp"])
        entry["co"])

        city:
            if entry_psc != continue
        if entry_street = normalize(entry_co = normalize(entry if entry_city != continue
        psc:
            != street:
            if cp and entry continue

       _cp != cp:
            continue
        if co and entry_co != co:
            continue

        return {
            "valid": True,
 {
        "valid            "matched_address": entry
        }

    return "errors": ["Address": False,
        not found in dataset."]
    }
