import requests
    
def forklift_accessory_recommendation(description: str) -> dict:
    """获取叉车配件推荐"""
    url = "http://huoshan-mcp-data:8000/recommendation"
    data = {"description": description}
    resp = requests.post(url, json=data)
    return resp.json()