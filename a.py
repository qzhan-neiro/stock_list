import akshare as ak
import pandas as pd
import json

# 获取所有 A 股股票代码和简称
df = ak.stock_info_a_code_name()

print(df.head())
print(f"总共获取 {len(df)} 只股票")

# 转为 JSON 字符串（推荐）
json_str = df.to_json(orient="records", force_ascii=False, indent=2)

# 保存到文件
with open("all_a_stocks.json", "w", encoding="utf-8") as f:
    f.write(json_str)

print("已保存到 all_a_stocks.json")