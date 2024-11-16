# import asyncio
# import websockets

# from websockets.exceptions import ConnectionClosedError, ConnectionClosedOK


# # List to store all connected clients
# connected_clients = set()


# # Adjust the handle_connection function to accept both 'websocket' and 'path' arguments.
# async def handle_connection(websocket):
#     print("New client connected")


#     connected_clients.add(websocket)
#     print("New client connected")

#     try:
#         # Listen for incoming messages from the client
#         async for message in websocket:
#             print(f"Received message from client: {message}")
#             # You can process the received value here

#             await asyncio.gather(*[client.send(message) for client in connected_clients if client != websocket ])

#     except (ConnectionClosedError, ConnectionClosedOK ):
#         print("Client disconnected")
    
    
#     finally: 
#         # Reomve the client from the set when it disconnects 
#         connected_clients.remove(websocket)

# # Start the WebSocket server
# async def main():
#     async with websockets.serve(handle_connection, "localhost", 6789):
#         print("WebSocket server started on ws://localhost:6789")
#         await asyncio.Future()  # Run forever

# # Run the event loop
# asyncio.run(main())


# import asyncio 
# import websockets
# import json 
# from websockets.exceptions import ConnectionClosedError, ConnectionClosedOK 


# # List to store all connected clients 
# connected_clients = set() 

# slider_values = {
#     "sliderValue1": None, 
#     "sliderValue2": None
# }

# async def handle_connection(websocket):
#     # Add the new client to the set of connected clients
#     connected_clients.add(websocket)
#     print("New client connected")

#     try: 
#         async for message in websocket:
#             print(f"Received message from client: {message}")
        
#         # Parse the incoming message 
#         try:
#             data = json.loads(message)

#             if "sliderValue1" in data:
#                 slider_values["sliderValue1"] = data["sliderValue1"]
            
#             if "sliderValue2" in data:
#                 slider_values["sliderValue2"] = data["sliderValue2"]
            

#             # Prepare the message with both slider values 
#             broadcast_message = json.dumps(slider_values)

#             await asyncio.gather(
#                 *[client.send(broadcast_message) for client in connected_client if client != websocket ]
#             )
        
#         except json.JSONDecodeError:
#             print("Error: Received a non-JSON message")

#     except (ConnectionClosedError, ConnectionClosedOK):
#         print("Client disconnected")
    
#     finally: 
#         # Remove the client from the set when it disconnects 
#         connected_clients.remove(websocket)

# async def main():
#     async with websockets.serve(handle_connection, "localhost", 6789):
#         print("WebSocket server started on ws://localhost:6789")
#         await asyncio.Future() 

# # Run the event looop 
# asyncio.run(main())


import asyncio
import websockets
import json
from websockets.exceptions import ConnectionClosedError, ConnectionClosedOK

# List to store all connected clients
connected_clients = set()

# Track the values of both sliders
slider_values = {
    "sliderValue1": None,
    "sliderValue2": None
}

async def handle_connection(websocket):
    # Add the new client to the set of connected clients
    connected_clients.add(websocket)
    print("New client connected")

    try:
        async for message in websocket:
            print(f"Received message from client: {message}")
            
            # Parse the incoming message
            try:
                data = json.loads(message)
                
                # Update the relevant slider value
                if "sliderValue1" in data:
                    slider_values["sliderValue1"] = data["sliderValue1"]
                if "sliderValue2" in data:
                    slider_values["sliderValue2"] = data["sliderValue2"]

                # Prepare the message with both slider values
                broadcast_message = json.dumps(slider_values)

                # Broadcast the message to all connected clients
                await asyncio.gather(
                    *[client.send(broadcast_message) for client in connected_clients if client != websocket]
                )
            except json.JSONDecodeError:
                print("Error: Received a non-JSON message")

    except (ConnectionClosedError, ConnectionClosedOK):
        print("Client disconnected")
    finally:
        # Remove the client from the set when it disconnects
        connected_clients.remove(websocket)

# Start the WebSocket server
async def main():
    async with websockets.serve(handle_connection, "localhost", 6789):
        print("WebSocket server started on ws://localhost:6789")
        await asyncio.Future()  # Run forever

# Run the event loop
asyncio.run(main())