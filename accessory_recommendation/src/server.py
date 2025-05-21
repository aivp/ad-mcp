#!/usr/bin/env python3
import argparse
import logging
import os
from typing import Dict, Optional
from mcp.server.fastmcp import FastMCP
import json
from datetime import datetime
import sys
from tools import forklift_accessory_recommendation
# Configure logging with more detailed format
logging.basicConfig(
    level=logging.DEBUG,  # 改为 DEBUG 级别以显示更多信息
    format="%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('mcp_server.log')  # 同时输出到文件
    ]
)
logger = logging.getLogger(__name__)

# Global variables
viking_knowledgebase_service = None

# Create MCP server
port = int(os.getenv("PORT", "8000"))
logger.info(f"Initializing MCP server on port {port}")
mcp = FastMCP("Server", port=port)
       
@mcp.tool() 
def accessory_recommendation(description: str):
    """
    根据描述进行配件的推荐
    Args:
        description:用户的描述
    """
    return forklift_accessory_recommendation(description)

def main():
    """Main entry point for the MCP server."""
    logger.info("Starting MCP server initialization")
    parser = argparse.ArgumentParser(
        description="Run the MCP Server"
    )
    parser.add_argument(
        "--transport",
        "-t",
        choices=["sse", "stdio"],
        default="stdio",
        help="Transport protocol to use (sse or stdio)",
    )

    args = parser.parse_args()
    logger.info(f"Server configuration: transport={args.transport}, port={port}")

    try:
        logger.info("Starting MCP server...")
        mcp.run(transport=args.transport)
    except Exception as e:
        logger.error(f"Critical error in MCP Server: {str(e)}", exc_info=True)
        raise
    finally:
        logger.info("MCP server shutdown")

if __name__ == "__main__":
    try:
        logger.info("=== MCP Server Starting ===")
        main()
    except KeyboardInterrupt:
        logger.info("Server stopped by user (KeyboardInterrupt)")
    except Exception as e:
        logger.critical(f"Fatal error: {str(e)}", exc_info=True)
        sys.exit(1)