import json

# =========================
# FOLLOWERS (pakai value)
# =========================
def get_followers(file):
    data = json.load(open(file, encoding="utf-8"))
    result = set()

    for item in data:
        try:
            user = item['string_list_data'][0]
            username = user.get('value')

            if username:
                result.add(username.strip().lower())

        except:
            pass

    return result


# =========================
# FOLLOWING (pakai title)
# =========================
def get_following(file):
    data = json.load(open(file, encoding="utf-8"))
    result = set()

    data = data.get('relationships_following', [])

    for item in data:
        try:
            title = item.get('title')

            if title:
                result.add(title.strip().lower())

        except:
            pass

    return result


# =========================
# LOAD DATA
# =========================
followers = get_followers('followers_1.json')
following = get_following('following.json')


# =========================
# LOGIC INTI
# =========================
not_follow_back = following - followers   # dia tidak follow kamu balik
mutual = following & followers            # saling follow


# =========================
# OUTPUT
# =========================
print("\n===================================")
print("📊 INSTAGRAM FOLLOW CHECK")
print("===================================\n")

print(f"👥 Followers kamu : {len(followers)}")
print(f"👥 Kamu follow    : {len(following)}")

print(f"\n❌ Tidak follow balik ({len(not_follow_back)}):\n")

if not_follow_back:
    for i, u in enumerate(sorted(not_follow_back), 1):
        print(f"{i}. {u}")
else:
    print("Semua follow balik 🎉")

print("\n===================================")