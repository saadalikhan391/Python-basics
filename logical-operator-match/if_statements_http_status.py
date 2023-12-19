http_status = 601
internet = 600
if http_status == 200 or http_status == 201:
    print("success")
elif http_status == 400:
    print("bad request")
elif http_status == 404:
    print("not found")
elif http_status == 500 or http_status ==501:
    print("server error")
elif http_status == 601 and internet == 600:
    print("internet service down")
else:
    print("Unkown status")