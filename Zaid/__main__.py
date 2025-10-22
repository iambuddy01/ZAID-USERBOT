import asyncio
import importlib
from pyrogram import idle
from Zaid.helper import join
from Zaid.modules import ALL_MODULES
from Zaid import clients, app, ids, init_aiosession, close_aiosession


async def start_bot():
    await init_aiosession()  # ✅ Start aiohttp session

    await app.start()
    print("LOG: Found Bot token. Booting...")

    for all_module in ALL_MODULES:
        importlib.import_module("Zaid.modules" + all_module)
        print(f"Successfully Imported {all_module} 💥")

    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            print(f"Started {ex.first_name} 🔥")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")

    print("All clients started successfully ✅")
    await idle()
    await close_aiosession()  # ✅ Cleanly close when idle ends


if __name__ == "__main__":
    asyncio.run(start_bot())
