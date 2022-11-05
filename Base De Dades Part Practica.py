# Import llibreria per a la base de dades 
import sqlite3

# Connexió base de dades 
basededades=sqlite3.connect("BaseDeDades")
connexio=basededades.cursor()

# Creació taules
connexio.execute("CREATE TABLE IF NOT EXISTS INFORMACIO (Ident integer PRIMARY KEY, Nom VARCHAR(100), Primer_Cognom VARCHAR(20), Segon_Cognom VARCHAR(20), Data VARCHAR(10), Tema VARCHAR(50), Hora VARCHAR(22), Aula VARCHAR(50), Tutor VARCHAR(50), Tribunal1 VARCHAR(50), Tribunal2 VARCHAR(50), Tribunal3 VARCHAR(50))") 
connexio.execute("CREATE TABLE IF NOT EXISTS INFORMACIO2 (Ident integer PRIMARY KEY, Nom VARCHAR(100), Primer_Cognom VARCHAR(20), Segon_Cognom VARCHAR(20), Alumne_TR1 VARCHAR(100), Alumne_TR2 VARCHAR(100), Alumne_TR3 VARCHAR(100), Alumne_TR1ibunal1 VARCHAR(100), Alumne_TR1ibunal2 VARCHAR(100), Alumne_TR1ibunal3 VARCHAR(100), Alumne_TR1ibunal4 VARCHAR(100), Alumne_TR1ibunal5 VARCHAR(100), Alumne_TR1ibunal6 VARCHAR(100), Alumne_TR1ibunal7 VARCHAR(100), Alumne_TR1ibunal8 VARCHAR(100), Alumne_TR1ibunal9 VARCHAR(100), Alumne_TR1ibunal10 VARCHAR(100), Alumne_TR1ibunal11 VARCHAR(100))")
connexio.execute("CREATE TABLE IF NOT EXISTS INFORMACIO3 (Ident_TR VARCHAR(100) PRIMARY KEY, Ident integer, Nom VARCHAR(200))")

