from collections import Counter
from core.config import DATA_DIR_PATH
import json
from app.services.data_service import fetch_alive_ads


def save_live_ads_as_json():
    counter = Counter(fetch_alive_ads())
    file_path = DATA_DIR_PATH.joinpath("alive_ads.json")
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(counter, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    save_live_ads_as_json()