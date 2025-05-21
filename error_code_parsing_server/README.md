# ADmcp 项目说明

## 项目简介

ADmcp 是一个基于 MCP（Model Context Protocol）协议的服务，主要用于叉车相关的智能工具服务，包括故障码解析和配件推荐。项目采用 Python 实现，支持通过 SSE 协议与外部智能体集成，以实现智能推荐和错误代码解析功能。

## 主要功能

- **故障码解析**  
  输入叉车故障码，快速返回对应的故障描述和建议解决方案。

- **配件推荐**  
  根据用户描述，智能推荐适合的叉车配件及其简要说明和参考价格。

## 目录结构

```
.
├── src/
│   ├── server.py           # 服务主程序，MCP 工具注册与服务入口
│   └── tools.py            # 叉车故障码解析与配件推荐核心逻辑
├── requirements.txt        # Python 依赖包列表
└── README.md               # 项目说明文档

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

在 `.cursor/mcp.json` 中注册工具，例如：

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
          "name": "error_code_parsing",
          "description": "解析叉车故障码，返回描述和解决方案",
          "parameters": {
            "type": "object",
            "properties": {
              "errorcode": {
                "type": "string",
                "description": "故障码"
              }
            },
            "required": ["error_code"]
          }
        },
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

- **故障码解析**

  ```json
  {
    "errorcode": "E005"
  }
  ```
  返回：
  ```json
  {
    "description": "制动系统异常",
    "solution": "检查制动油位和制动片磨损情况,必要时更换制动片"
  }
  ```

- **配件推荐**

  ```json
  {
    "description": "叉车需要新的配件"
  }
  ```
  返回示例：
  ```json
  {
    "query": "叉车需要新的配件",
    "recommendations": [
      {
        "name": "防滑叉齿套",
        "description": "增加叉齿与货物之间的摩擦力,防止货物滑落",
        "price": "¥300-500"
      },
      ...
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
docker build -t admcp .

# 运行容器
docker run -d -p 8000:8000 --name admcp admcp

# 查看容器日志
docker logs -f admcp

# 停止容器
docker stop admcp
```