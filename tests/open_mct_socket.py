import asyncio
import websockets
import json

async def subscribe_to_telemetry(websocket_url, telemetry_id, callback):
    """Subscribes to a specific telemetry point on the WebSocket.

    Args:
        websocket_url (str): The URL of the WebSocket server.
        telemetry_id (str): The identifier of the telemetry point to subscribe to.
        callback (callable): A function to be called with received telemetry data.
    """

    async with websockets.connect(websocket_url) as websocket:
        # Subscribe to the telemetry point
        await websocket.send(f"subscribe {telemetry_id}")

        async for message in websocket:
            try:
                point = json.loads(message)
                if point["id"] == telemetry_id:
                    await callback(point)
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error processing message: {e}")

async def main():
    websocket_url = "ws://localhost:8080/realtime"  # Replace with actual URL
    telemetry_id = "pwr.c"  # Replace with the ID you want to subscribe to

    async def handle_telemetry(data):
        print(f"Received telemetry data for {telemetry_id}: {data}")

    await subscribe_to_telemetry(websocket_url, telemetry_id, handle_telemetry)

if __name__ == "__main__":
    asyncio.run(main())