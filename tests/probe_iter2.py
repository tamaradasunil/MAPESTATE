# Edge probes for iteration 2 (pending-listing leaks, re-approve duplicate notifications)
import os, uuid, requests
API = os.environ["EXPO_PUBLIC_BACKEND_URL"].rstrip("/") + "/api"
def su(role):
    em = f"test_pr{uuid.uuid4().hex[:6]}@example.com"
    d = requests.post(f"{API}/auth/signup", json={"email": em, "password": "test1234", "name": "TEST_Probe", "role": role}).json()
    open("/tmp/iter2_emails.txt", "a").write(em + "\n")
    return {"Authorization": f"Bearer {d['session_token']}"}
o, b = su("owner"), su("buyer")
a = {"Authorization": "Bearer " + requests.post(f"{API}/auth/login", json={"email": "admin@mapestate.in", "password": "Mapestate@Admin2026"}).json()["session_token"]}
p = requests.post(f"{API}/properties", headers=o, json={"title": "TEST_Probe", "listing_type": "rent", "category": "apartment", "price": 25000, "address": "x", "city": "Pune", "lat": 18.5, "lng": 73.8}).json()
pid = p["id"]
print("pending: chat by buyer", requests.post(f"{API}/conversations", headers=b, json={"property_id": pid}).status_code)
print("pending: favorite by buyer", requests.post(f"{API}/favorites/{pid}", headers=b).status_code)
print("pending: enquiry by buyer", requests.post(f"{API}/enquiries", headers=b, json={"property_id": pid, "message": "TEST hi"}).status_code)
print("pending: report by buyer", requests.post(f"{API}/reports", headers=b, json={"property_id": pid, "reason": "fake"}).status_code)
print("pending: guest similar", requests.get(f"{API}/properties/{pid}/similar").status_code)
print("favorites list returns pending prop to buyer:", pid in [x["id"] for x in requests.get(f"{API}/favorites", headers=b).json()])
requests.post(f"{API}/saved-searches", headers=b, json={"name": "TEST_pune", "listing_type": "rent", "q": "Pune"})
requests.post(f"{API}/admin/properties/{pid}/approve", headers=a)
requests.post(f"{API}/admin/properties/{pid}/approve", headers=a)
n = [x for x in requests.get(f"{API}/notifications", headers=b).json() if x["property_id"] == pid]
print("saved-search notifications after approving twice:", len(n))
on = [x for x in requests.get(f"{API}/notifications", headers=o).json() if x["type"] == "listing_approved"]
print("owner approved notifs:", len(on))
# paused listing approve by admin
requests.patch(f"{API}/properties/{pid}", headers=o, json={"status": "paused"})
r = requests.post(f"{API}/admin/properties/{pid}/approve", headers=a); print("admin approve paused ->", r.json().get("status"))
print("admin bad status", requests.get(f"{API}/admin/properties", params={"status": "foo"}, headers=a).status_code)
print("PATCH active listing price edit keeps status:", requests.patch(f"{API}/properties/{pid}", headers=o, json={"price": 1}).json()["status"])
print("message on bad conv", requests.post(f"{API}/conversations/conv_x/messages", headers=b, json={"text": "x"}).status_code)
print("whitespace-only message", requests.post(f"{API}/conversations/{requests.get(f'{API}/conversations', headers=b).json()[0]['id']}/messages", headers=b, json={"text": "   "}).status_code)
