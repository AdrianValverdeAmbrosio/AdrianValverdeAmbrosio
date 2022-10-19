# Import llibreria per a la base de dades 
import sqlite3

# Connexió base de dades 
basededades=sqlite3.connect("BaseDeDades")
connexio=basededades.cursor()

# Creació taules
connexio.execute("CREATE TABLE IF NOT EXISTS INFORMACIO (Ident integer PRIMARY KEY, Nom VARCHAR(100), Primer_Cognom VARCHAR(20), Segon_Cognom VARCHAR(20), Data VARCHAR(10), Tema VARCHAR(50), Hora VARCHAR(22), Aula VARCHAR(50), Tutor VARCHAR(50))") 
connexio.execute("CREATE TABLE IF NOT EXISTS INFORMACIO2 (Ident integer PRIMARY KEY, Nom VARCHAR(100), Primer_Cognom VARCHAR(20), Segon_Cognom VARCHAR(20), Alumne_TR1 VARCHAR(100), Alumne_TR2 VARCHAR(100), Alumne_TR3 VARCHAR(100), Alumne_TR1ibunal1 VARCHAR(100), Alumne_TR1ibunal2 VARCHAR(100), Alumne_TR1ibunal3 VARCHAR(100))")
connexio.execute("CREATE TABLE IF NOT EXISTS INFORMACIO3 (Ident_TR VARCHAR(100) PRIMARY KEY, Ident integer, Nom VARCHAR(200))")

# Ficar la informació necessaria a les taules
# Taula dels alumnes
informacio=[
    ("1", "Alba", "Ballesteros", "Gil", "22/11", "C4","11:30","101", "56"),
    ("2", "Jara", "Baltasar", "Oliver", "22/11", "C3","11:30","101", "56"),
    ("3", "Rubén", "Carranza", "Cortés", "22/11", "","11:30","101", "57"),
    ("4", "Laia", "Castelblanque", "Torrente", "22/11", "C5","11:30","101", "58"),
    ("5", "Noa", "Coronado", "Fernández", "22/11", "SOC7","11:30","101", "59"),
    ("6", "Eric", "Cortegana", "López", "22/11", "MAT3","11:30","101", "60"),
    ("7", "Joan", "Fernández", "Moreira", "22/11", "C7", "11:30", "101", "55"),
    ("8", "Iker", "Fresneda", "Santiago", "22/11", "HUM1","11:30","101", "61"),
    ("9", "Abril", "García", "Candelera", "22/11", "","11:30","101", "62"),
    ("10", "Daniel", "García", "Candelera", "22/11", "MAT2","11:45", "101", "53"),
    ("11", "Sara", "Giménez", "Ariza", "22/11", "EXP2","11:30","101", "64"),
    ("12", "Ariadna", "Gómez", "Romagosa", "22/11", "EXP1","11:30","101", "65"),
    ("13", "Aitana", "Jubierre", "Llop", "22/11", "C6","11:30","101", "66"),
    ("14", "Nàdia", "Jubierre", "Llop", "22/11", "C1","11:30","101", "67"),
    ("15", "Álex", "Lara", "Bailón", "21/11", "MAT1","8:30", "101", "54"),
    ("16", "Paula", "Latorre", "Fonseca", "22/11", "","11:30","101", "58"),
    ("17", "Martina", "López", "Cote", "22/11", "C8","11:30","101", "68"),
    ("18", "Eva", "Martínez", "Sans", "22/11", "","11:30","101", "69"),
    ("19", "Pau", "Piquer", "Pulgarín", "21/11", "EXP3","11:30", "101", "64"),
    ("20", "Ángel", "Roso", "Martín", "20/11", "EFIS1","9:00", "101", "70"),
    ("21", "Diana", "Saez", "Ortiz", "22/11", "TEC1","11:30","101", "71"),
    ("22", "Adrián", "Valverde", "Ambrosio", "20/11", "TEC2","12:00", "101", "52"),
    ("23", "Ámbar", "Vera", "", "22/11", "","11:30","101", "68"),
    ("24", "Laura", "Aguilera", "López", "22/11", "CAT4","11:30","101", "72"),
    ("25", "Ghizlan", "Aoufi", "Aoufi", "22/11", "SOC1","11:30","101", "73"),
    ("26", "Ana", "Cancho", "Ortiz", "22/11", "ORI2","11:30","101", "74"),
    ("27", "Alba", "Caritg", "Arenas", "22/11", "ORI3","11:30","101", "75"),
    ("28", "Weijie", "Chen", "Pan", "22/11", "CAT1","11:30","101", "76"),
    ("29", "Marc", "Choez", "", "22/11", "C2","11:30","101", "77"),
    ("30", "Pau", "Cordón", "Carrasco", "22/11", "", "11:30", "101", "78"),
    ("31", "Judith", "Esteven", "Perera", "22/11", "","11:30","101", "79"),
    ("32", "Adrián", "García", "Sánchez", "22/11", "","11:30","101", "80"),
    ("33", "Alexia", "García", "Sevilla", "22/11", "ORI1","11:30","101", "61"),
    ("34", "Iker", "Gil", "Carrión", "22/11", "CAT3","11:30","101", "81"),
    ("35", "Carolina", "Guerrero", "Serrano", "22/11", "EST1","11:30","101", "82"),
    ("36", "Yassine", "Khouya", "", "22/11", "","11:30","101", "53"),
    ("37", "Sergi", "Llaveria", "Nuñez", "22/11", "","11:30","101", "83"),
    ("38", "Mónica", "Martín", "Cardosa", "22/11", "CAT2","11:30","101", "84"),
    ("39", "Álex", "Martín", "Oliva", "22/11", "SOC4","11:30","101", "85"),
    ("40", "Miriam", "Martínez", "Valverde", "22/11", "","11:30","101", "86"),
    ("41", "David", "Mejías", "Felguera", "22/11", "CAST1","11:30","101", "87"),
    ("42", "Alison", "Menendez", "Choez", "22/11", "","11:30","101", "80"),
    ("43", "Marcos", "Moreira", "Medina", "22/11", "SOC6","11:30","101", "88"),
    ("44", "Alvaro", "Navajas", "Navarro", "22/11", "","11:30","101", "79"),
    ("45", "Joel", "Perulero", "Camapyo", "22/11", "","11:30","101", "80"),
    ("46", "Pol", "Rodríguez", "Agenjo", "22/11", "","11:30","101", "89"),
    ("47", "Lucía", "Roldán", "Fernández", "22/11", "SOC5","11:30","101", "90"),
    ("48", "Claudia", "Ruíz", "Borrago", "22/11", "","11:30","101", "91"),
    ("49", "Miriam", "Santader","Gracia", "22/11", "SOC2","11:30","101", "92"),
    ("50", "Aina", "Serra", "Perelló", "22/11", "SOC3","11:30","101", "59"),
    ("51", "Alexis", "Villamur", "Alvarado", "22/11", "","11:30","101", "86")
    ] 

