import os
import sys
import socket

PORT = 4242
socket_binder = socket.socket()
socket_binder.bind(('localhost', PORT))
socket_binder.listen(10)

for _ in range(3):
    pid = os.fork()

    if pid == 0:  # child process
        """
        Child processes can be invoked by loading localhost:PORT in browser
        """
        child_pid = os.getpid()
        print(f"Child {child_pid} is listening on port {PORT}")
        try:
            while True:
                connection, address = socket_binder.accept()
                fd = connection.makefile('rw')

                fd.write(f"Child {child_pid} echo")
                fd.flush()
                message = fd.readline()
                fd.write(message)
                connection.close()
                print(f"Child {child_pid} echo'd {message.strip()}")
        except KeyboardInterrupt:
            sys.exit()

try:
    os.waitpid(-1, 0)
except KeyboardInterrupt:
    print("Keyboard Abort Initiated")
    sys.exit()
