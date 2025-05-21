FROM hub.docker-proxy.aidong.ai/library/python:3.12.7

WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制源代码
COPY src/ ./src/

# 暴露端口
EXPOSE 8000

# 设置环境变量
ENV PORT=8000

# 启动命令
CMD ["python", "src/server.py", "--transport", "sse"] 