import json, httpx, asyncio

BASE = "http://localhost:8000"

async def main():
    async with httpx.AsyncClient() as client:
        print("Start session...")
        r = await client.post(f"{BASE}/v1/sessions", json={"user_id":"u_1","locale":"he-IL"})
        print(r.json())

        print("Recommendation...")
        r = await client.post(f"{BASE}/v1/recommendations", json={"user_id":"u_1","subject":"math"})
        rec = r.json()
        print(json.dumps(rec, indent=2))

        if rec.get("items"):
            first = rec["items"][0]
            print("Submit answer...")
            r = await client.post(f"{BASE}/v1/submit", json={
                "user_id": "u_1",
                "subject": "math",
                "item_id": first["item_id"],
                "student_answer": "x=3"
            })
            print(r.json())

        print("Profile...")
        r = await client.get(f"{BASE}/v1/profiles/u_1")
        print(json.dumps(r.json(), indent=2))

if __name__ == "__main__":
    asyncio.run(main())