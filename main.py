import os
import discord
import redis

# Initialize Redis connection
r = redis.Redis(
    host=os.getenv("HOST"),
    port=12003,
    decode_responses=True,
    username="default",
    password=os.getenv("REDID")
)

TARGET_USER_ID = int(os.getenv("TARGET"))

def main(args):
    cached_status = r.get("status")
    if cached_status:
        print("Using cached status:", cached_status)
        return {"status": cached_status}
    else:
        intents = discord.Intents.default()
        intents.message_content = True
        intents.presences = True
        intents.members = True

        result = {"status": "offline"}
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            nonlocal result
            for guild in client.guilds:
                member = guild.get_member(TARGET_USER_ID)
                if member and member.status != discord.Status.offline:
                    result["status"] = member.status.value
                    break
            await client.close()

        client.run(os.getenv("BOB"))
        r.set("status", result["status"], ex=500)  # Cache for 5 minutes
        print("Fetched status:", result["status"])
        return result
