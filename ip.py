from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def message():
    # Get the IP address of the user
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
   
    # Get the user agent of the user
    user_agent = request.headers.get('User-Agent')
   
    # Get the hostname of the user
    hostname = request.host
   
    # Get the referrer of the user
    referrer = request.referrer

    print()
   
    # Print the IP address, user agent, hostname, and referrer to the console
    print(f"IP address: {ip_address}")

    print()

    print(f"User agent: {user_agent}")

    print()
 
    print(f"Hostname: {hostname}")

    print()
 
    print(f"Referrer: {referrer}")

    print()
   
    return '''
        <!DOCTYPE html>
        <html>
            <head>
                <title>IP Log Tool</title>
            </head>

            <body style="background-color:lightgray;">
                <h1>IP Logger</h1>
                <p>Your Ip Has Been Logged</p>
                
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
