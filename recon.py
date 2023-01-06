import socket

def scan_ports(host, start_port, end_port):
  open_ports = []

  for port in range(start_port, end_port+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((host, port))
    if result == 0:
      open_ports.append(port)
    s.close()

  return open_ports

if __name__ == "__main__":
  host = input("Enter target host: ")
  start_port = int(input("Enter start port: "))
  end_port = int(input("Enter end port: "))

  open_ports = scan_ports(host, start_port, end_port)

  print(f"Open ports: {open_ports}")
