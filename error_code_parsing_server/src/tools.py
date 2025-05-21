import random

def parse_forklift_error(error_code: str) -> dict:
    """
    解析叉车故障码,返回故障描述和建议解决方案
    Args:
        errorcode: 故障码字符串
    Returns:
        dict: 包含故障描述和解决方案的字典
    """
    error_mappings = {
        "E001": {
            "description": "液压系统压力异常",
            "solution": "检查液压油位和管路是否泄漏,必要时补充液压油"
        },
        "E002": {
            "description": "驱动电机过热",
            "solution": "停止作业让电机冷却,检查散热系统是否正常工作"
        },
        "E003": {
            "description": "电池电量过低",
            "solution": "及时充电或更换电池,建议电量低于20%时及时充电"
        },
        "E004": {
            "description": "转向系统故障", 
            "solution": "检查转向电机和转向机构,排查机械卡死情况"
        },
        "E005": {
            "description": "制动系统异常",
            "solution": "检查制动油位和制动片磨损情况,必要时更换制动片"
        },
        "E006": {
            "description": "门架升降异常",
            "solution": "检查门架导轨是否变形,链条是否松动,必要时调整或更换"
        },
        "E007": {
            "description": "倾斜油缸泄漏",
            "solution": "检查油缸密封圈,更换损坏的密封件"
        }
    }
    
    if error_code in error_mappings:
        return error_mappings[error_code]
    else:
        # 如果找不到对应故障码,返回通用提示
        return {
            "description": "未知故障码",
            "solution": "请联系维修人员进行检查"
        }