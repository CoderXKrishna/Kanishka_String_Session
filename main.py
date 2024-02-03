import asyncio
from KanishkaString import anony_boot  # Assuming 'anony_boot' is defined in KanishkaString module

async def main():
    await anony_boot()

if __name__ == "__main__":
    # Create and run the event loop
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
