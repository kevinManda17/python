from kivy.lang import Builder 
from kivy.core.window import Window 
from kivymd.app import MDApp
from kivymd.uix.screen import Screen 
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp 


#set the app size 
Window.size = (700, 500)

class MainApp(MDApp):

    def build(self):
        screen = Screen()

        table = MDDataTable(
            size_hint= (0.9, 0.6 ),
            pos_hint = {"center_x":0.5, "center_y":0.5},
            check =True, 
            use_pagination= True,
            rows_num = 3, 
            pagination_menu_height = "240dp",
            pagination_menu_pos= "center",
            background_color=[1,0,0,.5],
            column_data = [
                ("First Name", dp(40)),
                ("Last Name", dp(40)),
                ("Email Address", dp(35)),
                ("Phone Number", dp(35)),
            ],
            row_data = [
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kevin","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Kestia","Manda","kevmulambomm@gmail.com","+243 822979260"),
                ("Iron-manda","Manda","kevmulambomm@gmail.com","+243 822979260"),



            ]
        )

        #bind table 
        table.bind(on_check_press= self.checked)
        table.bind(on_row_press= self.row_checked)

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        # return Builder.load_file("data_tables_pagination.kv")
        # add table widget to screen
        screen.add_widget(table)
        return screen 
    
    #Function for check presses 
    def checked(self, instance_table, current_row):
        print(instance_table, current_row)

    #Function for row presses 
    def row_checked(self, instance_table, instance_row,):
        print(instance_table, instance_row)


MainApp().run()