# Ficar la informació necessaria a les taules
# Taula dels alumnes
informacio=[
    ("1", "Alba", "Ballesteros", "Gil", "8/11", "C4", "11:15", "1r Batx B", "56", "56", "61", "66"),
    ("2", "Jara", "Baltasar", "Oliver", "8/11", "C3", "11:15", "1r Batx B", "56", "56", "61", "66"),
    ("3", "Rubén", "Carranza", "Cortés", "8/11", "TEC3", "8:55", "1r Batx B", "57", "52", "57", "88"),
    ("4", "Laia", "Castelblanque", "Torrente", "8/11", "C5", "8:55", "2n Batx B", "58", "58", "71", "79"),
    ("5", "Noa", "Coronado", "Fernández", "8/11", "SOC6", "13:05", "2n Batx A", "59", "59", "86", "88"),
    ("6", "Eric", "Cortegana", "López", "8/11", "MAT3", "8:00", "Biblioteca", "60", "60", "80", "83"),
    ("7", "Joan", "Fernández", "Moreira", "8/11", "C7", "13:35", "1r Batx B", "55", "55", "73", "77"),
    ("8", "Iker", "Fresneda", "Santiago", "8/11", "HUM1", "9:50", "Biblioteca", "61", "54", "60", "61"),
    ("9", "Abril", "García", "Candelera", "8/11", "CAST2", "8:55", "2n Batx A", "62", "62", "92", "94"),
    ("10", "Daniel", "García", "Candelera", "8/11", "MAT2", "13:35", "1r Batx A", "53", "53", "54", "61"),
    ("11", "Sara", "Giménez", "Ariza", "8/11", "EXP2", "8:55", "1r Batx A", "64", "64", "80", "83"),
    ("12", "Ariadna", "Gómez", "Romagosa", "8/11", "EXP1", "11:15", "1r Batx A", "65", "65", "71", "72"),
    ("13", "Aitana", "Jubierre", "Llop", "8/11", "C6", "8:00", "1r Batx B", "66", "53", "66", "67"),
    ("14", "Nàdia", "Jubierre", "Llop", "8/11", "C1", "8:00", "1r Batx B", "67", "53", "66", "67"),
    ("15", "Álex", "Lara", "Bailón", "8/11", "MAT1", "13:35", "1r Batx A", "54", "53", "54", "61"),
    ("16", "Paula", "Latorre", "Fonseca", "8/11", "C9", "12:10", "1r Batx B", "58", "58", "66", "86"),
    ("17", "Martina", "López", "Cote", "8/11", "C8", "9:50", "2n Batx A", "68", "67", "68", "98"),
    ("18", "Eva", "Martínez", "Sans", "8/11", "EFIS2", "13:05", "2n Batx B", "69", "69", "70", "99"),
    ("19", "Pau", "Piquer", "Pulgarín", "8/11", "EXP3", "13:05", "1r Batx A", "64", "64", "65", "97"),
    ("20", "Ángel", "Roso", "Martín", "8/11", "EFIS1", "12:10", "1r Batx A", "70", "70", "73", "89"),
    ("21", "Diana", "Saez", "Ortiz", "8/11", "TEC1", "8:55", "2n Batx B", "71", "58", "71", "79"),
    ("22", "Adrián", "Valverde", "Ambrosio", "8/11", "TEC2", "8:55", "1r Batx B", "52", "52", "57", "88"),
    ("23", "Ámbar", "Vera", "", "8/11", "C10", "9:50", "2n Batx A", "68", "67", "68", "98"),
    ("24", "Laura", "Aguilera", "López", "8/11", "CAT4", "11:15", "1r Batx A", "72", "65", "71", "72"),
    ("25", "Ghizlan", "Aoufi", "Aoufi", "8/11", "SOC1", "9:50", "1r Batx A", "73", "63", "73", "85"),
    ("26", "Ana", "Cancho", "Ortiz", "8/11", "ORI2", "8:55", "Biblioteca", "74", "74", "78", "95"),
    ("27", "Alba", "Caritg", "Arenas", "8/11", "ORI3", "11:15", "Biblioteca", "75", "59", "75", "96"),
    ("28", "Weijie", "Chen", "Pan", "8/11", "CAT1", "8:00", "1r Batx A", "76", "61", "73", "76"),
    ("29", "Marc", "Choez", "", "8/11", "C2", "13:35", "1r Batx B", "77", "55", "73", "77"),
    ("30", "Pau", "Cordón", "Carrasco", "8/11", "ORI4", "8:55", "Biblioteca", "78", "74", "78", "95"),
    ("31", "Judith", "Esteven", "Perera", "8/11", "ORI5", "12:10", "Biblioteca", "79", "79", "80", "87"),
    ("32", "Adrián", "García", "Sánchez", "8/11", "SOC7", "8:55", "1r Batx A", "80", "64", "80", "83"),
    ("33", "Alexia", "García", "Sevilla", "8/11", "ORI1", "8:00", "1r Batx A", "61", "61", "73", "76"),
    ("34", "Iker", "Gil", "Carrión", "8/11", "CAT3", "9:50", "1r Batx B", "81", "55", "81", "84"),
    ("35", "Carolina", "Guerrero", "Serrano", "8/11", "EST1", "13:05", "1r Batx B", "82", "55", "82", "93"),
    ("36", "Yassine", "Khouya", "", "8/11", "MAT4", "9:50", "Biblioteca", "54", "54", "60", "61"),
    ("37", "Sergi", "Llaveria", "Nuñez", "8/11", "MAT5", "8:00", "Biblioteca", "83", "60", "80", "83"),
    ("38", "Mónica", "Martín", "Cardosa", "8/11", "CAT2", "9:50", "1r Batx B", "84", "55", "81", "84"),
    ("39", "Álex", "Martín", "Oliva", "8/11", "SOC4", "9:50", "1r Batx A", "85", "63", "73", "85"),
    ("40", "Miriam", "Martínez", "Valverde", "8/11", "MAT6", "12:10", "1r Batx B", "86", "58", "66", "86"),
    ("41", "David", "Mejías", "Felguera", "8/11", "CAST1", "12:10", "Biblioteca", "87", "79", "80", "87"),
    ("42", "Alison", "Menendez", "Choez", "8/11", "ORI6", "13:05", "Biblioteca", "80", "79", "80", "87"),
    ("43", "Marcos", "Moreira", "Medina", "", "", "", "", "", "", "", ""),
    ("44", "Alvaro", "Navajas", "Navarro", "", "", "", "", "", "", "", ""),
    ("45", "Joel", "Perulero", "Campayo", "8/11", "ORI7", "13:35", "Biblioteca", "80", "80", "86", "97"),
    ("46", "Pol", "Rodríguez", "Agenjo", "8/11", "EFIS3", "12:10", "1r Batx A", "89", "70", "73", "89"),
    ("47", "Lucía", "Roldán", "Fernández", "9/11", "SOC5", "11:15", "Sala d'actes", "90", "80", "90", "91"),
    ("48", "Claudia", "Ruíz", "Borrago", "9/11", "SOC8", "11:15", "Sala d'actes", "91", "80", "90", "91"),
    ("49", "Miriam", "Santader", "Gracia", "8/11", "SOC2", "8:55", "2n Batx A", "92", "62", "92", "94"),
    ("50", "Aina", "Serra", "Perelló", "8/11", "SOC3", "11:15", "Biblioteca", "59", "59", "75", "96"),
    ("51", "Alexis", "Villamur", "Alvarado", "8/11", "SOC9", "13:35", "Biblioteca", "86", "80", "86", "97")
    ] 

