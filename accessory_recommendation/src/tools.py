import random

def forklift_accessory_recommendation(description: str) -> dict:
    """
    根据描述推荐叉车配件
    Args:
        description: 用户描述
    Returns:
        dict: 包含推荐配件信息的字典
    """
    # 定义常见叉车配件列表
    accessories = [
        {
            "name": "防滑叉齿套",
            "description": "增加叉齿与货物之间的摩擦力,防止货物滑落",
            "price": "¥300-500"
        },
        {
            "name": "货叉加长套",
            "description": "用于延长货叉长度,适合搬运超长货物",
            "price": "¥800-1200" 
        },
        {
            "name": "防护栏",
            "description": "保护驾驶员安全,防止货物意外掉落",
            "price": "¥1000-2000"
        },
        {
            "name": "工作灯",
            "description": "提供照明,适合夜间或光线不足环境作业",
            "price": "¥200-400"
        },
        {
            "name": "轮胎保护链",
            "description": "保护轮胎,增加抓地力,适合恶劣地面环境",
            "price": "¥600-900"
        },
        {
            "name": "蓄电池液位计",
            "description": "监测电池液位,避免电池过度放电",
            "price": "¥150-300"
        }
    ]
    
    import random
    # 随机选择2-3个配件推荐
    num_recommendations = random.randint(2, 3)
    recommendations = random.sample(accessories, num_recommendations)
    
    return {
        "query": description,
        "recommendations": recommendations
    }