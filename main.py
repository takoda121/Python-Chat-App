import requests, json, customtkinter,tkinter, threading, time
from tkinter import messagebox

DOMAIN = "http://localhost:8080/ami.php?" #The url/file for the api
AUTO_UPDATE_CHAT = True #Updates the chat every 3 seconds.
texte = str(requests.get(f"{DOMAIN}pswrd").text)

def convert_to_dict(text):
    lines = text.split("<br>")
    data = {"username":[], "message":[], "time":[]}

    for line in lines:
        parts = line.split(" ")
        data["username"].append(parts[1])
        data["message"].append(parts[3])
        data["time"].append(parts[5])
    return(data)


print(convert_to_dict(texte))
output = convert_to_dict(texte)
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("500x600")
app.title("Chat App")


tabview_1 = customtkinter.CTkTabview(master=app, width=500, height=300)
tabview_1.grid(row=1, column=0, columnspan=2, padx=(10, 0), pady=(10, 20), sticky="nsew")
tabview_1.add("Channel 1")
#tabview_1.add("Channel 2")
textbox = customtkinter.CTkTextbox(tabview_1.tab("Channel 1"), width=430, state="disabled")
textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
textbox.configure(state="normal")

        
def update_text():
    count = 0
    textbox.configure(state="normal")
    kundaprc = convert_to_dict(str(requests.get(f"{DOMAIN}pswrd").text))
    textbox.delete(1.0, "end")
    for stupid in kundaprc["username"]:
        count = count + 1
        msg = kundaprc["message"][count-1]
        msg = msg.replace("Ł", " ")
        if (count + 1 > 20):
            cunt = 0
            textbox.delete("1.0", tkinter.END)
            last_lines = kundaprc["username"][-20:]
            for line in last_lines:
                kripl = kundaprc["message"][-20+cunt]
                kokotskykripl = kripl.replace("Ł", " ")
        if "\u3164" in stupid:
            print("huh")
            line = stupid.replace("\u3164","")
            username = line.split(": ")
            textbox.insert("end", username, "username_tag")
            textbox.tag_config("username_tag", foreground="red")
            textbox.insert("end", f": {msg}")
        else:
            textbox.insert("end", f'{stupid}: {msg} \n',)
        if stupid == "":
            textbox.insert("end", stupid + " "+msg+ "\n","username_tag")
            textbox.tag_config("username_tag", foreground="red")
        textbox.see(tkinter.END)
    textbox.configure(state="disabled")

def kokotar():
    while 1 != 2:
        time.sleep(3)
        update_text()
if AUTO_UPDATE_CHAT == True:
    t = threading.Thread(target=kokotar).start()
count = 0
for stupid in output["username"]:
        count = count + 1
        msg = output["message"][count-1]
        msg = msg.replace("Ł", " ")
        if (count + 1 > 20):
            cunt = 0
            textbox.delete("1.0", tkinter.END)
            last_lines = output["username"][-20:]
            if (count + 1 > 20):
                cunt = 0
                textbox.delete("1.0", tkinter.END)
                last_lines = output["username"][-20:]
                for line in last_lines:
                    kripl = output["message"][-20+cunt]
                    kokotskykripl = kripl.replace("Ł", " ")
                    if "ㅤ" in line:
                        buduprcatte = line.replace("ㅤ", "")
                        textbox.tag_config(buduprcatte, foreground="red")
                        textbox.insert("end", f'{buduprcatte}: {msg} \n')
                    else:
                        textbox.insert("end", f'{line}: {kokotskykripl} \n')
                    cunt = cunt + 1
        if stupid == "":
            textbox.insert("end", stupid + " "+msg+ "\n")
        else:
            if "ㅤ" in stupid:
                buduprcatte = stupid.replace("ㅤ", "")
                textbox.tag_config(buduprcatte, foreground="red")
                textbox.insert("end", f'{buduprcatte}: {msg} \n')
            else:
                textbox.insert("end", f'{stupid}: {msg} \n')
textbox.configure(state="disabled")
textbox.yview_moveto(1.0)
textbox.see(tkinter.END)

entry = customtkinter.CTkEntry(app, placeholder_text="ChatKey")
entry.grid(row=3, column=0, columnspan=1, padx=(0, 0), pady=(20, 20), sticky="nsew")
entrya = customtkinter.CTkEntry(app, placeholder_text="Message")
entrya.grid(row=4, column=0, columnspan=1, padx=(0, 0), pady=(20, 20), sticky="nsew")
def write():
    key= entry.get()
    bab= entrya.get()
    if "Ł" in bab:
        messagebox.showinfo("Alert", "A letter (Ł) in your message was blacklisted!")
        return
    requests.get(f"{DOMAIN}pswrde&userl={key}&msgl={bab}")
    update_text()

string_input_button = customtkinter.CTkButton(app, text="Send",command=write)
string_input_button.grid(row=5, column=0, padx=20, pady=(10, 10))
string_input_button = customtkinter.CTkButton(app, text="Update Chat",command=update_text)
string_input_button.grid(row=6, column=0, padx=20, pady=(10, 10))
app.mainloop()