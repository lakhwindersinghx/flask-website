from website import create_app


app=create_app()

if __name__=='__main__':
    app.run(debug=True)
    #everytimme we make change to app, this updates and reruns the server