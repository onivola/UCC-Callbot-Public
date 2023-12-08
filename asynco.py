import asyncio
import aiohttp
import time
start_time = time.time()
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = "https://luis-ia.cognitiveservices.azure.com/luis/prediction/v3.0/apps/2a9f0849-04e1-4c3c-9659-490d07d52ed8/slots/staging/predict?verbose=true&show-all-intents=true&log=true&subscription-key=7b7090cc610049e58afa870ee86a4b1d&query=non"
    response = await fetch(url)
    print(response)

if __name__ == "__main__":
    asyncio.run(main())

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time, "seconds")