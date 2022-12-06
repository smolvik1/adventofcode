import os

input = os.path.join(os.path.dirname(__file__), "input.txt")
buffer = open(input, "r").read()
packet_length = 4
message_length = 14


def uniqueCharacters(str):
    setstring = set(str)
    if len(setstring) == len(str):
        return True
    else:
        return False


packetstart = ""
messagestart = ""

for i in range(0, len(buffer) - packet_length + 1):
    packet = buffer[i : (i + packet_length)]
    if (uniqueCharacters(packet)) and (not packetstart):
        packetstart = i + packet_length
    if i <= len(buffer) - message_length + 1:
        message = buffer[i : (i + message_length)]
        if (uniqueCharacters(message)) and (not messagestart):
            messagestart = i + message_length

print(packetstart)
print(messagestart)