# Taula dels professors
informacio2=[
    ("52", "Ángel", "Gómez", "", "22", "00", "00", "22", "00", "00"),
    ("53", "Jordi", "Limones", "Villalba", "10", "00", "00", "10", "00", "00"),
    ("54", "Juan Manuel", "Campanon", "Martín", "15", "00","00", "15", "00", "00"),
    ("55", "Roser", "Teixidor", "Macias", "7","00","00", "7","00", "00"),
    ("56", "Yolanda", "Losa", "Martínez", "1", "2","00", "1", "2", "00"),
    ("57", "Sílvia", "Mejías", "", "3","00","00", "3","00", "00"),
    ("58", "Conchi", "Bataller", "Barceló", "4", "16","00", "4", "16", "00"),
    ("59", "Albert", "Guasch", "", "5", "50","00", "5", "50", "00"),
    ("60", "Eliana", "Hernández", "Hernández", "6","00","00", "6","00", "00"),
    ("61", "Carles", "Ordóñez", "Álvarez", "8", "33","00", "8", "33", "00"),
    ("62", "Laia", "López", "Manrique", "9","00","00", "9","00", "00"),
    ("63", "Jordi", "Limones", "Villalba", "10","00","00", "10","00", "00"),
    ("64", "Estefania", "Grau", "Noguera", "11", "19","00", "11", "19", "00"),
    ("65", "Raquel", "Vilda", "Andrés", "12","00","00", "12","00", "00"),
    ("66", "Estela", "Roig", "Ferrer", "13","00","00", "13","00", "00"),
    ("67", "José María", "González", "", "14","00","00", "14","00", "00"),
    ("68", "Eulàlia", "Ripoll", "", "17","23","00", "17","23", "00"),
    ("69", "Àngels", "Luque", "Rosua", "18","00","00", "18","00", "00"),
    ("70", "Inés", "Nguema", "Mesas", "20","00","00", "20","00", "00"),
    ("71", "Raül", "Gilberte", "Abella", "21","00","00", "21","00", "00"),
    ("72", "Arnau", "Pujadas", "Jorba", "24","00","00", "24","00", "00"),
    ("73", "Beatriz", "Jiménez", "Martos", "25","00","00", "25","00", "00"),
    ("74", "Àngels", "Izquierdo", "", "26","00","00", "26","00", "00"),
    ("75", "Pilar", "Àlvarez", "Larios", "27","00","00", "27","00", "00"),
    ("76", "José Miguel", "Pérez", "Peinado", "28","00","00", "28","00", "00"),
    ("77", "Virginia", "Fernández", "López", "29","00","00", "29","00", "00"),
    ("78", "Beatriz", "Ramírez", "Rodríguez", "30", "00","00", "30", "00", "00"),
    ("79", "Queralt", "Bernàcer", "Sanjuan", "31","44","00", "31","44", "00"),
    ("80", "Marc", "Garriga", "Solanas", "32", "42", "45", "32", "42", "45"),
    ("81", "Catalina", "Planells", "Ripoll", "34","00","00", "34","00", "00"),
    ("82", "MagalÍ Chane", "Yu", "Chiu", "35","00","00", "35","00", "00"),
    ("83", "Mireia", "Mateu", "", "37","00","00", "37","00", "00"),
    ("84", "Anna", "Bou", "Fernández", "38","00","00", "38","00", "00"),
    ("85", "Pablo", "Montes", "Gómez", "39","00","00", "39","00", "00"),
    ("86", "Antoni", "Loro", "", "40", "51","00", "40", "51", "00"),
    ("87", "Antonio", "Cano", "López", "41","00","00", "41","00", "00"),
    ("88", "Nàdia", "Varo", "Moral", "43","00","00", "43","00", "00"),
    ("89", "Carolina", "Sandoval", "Landaburu", "46","00","00", "46","00", "00"),
    ("90", "Jorge", "Torres", "Hernàndez", "47","00","00", "47","00", "00"),
    ("91", "Anna", "Garcia", "Torres", "48","00","00", "48","00", "00"),
    ("92", "Jordi", "Closa", "", "49","00","00", "49","00", "00")
]

