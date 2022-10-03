from concurrent.futures import ThreadPoolExecutor

import grpc

from protos.builds.services_pb2_grpc import add_WatermarkServiceServicer_to_server
from WatermarkService import WatermarkService


def execute_server():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_WatermarkServiceServicer_to_server(WatermarkService(), server)
    server.add_insecure_port("[::]:3000")
    server.start()

    print("The server is up and running...")
    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()
