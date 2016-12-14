import tkinter as tk

class DropMenu(tk.Frame):

    def __init__(
        self,
        parent,
        controller
        ):
        tk.Frame.__init__(
            self,
            parent
            )   
        self.controller = controller

        self.init_window()

    def init_window(self):

        self.pack(fill=tk.BOTH, expand=1)

        menu = tk.Menu(self.controller)
        self.controller.config(menu=menu)

        
        Home = tk.Menu(menu)
        
        Home.add_command(
            label="Go to HomePage",
            command=lambda:
            self.controller.show_frame("MainMenu")
            )
        Home.add_separator()
        Home.add_command(
            label="Snake Wallpapers(HD)",
            )
        Home.add_command(
            label="Snake Bite First Aid"
            )
        Home.add_separator()
        Home.add_command(
            label="Exit"
            )
        menu.add_cascade(
            label="Home",
            menu=Home
            )
        
        #Snakes
        Family = tk.Menu(menu)
        #Family
        Alethinophidia = tk.Menu(Family)
        Scolecophidia = tk.Menu(Family)

        #Alethinophidia(15)[Serpentes]
        Acrochordidae = tk.Menu(Alethinophidia)
        Aniliidae = tk.Menu(Alethinophidia)
        Anomochilidae = tk.Menu(Alethinophidia)
        Atractaspididae = tk.Menu(Alethinophidia)
        Boidae = tk.Menu(Alethinophidia)
        Bolyeriidae = tk.Menu(Alethinophidia)
        Colubridae = tk.Menu(Alethinophidia)
        Cylindrophiidae = tk.Menu(Alethinophidia)
        Elapidae = tk.Menu(Alethinophidia)
        Loxocemidae = tk.Menu(Alethinophidia)
        Pythonidae = tk.Menu(Alethinophidia)
        Tropidophiidae = tk.Menu(Alethinophidia)
        Uropeltidae = tk.Menu(Alethinophidia)
        Viperdae = tk.Menu(Alethinophidia)
        Xenopeltidae = tk.Menu(Alethinophidia)

        #Scolecophidia(3)[Serpentes]
        Anomalepidae = tk.Menu(Scolecophidia)
        Leptotyphlopidae = tk.Menu(Scolecophidia)
        Typhlopidae = tk.Menu(Scolecophidia)

        Family.add_cascade(
            label="Alethinophidia",
            menu=Alethinophidia
            )
        Family.add_cascade(
            label="Scolecophidia",
            menu=Scolecophidia
            )

        #Acrochordidae[Genera]
        Alethinophidia.add_cascade(
            label="Acrochordidae - File Snakes",
            menu=Acrochordidae
            )

        Acrochordus = tk.Menu(Acrochordidae)
        Acrochordidae.add_cascade(
            label="Acrochordus - Java Wart Snakes",
            menu=Acrochordus
            )

        #Aniliidae[Genera]
        Alethinophidia.add_cascade(
            label="Aniliidae - Coral Pipe Snakes",
            menu=Aniliidae
            )

        Aniliius = tk.Menu(Aniliidae)
        Aniliidae.add_cascade(
            label="Anillius - American Pipe SSnake",
            menu=Aniliius
            )

        #Anomochilidae[Genera]
        Alethinophidia.add_cascade(
            label="Anomochilidae - Dwarf Pipe Snakes",
            menu=Anomochilidae
            )

        Anomochilius = tk.Menu(Anomochilidae)
        Anomochilidae.add_cascade(
            label="Anomochilius - Dwarf Pipe Snakes",
            menu=Anomochilius
            )

        #Atractaspididae[Genera]
        Alethinophidia.add_cascade(
            label="Atractaspididae - Stiletto Snakes",
            menu=Atractaspididae
            )

        Amblyodipsas = tk.Menu(Atractaspididae)
        Aparallactus = tk.Menu(Atractaspididae)
        Atractaspis = tk.Menu(Atractaspididae)
        Brachyophis = tk.Menu(Atractaspididae)
        Chilorphinophis = tk.Menu(Atractaspididae)
        Elapotinus = tk.Menu(Atractaspididae)
        Hypoptophis = tk.Menu(Atractaspididae)
        Macrelaps = tk.Menu(Atractaspididae)
        Micrelaps = tk.Menu(Atractaspididae)
        Poecilopholis = tk.Menu(Atractaspididae)
        Polemon = tk.Menu(Atractaspididae)
        Xenocalamus = tk.Menu(Atractaspididae)

        #Boidae[Genera]
        Alethinophidia.add_cascade(
            label="Boidae - Boas",
            menu=Boidae
            )

        Boinae = tk.Menu(Boidae)
        Boa = tk.Menu(Boidae)
        Candoia = tk.Menu(Boidae)
        Epicrates = tk.Menu(Boidae)
        Eunectes = tk.Menu(Boidae)
        Erycinae = tk.Menu(Boidae)
        Charina = tk.Menu(Boidae)
        Eryx = tk.Menu(Boidae)
        Gongylophis = tk.Menu(Boidae)

        #Bolyeriidae[Genera]
        Alethinophidia.add_cascade(
            label="Bolyeridae - Round Island Boas",
            menu=Bolyeriidae
            )
        
        Bolyeria = tk.Menu(Bolyeriidae)
        Casarea = tk.Menu(Bolyeriidae)

        #Colubridae[Genera]
        Alethinophidia.add_cascade(
            label="Colubridae - Colubrids",
            menu=Colubridae
            )

        IncertaeSedis = tk.Menu(Colubridae)
        Blythia = tk.Menu(Colubridae)
        Cercaspis = tk.Menu(Colubridae)
        Cyclocorus = tk.Menu(Colubridae)
        Elapoidis = tk.Menu(Colubridae)
        Gongylosoma = tk.Menu(Colubridae)
        Haplocercus = tk.Menu(Colubridae)
        Helophis = tk.Menu(Colubridae)
        Myersophis = tk.Menu(Colubridae)
        Oreocalamus = tk.Menu(Colubridae)
        Poecilopholis = tk.Menu(Colubridae)
        Rhabdops = tk.Menu(Colubridae)
        Tetralepsis = tk.Menu(Colubridae)
        Thermophis = tk.Menu(Colubridae)
        Trachischium = tk.Menu(Colubridae)
        Xenodermatinae = tk.Menu(Colubridae)
        Achalinus = tk.Menu(Xenodermatinae)
        Fimbrios = tk.Menu(Xenodermatinae)
        Oxyrhabdium = tk.Menu(Xenodermatinae)
        Stoliczkia = tk.Menu(Xenodermatinae)
        Xenodermus = tk.Menu(Xenodermatinae)
        Xylophis = tk.Menu(Xenodermatinae)
        Pareatinae = tk.Menu(Xenodermatinae)
        Aplopeltura = tk.Menu(Xenodermatinae)
        Asthenodipsas = tk.Menu(Xenodermatinae)
        Pareas = tk.Menu(Xenodermatinae)
        Calamariinae = tk.Menu(Xenodermatinae)
        Calamaria = tk.Menu(Xenodermatinae)
        Calamorhabdium = tk.Menu(Xenodermatinae)
        Collorhabdium = tk.Menu(Xenodermatinae)
        Etheridgeum = tk.Menu(Xenodermatinae)
        Macrocakamus = tk.Menu(Xenodermatinae)
        Pseudorabdion = tk.Menu(Xenodermatinae)
        Rabdion = tk.Menu(Xenodermatinae)
        Homalopsinae = tk.Menu(Colubridae)
        Bitia = tk.Menu(Homalopsinae)
        Cantoria = tk.Menu(Homalopsinae)
        Cerberus = tk.Menu(Homalopsinae)
        Enhydris = tk.Menu(Homalopsinae)
        Erpeton = tk.Menu(Homalopsinae)
        Fordonia = tk.Menu(Homalopsinae)
        Gerarda = tk.Menu(Homalopsinae)
        Heurnia = tk.Menu(Homalopsinae)
        Homalopsis = tk.Menu(Homalopsinae)
        Myron = tk.Menu(Homalopsinae)
        
        

        #Cylindrophiidae[Genera]
        Alethinophidia.add_cascade(
            label="Cylindrophiidae - Asias Pipe Snakes",
            menu=Cylindrophiidae
            )

        #Elapidae[Genera]
        Alethinophidia.add_cascade(
            label="Elapidae - Cobras, Coral Snakes, Mambas, Kraits, Sea Snakes, Australian Elapids",
            menu=Elapidae
            )

        #Loxocemidae[Genera]
        Alethinophidia.add_cascade(
            label="Loxocemidae - Mexican Burrowing Snake",
            menu=Loxocemidae
            )

        #Pythonidae[Genera]
        Alethinophidia.add_cascade(
            label="Pythonidae - Pythons",
            menu=Pythonidae
            )

        #Tropidophiidae[Genera]
        Alethinophidia.add_cascade(
            label="Tropidophiidae - Dwarf Boas",
            menu=Tropidophiidae
            )

        #Uropeltidae[Genera]
        Alethinophidia.add_cascade(
            label="Uropeltidae - Shield-tailed Snakes, Short-tailed Snakes",
            menu=Uropeltidae
            )


        #Viperdae[Genera]
        Alethinophidia.add_cascade(
            label="Viperdae - Vipers, Pitvipers, Rattlesnakes",
            menu=Viperdae
            )
        Bitis = tk.Menu(Viperdae)
        Bitis.add_command(
            label="Bitis arietans - Puff Adder",
            command=lambda:
            self.controller.show_frame("BitisArietans")
            )
        Bitis.add_command(
            label="Bitis atropas - Berg Adder",
            command=lambda:
            self.controller.show_frame("BitisAtropas")
            )
        Bitis.add_command(
            label="Bitis gabonica - Gaboon Adder",
            command=lambda:
            self.controller.show_frame("BitisGabonica")
            )
        Viperdae.add_cascade(
            label="Bitis",
            menu=Bitis,
            )

        #Xenopeltidae[Genera]
        Alethinophidia.add_cascade(
            label="Xenopeltidae - Sundeam Snakes",
            menu=Xenopeltidae
            )
        

        menu.add_cascade(
            label="Snake Families",
            menu=Family
            )

        #Anomalepidae[Genera]
        Scolecophidia.add_cascade(
            label="Anomalephidae - Dawn Blind Snakes",
            menu=Anomalepidae
            )

        #Leptotyphlopidae[Genera]
        Scolecophidia.add_cascade(
            label="Leptotyphlopidae - Slender Blind Snakes",
            menu=Leptotyphlopidae
            )

        #Typhlopidae[Genera]
        Scolecophidia.add_cascade(
            label="Typhlopidae - Blind Snakes",
            menu=Typhlopidae
            )
        
        Biology = tk.Menu(menu)
        Venom = tk.Menu(Biology)
        Fangs = tk.Menu(Biology)
        
        #Venom
        Venom.add_command(
            label="Basic Venom Description",
            command=lambda:
            self.controller.show_frame("VenomBasics")
            )
        Venom.add_command(
            label="Haemotoxic",
            command=lambda:
            self.controller.show_frame("HaemoToxic")
            )
        Venom.add_command(
            label="Cytotoxic",
            command=lambda:
            self.controller.show_frame("CytoToxic")
            )
        Venom.add_command(
            label="Neurotoxic",
            command=lambda:
            self.controller.show_frame("NeuroToxic")
            )
        Venom.add_command(
            label="Myotoxic",
            command=lambda:
            self.controller.show_frame("MyoToxic")
            )

        #Fangs
        Fangs.add_command(
            label="Proteroglyphous",
            )
        Fangs.add_command(
            label="Solenoglyphous",
            )
        Fangs.add_command(
            label="Opistoglyphous",
            )
        Fangs.add_command(
            label="Aglyphous",
            )
        menu.add_cascade(
            label="Snake Biology",
            menu=Biology
            )
        Biology.add_cascade(
            label="Venom",
            menu=Venom
            )
        Biology.add_cascade(
            label="Fangs",
            menu=Fangs
            )
        

        

