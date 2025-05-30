# ADmcp 故障码解析服务

## 项目简介

ADmcp 故障码解析服务是 ADmcp 项目的一个子模块，基于 MCP（Model Context Protocol）协议实现，专注于为叉车用户提供故障码解析服务。该服务通过分析故障码，为用户提供准确的故障描述和解决方案建议。

## 主要功能

- **故障码解析**  
  输入叉车故障码，快速返回对应的故障描述和建议解决方案。

- **故障诊断建议**  
  根据故障类型，提供详细的诊断步骤和维修建议。

- **故障码管理**  
  支持多种品牌和型号叉车的故障码数据库管理。

## 目录结构

```
.
├── src/
│   ├── server.py           # 服务主程序，MCP 工具注册与服务入口
│   └── tools.py            # 故障码解析核心逻辑
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
          "name": "error_code_parsing",
          "description": "解析叉车故障码，返回描述和解决方案",
          "parameters": {
            "type": "object",
            "properties": {
              "error_code": {
                "type": "string",
                "description": "故障码"
              }
            },
            "required": ["error_code"]
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
  "error_code": "E005"
}
```

返回示例：
```json
{
  "error_code": "E005",
  "description": "制动系统异常",
  "solution": "检查制动油位和制动片磨损情况，必要时更换制动片",
  "severity": "高",
  "affected_systems": ["制动系统", "液压系统"],
  "maintenance_priority": "立即处理"
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
docker build -t admcp-error-parser .

# 运行容器
docker run -d -p 8000:8000 --name admcp-error-parser admcp-error-parser

# 查看容器日志
docker logs -f admcp-error-parser

# 停止容器
docker stop admcp-error-parser
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