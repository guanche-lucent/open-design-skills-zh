#!/usr/bin/env python3
"""Serve only local examples; does not open a browser or publish externally."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from pathlib import Path
import argparse
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--port',type=int,default=8772)
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]/'examples'
server=ThreadingHTTPServer(('127.0.0.1',args.port),partial(SimpleHTTPRequestHandler,directory=str(root)))
print(f'案例集：http://127.0.0.1:{server.server_port}/reference-replicas/index.html',flush=True)
print('按 Ctrl+C 停止。',flush=True)
try: server.serve_forever()
except KeyboardInterrupt: pass
finally: server.server_close()
