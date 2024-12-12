from television import Television  # import statement needed to gain access to Television class
from remote import * # import statement to import all of gui_television


def main():
    window = Tk()
    window.title('TV Remote')
    window.geometry('300x700')
    window.resizable(False, False)

    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()