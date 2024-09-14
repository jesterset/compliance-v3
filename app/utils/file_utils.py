# app/utils/file_utils.py
import aiofiles
import csv
import time

async def save_to_csv(data, filename_prefix="batch"):
    filename = f"./batch_run/{filename_prefix}_{int(time.time())}.csv"
    async with aiofiles.open(filename, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['input', 'chat_type', 'match_count', 'matches', 'rules'])
        for row in data:
            await writer.writerow([row['input'], row['chat_type'], row['match_count'], row['matches'], row['rules']])