import aiofiles
import csv
import time

async def convert_data(data):
    for row in data:
        matches_list = [item for item in eval(row['matches'])]
        rules_list = [item['rule'] for item in eval(row['rules'])]
        row['matches'] = ', '.join(matches_list)
        row['rules'] = ' '.join(rules_list)
    return data

async def save_to_csv(data, filename_prefix="batch"):
    print("Saving to CSV")
    filename = f"./batch_run/{filename_prefix}_{int(time.time())}.csv"
    async with aiofiles.open(filename, mode='w') as file:
        writer = csv.writer(file)
        await writer.writerow(['input', 'chat_type', 'match_count', 'matches', 'rules'])

        for row in data:
            await writer.writerow([row['input'], row['chat_type'], row['match_count'], row['matches'], row['rules']])

    return {
        "message": "Batch processing completed successfully",
        "processed_count": len(data)
    }
