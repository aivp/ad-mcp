import requests

def parse_forklift_error(error_code: str) -> dict:
    """
    解析叉车故障码,返回故障描述和建议解决方案
    Args:
        errorcode: 故障码字符串
    """
    url = "http://huoshan-mcp-data:8000/errorcode"
    data = {"error_code": error_code}
    resp = requests.post(url, json=data)
    return resp.json()