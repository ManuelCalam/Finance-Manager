windowWidth = 800
windowHeight = 500 

def centerWindow(window):
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    pos_x = (screenWidth - windowWidth) // 2
    pos_y = (screenHeight - windowHeight) // 2
 
    window.geometry(f"{windowWidth}x{windowHeight}+{pos_x}+{pos_y}")