# Taula dels TRs
informacio3=[
    ("C1","14","Investigació i experimentació amb animals amb diverses finalitats i altres alternatives"),
    ("C2","29","Relacions d’humans i gossos. El millor amic de l’home?"),
    ("C3","2","Investigació sobre la resistència als antibiòtics. Per què ens trobem davant d’una crisi sanitària?"),
    ("C4","1","La capacitat regenerativa de les planàries"),
    ("C5","4","Senzillament, agafar la mà amb amor. Estudi del funcionament de les cures pal·liatives sobre si veritablement ajuden"),
    ("C6","13","Combinació d’inhibidors i quimioteràpia pel tractament del càncer de mama"),
    ("C7","7","Estudi sobre la supremacia de la femella més vella en goril·les"),
    ("C8","17","La química del perfum"),
    ("SOC1","25","Harragas: Anàlisi de l'experiència migratòria dels marroquins a Espanya"),
    ("SOC2","49","Estudi de l’explotació laboral a Espanya"),
    ("SOC3","50","Una aproximació al paper de les ONG com agents de canvi"),
    ("SOC4","39","Fosses del Franquisme. L’impacte de la repressió durant la guerra civil i la repressió franquista"),
    ("SOC5","47","Investigació i experimentació durant l’època nazi"),
    ("SOC6","43","Evolució, feminització i anàlisi del servei domèstic a Espanya"),
    ("SOC7","5","Els infants robats durant el franquisme i la transició"),
    ("EFIS1","20","Lesiones deportivas en adolescentes"),
    ("EXP1","12","Els edificis energèticament eficients"),
    ("EXP2","11","Maurits Cornelis Escher: Quan les matemàtiques i la psicologia es transformen en art"),
    ("EXP3","19","Estudi de les cases prefabricades i modulars com a vivenda emergent"),
    ("HUM1","8","El relat i la ciència-ficció."),
    ("CAST1","41","Cómo nace un libro"),
    ("CAT1","28","Artistes i llibertat d'expressió: Cal censurar les lletres de les cançons?"),
    ("CAT2","38","La influència de l’astrologia en la societat occidental"),
    ("CAT3","34","Comparació entre el periodisme analogic i digital"),
    ("CAT4","24","Introducció a l’obra musical de Charles Camille Saint-Saëns (Anàlisi de Introduction et rondo capriccioso en la mineur op. 28)"),
    ("EST1","35","L'apprentissage du français: Prosodie et interlangue"),
    ("MAT1","15","Investigació i inversió en Bitcoin"),
    ("MAT2","10","Leonhard Euler y la geometría."),
    ("MAT3","6","Es pot programar un Excel que resolgui sudokus?"),
    ("ORI1","33","Tòpics de gènere i com afecten a les persones"),
    ("ORI2","26","Els estereotips de gènere en els influencers i el seu impacte en els adolescents"),
    ("ORI3","27","Les conseqüències psicològiques de l’adopció"),
    ("TEC1","21","Elaboració de la història dels videojocs i desenvolupament d’un amb Unity"),
    ("TEC2","22","Software de gestió i programació en Python")
    ]

# Fiquem la informació a les diferents taules
connexio.executemany("INSERT OR IGNORE INTO INFORMACIO VALUES (?,?,?,?,?,?,?,?,?)", informacio)
connexio.executemany("INSERT OR IGNORE INTO INFORMACIO2 VALUES (?,?,?,?,?,?,?,?,?,?)", informacio2)
connexio.executemany("INSERT OR IGNORE INTO INFORMACIO3 VALUES (?,?,?)", informacio3)

# Desar canvis base de dades 
basededades.commit()
# Tancar connexió amb la base de dades 
basededades.close()
