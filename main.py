from typing import Final
from telegram import Update 
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = "YOUR BOT'S TOKEN"
BOT_USERNAME: Final = '@USERNAME'

pic = 'periodic.jpg'

#Commands
async def start_command(update: Update, context: ContextTypes):
    await update.message.reply_text('Hello !')

async def help_command(update: Update, context: ContextTypes):
    await update.message.reply_text("I can give you some info about periodic table .")

async def periodic_table_command(update: Update, context: ContextTypes):
    await update.message.reply_photo(pic)

async def mandaliof_command(update: Update, context: ContextTypes):
    await update.message.reply_text("Mendeleev was born in the village of Verkhnie Aremzyani, near Tobolsk in Siberia, to Ivan Pavlovich Mendeleev [ru] (1783–1847) and Maria Dmitrievna Mendeleeva (née Kornilieva) (1793–1850).[3][4] Ivan worked as a school principal and a teacher of fine arts, politics and philosophy at the Tambov and Saratov gymnasiums.[5] Ivan's father, Pavel Maximovich Sokolov, was a Russian Orthodox priest from the Tver region.[6] As per the tradition of priests of that time, Pavel's children were given new family names while attending the theological seminary,[7] with Ivan getting the family name Mendeleev after the name of a local landlord")

async def avogadro_command(update: Update, context: ContextTypes):
    await update.message.reply_text('6.02 * (10**23)')

async def pi_command(update: Update, context: ContextTypes):
    await update.message.reply_text('3.14')

async def metals_command(update: Update, context: ContextTypes):

    await update.message.reply_text("""We have \n 
3	Li	Lithium 
4	Be	Beryllium
11	Na	Sodium
12	Mg	Magnesium
13	Al	Aluminum
19	K	Potassium
20	Ca	Calcium
21	Sc	Scandium
22	Ti	Titanium
23	V	Vanadium
24	Cr	Chromium
25	Mn	Manganese
26	Fe	Iron
27	Co	Cobalt
28	Ni	Nickel
29	Cu	Copper
30	Zn	Zinc
31	Ga	Gallium
37	Rb	Rubidium
38	Sr	Strontium
39	Y	Yttrium
40	Zr	Zirconium
41	Nb	Niobium
42	Mo	Molybdenum
43	Tc	Technetium
44	Ru	Ruthenium
45	Rh	Rhodium
46	Pd	Palladium
47	Ag	Silver
48	Cd	Cadmium
49	In	Indium
50	Sn	Tin
55	Cs	Cesium
56	Ba	Barium
57	La	Lanthanum
58	Ce	Cerium
59	Pr	Praseodymium
60	Nd	Neodymium
61	Pm	Promethium
62	Sm	Samarium
63	Eu	Europium
64	Gd	Gadolinium
65	Tb	Terbium
66	Dy	Dysprosium
67	Ho	Holmium
68	Er	Erbium
69	Tm	Thulium
70	Yb	Ytterbium
71	Lu	Lutetium
72	Hf	Hafnium
73	Ta	Tantalum
74	W	Tungsten
75	Re	Rhenium
76	Os	Osmium
77	Ir	Iridium
78	Pt	Platinum
79	Au	Gold
80	Hg	Mercury
81	Tl	Thallium
82	Pb	Lead
83	Bi	Bismuth
84	Po	Polonium
87	Fr	Francium
88	Ra	Radium
89	Ac	Actinium
90	Th	Thorium
91	Pa	Protactinium
92	U	Uranium
93	Np	Neptunium
94	Pu	Plutonium
95	Am	Americium
96	Cm	Curium
97	Bk	Berkelium
98	Cf	Californium
99	Es	Einsteinium
100	Fm	Fermium
101	Md	Mendelevium
102	No	Nobelium
103	Lr	Lawrencium
104	Rf	Rutherfordium
105	Db	Dubnium
106	Sg	Seaborgium
107	Bh	Bohrium
108	Hs	Hassium
109	Mt	Meitnerium
110	Ds	Darmstadtium
111	Rg	Roentgenium
112	Cn	Copernicium
113	Nh	Nihonium
114	Fl	Flerovium
115	Mc	Moscovium
116	Lv	Livermorium""")

async def semimetals_command(update: Update, context: ContextTypes):
    await update.message.reply_text(""" we have \n 5	B	Boron
14	Si	Silicon
32	Ge	Germanium
33	As	Arsenic
51	Sb	Antimony
52	Te	Tellurium
84	Po	Polonium
117	Ts	Tennessine""")
    
async def nonmetals_command(update: Update, context: ContextTypes):
    await update.message.reply_text(""" we have \n 1	H	Hydrogen
2	He	Helium
6	C	Carbon
7	N	Nitrogen
8	O	Oxygen
9	F	Fluorine
10	Ne	Neon
15	P	Phosphorus
16	S	Sulfur
17	Cl	Chlorine
18	Ar	Argon
34	Se	Selenium
35	Br	Bromine
36	Kr	Krypton
53	I	Iodine
54	Xe	Xenon
85	At	Astatine
86	Rn	Radon
117	Ts	Tennessine
118	Og	Oganesson""")

# Responses 
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hello !'
    
    if 'how are you' in processed:
        return 'Fine, thanks for asking.'
    
    return 'I do not understand.' 

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text 

    print(f' user {update.message.chat.id} in {message_type}: {text}')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip() 
            response: str = handle_response(new_text)
        else: 
            return  
    else:
        response: str = handle_response(text)

    print('Bot : ', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error.')

if __name__ == '__main__':
    print('start bot ...')
    app = Application.builder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('periodictable', periodic_table_command))
    app.add_handler(CommandHandler('avogadro', avogadro_command))
    app.add_handler(CommandHandler('pi', pi_command))
    app.add_handler(CommandHandler('metals', metals_command))
    app.add_handler(CommandHandler('semimetals', semimetals_command))
    app.add_handler(CommandHandler('nonmetals', nonmetals_command))
    app.add_handler(CommandHandler('mandaliof', mandaliof_command))

    # messages 
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # error 
    app.add_error_handler(error) 

    print('start polling ... ')
    app.run_polling(poll_interval=3)