# Taula dels professors
informacio2=[
    ("52", "Àngel", "Gómez", "", "22", "00", "00", "3", "22", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("53", "Jordi", "Limones", "", "10", "00", "00", "10", "13", "14", "15", "00", "00", "00", "00", "00", "00", "00"),
    ("54", "Juan Manuel", "Campanon", "", "15", "36", "00", "8", "10", "15", "36", "00", "00", "00", "00", "00", "00", "00"),
    ("55", "Roser", "Teixidor", "", "7", "00", "00", "7", "29", "34", "35", "38", "00", "00", "00", "00", "00", "00"),
    ("56", "Yolanda", "Losa", "", "1", "2", "00", "1", "2", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("57", "Sílvia", "Mejías", "", "3", "00", "00", "3", "22", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("58", "Conchi", "Bataller", "", "4", "16", "00", "4", "16", "21", "40", "00", "00", "00", "00", "00", "00", "00"),
    ("59", "Albert", "Guasch", "", "5", "50", "00", "5", "27", "50", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("60", "Eliana", "Hernández", "", "6", "00", "00", "6", "8", "36", "37", "00", "00", "00", "00", "00", "00", "00"),
    ("61", "Carles", "Ordóñez", "", "8", "33", "00", "1", "2", "8", "10", "15", "28", "33", "36", "00", "00", "00"),
    ("62", "Laia", "López", "", "9", "00", "00", "9", "49", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("63", "Montserrat", "Garrabou", "", "00", "00", "00", "25", "39", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("64", "Estefania", "Grau", "", "11", "19", "00", "11", "19", "32", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("65", "Raquel", "Vilda", "", "12", "00", "00", "12", "19", "24", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("66", "Estela", "Roig", "", "13", "00", "00", "1", "2", "13", "14", "16", "40", "00", "00", "00", "00", "00"),
    ("67", "José María", "González", "", "14", "00", "00", "13", "14", "17", "23", "00", "00", "00", "00", "00", "00", "00"),
    ("68", "Eulàlia", "Ripoll", "", "17", "23", "00", "17", "23", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("69", "Àngels", "Luque", "", "18", "00", "00", "18", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("70", "Inés", "Nguema", "", "20", "00", "00", "18", "20", "46", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("71", "Raül", "Gilberte", "", "21", "00", "00", "4", "12", "21", "24", "00", "00", "00", "00", "00", "00", "00"),
    ("72", "Arnau", "Pujadas", "", "24", "00", "00", "12", "24", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("73", "Beatriz", "Jiménez", "", "25", "00", "00", "7", "20", "25", "28", "29", "33", "39", "46", "00", "00", "00"),
    ("74", "Àngels", "Izquierdo", "", "26", "00", "00", "26", "30", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("75", "Pilar", "Àlvarez", "", "27", "00", "00", "27", "50", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("76", "José Miguel", "Pérez", "", "28", "00", "00", "28", "33", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("77", "Virginia", "Fernández", "", "29", "00", "00", "7", "29", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("78", "Beatriz", "Ramírez", "", "30", "00", "00", "26", "30", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("79", "Queralt", "Bernàcer", "", "31", "00", "00", "4", "21", "31", "41", "42", "00", "00", "00", "00", "00", "00"),
    ("80", "Marc", "Garriga", "", "32", "42", "45", "6", "11", "31", "32", "37", "41", "42", "45", "47", "48", "51"),
    ("81", "Catalina", "Planells", "", "34", "00", "00", "34", "38", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("82", "Magalí Chane", "Yu", "", "35", "00", "00", "35", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("83", "Mireia", "Mateu", "", "37", "00", "00", "6", "11", "32", "37", "00", "00", "00", "00", "00", "00", "00"),
    ("84", "Anna", "Bou", "", "38", "00", "00", "34", "38", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("85", "Pablo", "Montes", "", "39", "00", "00", "25", "39", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("86", "Antoni", "Loro", "", "40", "51", "00", "5", "16", "40", "45", "51", "00", "00", "00", "00", "00", "00"),
    ("87", "Antonio", "Cano", "", "41", "00", "00", "31", "41", "42", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("88", "Nàdia", "Varo", "", "00", "00", "00", "3", "5", "22", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("89", "Carolina", "Sandoval", "", "46", "00", "00", "20", "46", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("90", "Jorge", "Torres", "", "47", "00", "00", "47", "48", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("91", "Anna", "Garcia", "", "48", "00", "00", "47", "48", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("92", "Jordi", "Closa", "", "49", "00", "00", "9", "49", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("93", "Carmen", "Cabezos", "", "00", "00", "00", "35", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("94", "Mónica", "Jimeno", "", "00", "00", "00", "9", "49", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("95", "Joan", "Amils", "", "00", "00", "00", "26", "30", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("96", "Anabel", "Mejuto", "", "00", "00", "00", "27", "50", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("97", "Irene", "Cuadrado", "", "00", "00", "00", "19", "45", "51", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("98", "Ana", "Candela", "", "00", "00", "00", "17", "23", "00", "00", "00", "00", "00", "00", "00", "00", "00"),
    ("99", "Jordi", "Carbonell", "", "00", "00", "00", "18", "00", "00", "00", "00", "00", "00", "00", "00", "00", "00")
]

# Taula dels TRs
informacio3=[
    ("C1", "14", "Investigació i experimentació amb animals amb diverses finalitats i altres alternatives"),
    ("C2", "29", "Relacions d’humans i gossos. El millor amic de l’home?"),
    ("C3", "2", "Investigació sobre la resistència als antibiòtics. Per què ens trobem davant d’una crisi sanitària?"),
    ("C4", "1", "La capacitat regenerativa de les planàries"),
    ("C5", "4", "Senzillament, agafar la mà amb amor. Estudi del funcionament de les cures pal·liatives sobre si veritablement ajuden"),
    ("C6", "13", "Combinació d’inhibidors i quimioteràpia pel tractament del càncer de mama"),
    ("C7", "7", "Estudi sobre la supremacia de la femella més vella en goril·les"),
    ("C8", "17", "La química del perfum"),
    ("C9", "16", "La fecundació in vitro i l’ambigüitat del mosaïcisme embrionari"),
    ("C10", "23", "L’aplicació del mètode CRISPR-Cas9 a les malalties genètiques"),
    ("SOC1", "25", "Harragas: Anàlisi de l'experiència migratòria dels marroquins a Espanya"),
    ("SOC2", "49", "Estudi de l’explotació laboral a Espanya"),
    ("SOC3", "50", "Una aproximació al paper de les ONG com agents de canvi"),
    ("SOC4", "39", "Fosses del Franquisme. L’impacte de la repressió durant la guerra civil i la repressió franquista"),
    ("SOC5", "47", "Investigació i experimentació durant l’època nazi"),
    ("SOC6", "5", "Els infants robats durant el franquisme i la transició"),
    ("SOC7", "32", "Estudio del partido político de Vox en función del programa electoral y su obra de gobierno"),
    ("SOC8", "48", "Els efectes de la pandèmia en la salut mental de la població"),
    ("SOC9", "51", "Es troba el sector agrari en declivi?"),
    ("EFIS1", "20", "Lesiones deportivas en adolescentes"),
    ("EFIS2", "18", "Les lesions a l’atletisme"),
    ("EFIS3", "46", "Discriminacio al fútbol femeni"),
    ("EXP1", "12", "Els edificis energèticament eficients"),
    ("EXP2", "11", "Maurits Cornelis Escher: Quan les matemàtiques i la psicologia es transformen en art"),
    ("EXP3", "19", "Estudi de les cases prefabricades i modulars com a vivenda emergent"),
    ("HUM1", "8", "El relat i la ciència-ficció"),
    ("CAST1", "41", "Cómo nace un libro"),
    ("CAST2", "9", "“El universo femenino de Lorca”. La casa de Bernarda Alba"),
    ("CAT1", "28", "Artistes i llibertat d'expressió: Cal censurar les lletres de les cançons?"),
    ("CAT2", "38", "La influència de l’astrologia en la societat occidental"),
    ("CAT3", "34", "Comparació entre el periodisme analogic i digital"),
    ("CAT4", "24", "Introducció a l’obra musical de Charles Camille Saint-Saëns (Anàlisi de Introduction et rondo capriccioso en la mineur op. 28)"),
    ("EST1", "35", "L'apprentissage du français: Prosodie et interlangue"),
    ("MAT1", "15", "Investigació i inversió en Bitcoin"),
    ("MAT2", "10", "Leonhard Euler y la geometría"),
    ("MAT3", "6", "Es pot programar un Excel que resolgui sudokus?"),
    ("MAT4", "36", "El funcionament de les criptomonedes i el seu impacte en la societat actual"),
    ("MAT5", "37", "Estudi de les loteries a Espanya"),
    ("MAT6", "40", "Grup Inditex i les seves estratègies"),
    ("ORI1", "33", "Tòpics de gènere i com afecten a les persones"),
    ("ORI2", "26", "Els estereotips de gènere en els influencers i el seu impacte en els adolescents"),
    ("ORI3", "27", "Les conseqüències psicològiques de l’adopció"),
    ("ORI4", "30", "Consumició de marihuana en els adolescents de Sant Feliu i com els hi afecta"),
    ("ORI5", "31", "Anàlisi de l’alumnat nouvingut a l’institut Martí Dot i el seu contacte amb el català"),
    ("ORI6", "42", "Anàlisi comparativa de l'ús dels llatinismes en la premsa espanyola i en l'equatoriana"),
    ("ORI7", "45", "Estudi de l’emancipació dels joves de Sant Feliu de Llobregat en relació amb les dades estadístiques catalanes i espanyoles"),
    ("TEC1", "21", "Elaboració de la història dels videojocs i desenvolupament d’un amb Unity"),
    ("TEC2", "22", "Software de gestió i programació en Python"),
    ("TEC3", "3", "Com podria ser la instal·lació de plaques solars a l’institut Martí Dot")
    ]

# Fiquem la informació a les diferents taules
connexio.executemany("INSERT OR IGNORE INTO INFORMACIO VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", informacio)
connexio.executemany("INSERT OR IGNORE INTO INFORMACIO2 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", informacio2)
connexio.executemany("INSERT OR IGNORE INTO INFORMACIO3 VALUES (?,?,?)", informacio3)

# Desar canvis base de dades 
basededades.commit()
# Tancar connexió amb la base de dades 
basededades.close()
