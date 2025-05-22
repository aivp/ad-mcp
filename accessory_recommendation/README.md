# ADmcp 配件推荐服务

## 项目简介

ADmcp 配件推荐服务是 ADmcp 项目的一个子模块，基于 MCP（Model Context Protocol）协议实现，专注于为叉车用户提供智能配件推荐服务。该服务通过分析用户需求和使用场景，为用户推荐最适合的叉车配件。

## 主要功能

- **智能配件推荐**  
  根据用户描述，智能推荐适合的叉车配件及其简要说明和参考价格。

- **配件分类管理**  
  支持多种配件类型的分类和筛选，包括液压系统、电气系统、制动系统等。

- **用户偏好分析**  
  学习用户的使用习惯和偏好，提供更精准的推荐。

## 目录结构

```
.
├── src/
│   ├── server.py           # 服务主程序，MCP 工具注册与服务入口
│   └── tools.py            # 配件推荐核心逻辑
├── requirements.txt        # Python 依赖包列表
├── Dockerfile             # Docker 构建文件
├── docker-compose.yml     # Docker Compose 配置
└── README.md              # 项目说明文档
```

## 快速开始

### 1. 安装依赖

建议使用虚拟环境：

```bash
python -m venv .venv
source .venv/bin/activate  # Windows 下为 .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 启动服务

```bash
python src/server.py --transport sse
```

服务默认监听本地 8000 端口，支持 SSE 协议。

### 3. 配置 MCP 工具（以 Cursor 为例）

在 `.cursor/mcp.json` 中注册工具：

```json
{
  "mcpServers": {
    "local-server": {
      "command": "python",
      "args": [
        "./src/server.py",
        "--transport",
        "sse"
      ],
      "env": {
        "PORT": "Port"
      },
      "type": "sse",
      "url": "http://IP:Port/sse",
      "tools": [
        {
          "name": "accessory_recommendation",
          "description": "根据描述推荐叉车配件",
          "parameters": {
            "type": "object",
            "properties": {
              "description": {
                "type": "string",
                "description": "配件需求描述"
              }
            },
            "required": ["description"]
          }
        }
      ]
    }
  }
}
```

### 4. 工具调用示例

```json
{
  "description": "叉车需要更换制动片"
}
```

返回示例：
```json
{
  "query": "叉车需要更换制动片",
  "recommendations": [
    {
      "name": "制动片套装",
      "description": "适用于叉车制动系统，包含制动片和安装配件",
      "price": "¥800-1200",
      "compatibility": ["CPD15", "CPD20", "CPD25"],
      "estimated_lifetime": "6-12个月"
    },
    {
      "name": "制动片（单件）",
      "description": "单个制动片，适用于紧急更换",
      "price": "¥200-300",
      "compatibility": ["CPD15", "CPD20", "CPD25"],
      "estimated_lifetime": "3-6个月"
    }
  ]
}
```

## Docker 部署

### 1. 使用 Docker Compose 启动服务

```bash
# 构建并启动服务
docker-compose up -d

# 查看服务日志
docker-compose logs -f

# 停止服务
docker-compose down
```

### 2. 直接使用 Docker 命令

```bash
# 构建镜像
docker build -t admcp-accessory .

# 运行容器
docker run -d -p 8001:8001 --name admcp-accessory admcp-accessory

# 查看容器日志
docker logs -f admcp-accessory

# 停止容器
docker stop admcp-accessory
```

## 开发说明

### 日志配置

服务使用 Python 的 logging 模块进行日志记录，日志文件位于 `mcp_server.log`。日志级别设置为 DEBUG，包含详细的时间戳、文件名和行号信息。

### 错误处理

服务实现了完整的错误处理机制：
- 参数验证
- 异常捕获和日志记录
- 友好的错误提示

### 测试

建议在提交代码前进行以下测试：
1. 单元测试
2. 集成测试
3. 接口测试

## 许可证

MIT License

## 联系方式

如有问题或建议，请通过以下方式联系我们：
- 提交 Issue
- 发送邮件至：[项目邮箱]
