import http.server
import ssl

# Definir o endereço e a porta do servidor
server_address = ('localhost', 8080)

# Criar um servidor HTTP simples
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Configurar o contexto SSL com os certificados
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile="server.crt", keyfile="server.key")

# Envolver o socket do servidor com SSL
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

print("Servidor HTTPS rodando em https://localhost:8080")
httpd.serve_forever()