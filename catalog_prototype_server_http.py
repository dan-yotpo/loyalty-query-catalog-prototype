#!/usr/bin/env python3
"""
Hosted entry point for the catalog prototype MCP server.

This does NOT redefine any tools. It imports the already-built `server`
object from catalog_prototype_server.py (which registers all 27 tools at
import time) and runs it over HTTP instead of stdio, so it can be deployed
somewhere colleagues can reach over a URL instead of everyone needing a
local Python install pointed at a local file.

Run locally to test the HTTP version before deploying:
    PORT=8000 python3 catalog_prototype_server_http.py
    -> serves at http://127.0.0.1:8000/mcp

On a host like Render, the platform sets $PORT for you automatically.
"""
import os

from catalog_prototype_server import server

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    server.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=port,
        streamable_http_path="/mcp",
    )
