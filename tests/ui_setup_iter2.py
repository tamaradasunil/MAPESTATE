# Setup TEST_ owner+buyer and a pending listing for iteration-2 UI tests
import os, uuid, json, requests
API = os.environ["EXPO_PUBLIC_BACKEND_URL"].rstrip("/") + "/api"
out = {}
for role, name in (("owner", "TEST_UIOwner"), ("buyer", "TEST_UIBuyer")):
    em = f"test_ui{uuid.uuid4().hex[:6]}@example.com"
    d = requests.post(f"{API}/auth/signup", json={"email": em, "password": "test1234", "name": name, "role": role, "phone": "+919876543210"}).json()
    out[role] = {"email": em, "token": d["session_token"], "uid": d["user"]["user_id"]}
h = {"Authorization": f"Bearer {out['owner']['token']}"}
p = requests.post(f"{API}/properties", headers=h, json={"title": "TEST_UI Lakeview Flat Qwz", "listing_type": "buy", "category": "apartment", "price": 6100000,
    "address": "TEST road", "city": "Hyderabad", "locality": "Madhapur", "lat": 17.448, "lng": 78.391, "bedrooms": 2}).json()
out["pid"] = p["id"]; print(p["status"])
open("/tmp/iter2_emails.txt", "a").write(out["owner"]["email"] + "\n" + out["buyer"]["email"] + "\n")
json.dump(out, open("/tmp/ui_iter2.json", "w"))
print(json.dumps({k: (v if k == "pid" else v["email"]) for k, v in out.items()}))
