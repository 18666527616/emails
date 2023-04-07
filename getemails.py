python
Copy code
import asyncio
import aiohttp

async def fetch_emails(session, url):
    async with session.get(url) as response:
        data = await response.json()
        emails = [item['email'] for item in data]
        return emails

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, 101):
            url = 'https://jsonplaceholder.typicode.com/posts'+'/'+str(i)+'/'+'comments'
            tasks.append(asyncio.create_task(fetch_emails(session, url)))

        results = await asyncio.gather(*tasks)

    with open('emails.txt', 'w') as f:
        for emails in results:
            f.write('\n'.join(emails) + '\n')

if __name__ == '__main__':
    start_time = time.monotonic()
    asyncio.run(main())
    end_time = time.monotonic()
    print(f"Time used: {end_time - start_time} seconds.")
